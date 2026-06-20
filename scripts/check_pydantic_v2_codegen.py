#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import subprocess
import sys
import tempfile
import warnings
from pathlib import Path
from types import ModuleType


REPO_ROOT = Path(__file__).resolve().parents[1]
ENTITIES_SPEC = REPO_ROOT / "specification" / "entities.yaml"
EXPECTED_ODDRN_EXAMPLE = "//aws/glue/{account_id}/{database}/{tablename}"


def fail(message: str) -> None:
    raise SystemExit(message)


def run_codegen(output: Path) -> None:
    command = [
        sys.executable,
        "-m",
        "datamodel_code_generator",
        "--input",
        str(ENTITIES_SPEC),
        "--output",
        str(output),
        "--input-file-type",
        "openapi",
        "--output-model-type",
        "pydantic_v2.BaseModel",
        "--field-extra-keys",
        "example",
        "--formatters",
        "black",
        "isort",
    ]
    completed = subprocess.run(command, cwd=REPO_ROOT, capture_output=True, text=True)
    if completed.returncode != 0:
        sys.stderr.write(completed.stdout)
        sys.stderr.write(completed.stderr)
        fail("datamodel-code-generator failed.")


def assert_generated_text_is_pydantic_v2_safe(generated: Path) -> None:
    text = generated.read_text()

    if "example=" in text:
        fail(
            "Generated Pydantic v2 model still contains deprecated "
            "Field(..., example=...) metadata."
        )

    if "json_schema_extra" not in text and "examples=" not in text:
        fail(
            "Generated model does not preserve OpenAPI examples through "
            "Pydantic v2-safe schema metadata."
        )


def import_generated_module(generated: Path) -> ModuleType:
    try:
        from pydantic.warnings import PydanticDeprecatedSince20
    except ImportError:
        fail(
            "pydantic>=2 is required. Install pydantic and "
            "datamodel-code-generator before running this check."
        )

    spec = importlib.util.spec_from_file_location("odd_models_pydantic_v2", generated)
    if spec is None or spec.loader is None:
        fail(f"Could not load generated module from {generated}.")

    module = importlib.util.module_from_spec(spec)
    with warnings.catch_warnings():
        warnings.simplefilter("error", PydanticDeprecatedSince20)
        spec.loader.exec_module(module)
    return module


def assert_example_is_preserved_in_schema(module: ModuleType) -> None:
    base_object = getattr(module, "BaseObject")
    base_object.model_rebuild(_types_namespace=vars(module))
    oddrn_schema = base_object.model_json_schema()["properties"]["oddrn"]

    if oddrn_schema.get("example") == EXPECTED_ODDRN_EXAMPLE:
        return

    examples = oddrn_schema.get("examples")
    if isinstance(examples, list) and EXPECTED_ODDRN_EXAMPLE in examples:
        return

    fail("Generated schema does not preserve the BaseObject.oddrn example.")


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp_dir:
        generated = Path(tmp_dir) / "odd_models_pydantic_v2.py"
        run_codegen(generated)
        assert_generated_text_is_pydantic_v2_safe(generated)
        module = import_generated_module(generated)
        assert_example_is_preserved_in_schema(module)

    print(
        "Pydantic v2 codegen is warning-free and preserves OpenAPI examples "
        "as schema metadata."
    )


if __name__ == "__main__":
    main()

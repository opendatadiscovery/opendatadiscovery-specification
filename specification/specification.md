# Specification

Version: Draft

## OpenDataDiscovery scope

OpenDataDiscovery specification is intentionally agnostic about the specifics of particular data sources and data catalogs. It exists to describe the semantics of data discovery process.

## Discovery process

Metadata discovery process is very simular to metrics/logs/traces gathering process. We might have pull or push model. Both of them is better for their use cases.

### Pull model

Pulling metadata directly from the source seems is the most straightforward way to gather metadata, but it may become a nightmare to develope and maintain a centralized fleet of domain-specific crawlers. OpenDataDiscovery introduces new entity: OpenDataDiscovery Adapater. The main goal of these adapaters are to be source specific and expose only information could be gathered from certain data source.s

### Push model

It supports for individual metadata providers push the information to the central repository via APIs.
This could be more prefered way for certain use cases. For example Airflow jobs runs and quality check runs.

## DataModel

Knowledge about data is spread amongst many people and systems. OpenDataDiscovery role is to provide a standard protoocol how metadata can be collected and correlated in as automated fashion as possible.
To enable many different datasources and tools to expose the metadata we need agreement on what data should be exposed and in what format (structures).
Specification contains of high level entities  DataInputs, DataTransformers, DataSets and DataConsumers.
Each entity has a unique url describing a place, system and an identifier in this system.

###  DataInputs

Is a source of your data, it could be described as a web site url, external s3 bucket or real life data place.

```proto
message DataInput {
    string url = 1;
    string description = 2;    
}
```

### DataSets

DataSet is a collectin of data stored in structured, semi-structued or unstructured format.
It might be a table in relational database, parquet file on s3 bucket, hive catalog table and so on.
DataSets could have subdatasets. For example Hive table is a dataset itself and it consists of DataSets as a folders/files on HDFS/S3.

```yaml
DataSet:
    type: object
    properties:
        oddrn:
          example: //aws/glue/{account_id}/{database}/{tablename}
          type: string
        name:
          type: string
        owner:
          example: //aws/iam/{account_id}/user/name
          type: string
        parentOddrn:
            type: string
            example: //aws/glue/{account_id}/{database}/{tablename}
        description:
            type: string
        updatedAt:
            format: date-time
            type: string
        subtype:
            enum:
                - DATASET_TABLE
                - DATASET_FILE
                - DATASET_FEATURE_GROUP
            type: string
        fieldList:
            items:
            $ref: '#/components/schemas/DataSetField'
            type: array
        dataSetList:
            items:
            $ref: '#/components/schemas/DataSet'
            type: array
    required:
        - description

DataSetField:
    type: object
    properties:
        type:
            $ref: '#/components/schemas/DataSetFieldType'
        defaultValue:
            type: string
        description:
            type: string
        required:
        - type

DataSetFieldType:
    type: object
    properties:
        name:
            type: string
        type:
            type: string
        logicalType:
            type: string
        isNullable:
            type: boolean
        isList:
            type: boolean
        isMap:
            type: boolean
        keyType:
            $ref: '#/components/schemas/DataSetFieldType'
        valueType:
            $ref: '#/components/schemas/DataSetFieldType'
        stats:
            $ref: '#/components/schemas/DataSetFieldStat'
        fieldList:
            type: array
            items:
            $ref: '#/components/schemas/DataSetFieldType'
        required:
        - type
        - isNullable
        - isMap
        - isList

```

#### Tables

Example oddrn
```//postgresql/{host}/{database}/{schema}/{tablename}```

#### Files

Example url:
```//aws/s3/{bucket}/{path}```

#### FeatureGroups

Example url:

```//feast/host/{namespace}/{featuregroup}```

###  DataTransformers

```proto
message DataTransformer {
    string url = 1; // url: airflow://{host}/{path}/{job_id}
    string description = 2;
    repeated string input_dataset_urls = 3;
    repeated string output_dataset_urls = 4; 
    string owner = 5;
}
```

#### ETL jobs

Example url: airflow://{host}/{path}/{job_id}  

#### ML Training jobs

Example url: kubeflow://{host}/{path}/{job_id}

### DataConsumers

```proto
message DataConsumer {
    string url = 1; // url: seldon://{host}/{path}/{model_id}  
    string description = 2;
    repeated string input_dataset_urls = 3;
    string owner = 4;
}
```

#### ML Models

Example url: ```sagemaker://{account_id}/{model_id}```

#### BI dashboards

Example url: ```tableu://{host}/{path}/{dashboard_id}```

### DataSetStats

```proto
message DataSetStat {
    string dataset_url = 1; // url: aws+glue://{account_id}/{database}/{tablename}
    string description = 2;
    string owner = 3;
    repeated DataSetColumnStat columns = 4; 
    uint64 count_rows = 5;
    timstamp last_update = 6;
    uint64 count_duplicates = 7;
}

message DataSetColumnStat {
    string name = 1;
    uint64 count_unqiues = 2;
    uint64 count_nulls = 3;
    uint64 count_non_nulls = 4;
    string max_value = 5;
    string min_value = 6;
    string average = 6;
}
```

### DataSetQualityTests

```proto
message DataSetQualityTest {
    string url = 1;
    repeated string dataset_urls = 2; // url: aws+glue://{account_id}/{database}/{tablename}
    repeated string columns = 3;
    string test_suite_url = 4;
    string test_name = 5;
    string description = 6;
    string owner = 7;
    Priority priority = 8;
    repeated string linked_urls = 9;
}

message DataSetQualityTestSuite {
    string url = 1;
    string description_url = 2;
}

message DataSetQualityCheckRun {
    string url = 1;
    timestamp run_at = 2;
    string run_by = 3;
    Status status = 4;
    string result = 5;
}
```

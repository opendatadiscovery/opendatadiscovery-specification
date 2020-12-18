# Specification

## OpenDataDiscovery scope

OpenDataDiscovery specification is intentionally agnostic about the specifics of particular data sources and data catalogs. It exists to describe the semantics of data discovery process.

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

```proto
message DataSet {
    string url = 1; // url: aws+glue://{account_id}/{database}/{tablename}
    string description = 2;
    repeated DataSet sub_datasets= 3;
    string owner = 4;
    repeated DataSetColumn columns = 5;
}

message DataSetColumn {
    string name = 1;
    string type = 2;
    boolean is_nullable = 3;
    string default_value = 4;    
}
```

#### Tables

Example url: postgresql://{host}/{database}/{schema}{tablename}

#### Files

Example url: url: aws+s3://{bucket}/{path}

#### FeatureGroups

Example url: url: feast://{host}/{featuregroup}

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

Example url: sagemaker://{account_id}/{model_id}

#### BI dashboards

Example url: tableu://{host}/{path}/{dashboard_id}

### DataSetStats

```proto
message DataSetStat {
    string dataset_url = 1; // url: aws+glue://{account_id}/{database}/{tablename}
    string description = 2;
    string owner = 3;
    repeated DataSetColumnStat columns = 4;    
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

### DataSetQualityChecks

```proto
message DataSetQualityChecks {
    string dataset_url = 1; // url: aws+glue://{account_id}/{database}/{tablename}
    string description = 2;
    string owner = 3;
    repeated QualityCheck cheks = 4;
}


```

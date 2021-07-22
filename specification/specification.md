# Open Data Discovery Specification

# Challenge

The rapid growth of data volumes and people dealing with it in organizations creates new challenges that never existed before.


<ol>
<li>Knowledge about data is scattered across numerous systems and owners</li>
<li>Legacy data catalogs use proprietary not interchangeable metadata formats</li> 
<li>Legacy data catalogs don’t support building federated systems</li> 
<li>Legacy data catalogs are limited to static data assets - tables, schemas and so on</li> 
<li>Legacy data catalogs provide no support of ML Models and data pipelines</li> 
<li>A centralized fleet of domain-specific crawlers is hard to develop, extend and maintain</li>
<li>Data discovery eats up to 30% of the time of data teams</li>
<li>Data discovery/access is the major barrier to applying AI at scale in organizations</li>
</ol>


Some open-source initiatives are already trying to address these challenges. For example, open-source data catalogs like Amundsen, DataHub, Marquez are built to reduce data discovery time. Their strong and, at the same time weak, side is the monolithic and closed design of the discovery process. It significantly limits the possibilities of reusing discovered metadata across other data discovery products and reduces scalability. These products are successful solutions to problems 1, 6, and 7. However, they don’t cover 2-5 and 8. 

Marquez's team introduced OpenLineage specification to standardize the data lineage discovery process. However, it doesn’t cover entities outside of Data Lakes / Warehouses world, like Dashboards, Pipelines, and ML Models. It also doesn’t enrich your metadata with quality tests information and results, and data profiling. 

# Proposed Solution

Open Data Discovery is an open standards specification that unifies metadata formats and allows multiple data sources and participants of the data discovery landscape to exchange metadata effectively, transparently, and consistently.   

It describes the semantics of the data discovery process as we envision it. It is data source agnostic by design and is intentionally not tied to the specifics of any particular data source or data catalog. 

Core features:

<ol>
<li>Standard <b>Open Data Discovery API (ODD API)</b> for currently known data entities</li>
<li><b>Extensible model</b> to include data entities that could show up</li> 
<li>Includes<b>entities for the ML world</b></li> 
<li><b>Federated Catalog of Catalogs</b> for data discovery</li> 
<li>A <b>reference implementation</b> based on ODD API specification</li> 
<li>An <b>Open-Source product</b> based on open standards</li>
<li><b>Composable and pluggable architecture</b> architecture to fit any data strategy/business requirements</li>
<li><b>Community-driven</b> to achieve better compatibility with a wide list of integrations</li>
</ol>

<p align="center">
<img src="./images/open-data-discovery-standard-before-after.jpg" width="600px" alt="open-data-discovery-standard-before-and-after"/>&nbsp;
</p>

**Diagram 1** shows 1) Currently existing discovery ecosystem, where multiple data sources (feature stores, ETL tools, ML pipelines, data warehouses, data quality tools) and data catalogs exchange data with each other directly. 2) How the process will change with ODD. Various data sources and data catalogs will exchange data in a unified format through a single ODD Adapter. 

The diagrams are inspired by the [OpenLineage](https://github.com/OpenLineage/OpenLineage) documentation. 


<p align="center">
<img src="./images/open-data-discovery-reference-catalog-implementation.jpg" width="600px" alt="open-data-discovery-reference-catalog-implementation"/>&nbsp;
</p>

**Diagram 2** shows Open Data Discovery process with pull, push, and federation strategies. 
Any data source including Data Catalog can expose ODD Adapter API or have a specific adapter microservice to be discovered. It may also use a push strategy to be combined with already discovered data entities. ODD Data catalogs intentionally do not have access to the real data and operate only consumed metadata.

 
 #Engagement Benefits

There are 3 main groups of Clients & Partners of ODD: 

<ul>
<li><b>Data Catalogs</b> - DataHub, Amundsen, Collibra, Alation, etc.) </li>
<li><b>Data Assets</b> - sources/consumers (ETL Tools, warehouses, BI, feature stores, ML pipelines, data quality tools, etc.)</li> 
<li><b>End Users</b> (enterprises: their data teams, engineers, product maangers, analysts, etc.)</li> 
</ul>

Each of the groups can benefit greatly from engagement with and early adoption of ODD.

## Data Catalogs

**Goal**: wider adoption & market integration, better product for users, market development.


<ul>
<li>Faster time-to-value</li>
<li>Better integration with the Data Discovery ecosystem</li> 
<li>Improvement of data discovery experience for users</li> 
<li>Covering more use cases for the community</li>
<li>Onboarding more renowned companies</li>
<li>Acceleration of the whole ecosystem</li>
</ul>
  
 
## Data Sources

**Goal**: wider adoption & market integration, better product for users, more & better clients, market development. 

<ul>
<li>Better integration with the data discovery ecosystem</li>
<li>Faster adoption and recognition on the market</li> 
<li>Opportunity to onboard more and better clients</li> 
</ul>
 

## End Users

**Goal**: fast finding & evaluation of trusted data, producing better end products with faster TTM, effective metadata exchange between teams & departments 

<ul>
<li>Better quality & speed of the data discovery and access</li>
<li>Fast integration of metadata from various business units</li> 
<li>Ability to quickly find, evaluate and trust data</li> 
<li>Federated solution to bring together all business units</li> 
<li>Data observability, quality, health tracking</li> 
<li>Real end-to-end lineage</li> 
<li>Multi-cloud solution</li> 
</ul>

 
# Scope

## ODD Scope

ODD describes the process of gathering metadata from data storages/sources such as data lakes and data warehouses, data discovery processes through push and pull models and APIs that should be provided.  

## Out of ODD Scope

ODD does not describe Data Catalog and how it works: its authentication and authorization, how it provides access to data, etc.

# Discovery Models

## Push and Pull Models

The metadata discovery process is very similar to that of gathering metrics/logs/traces. It can be done through a pull or push model (or both). Each of the models has a range of use cases it suits best. ODD uses both models to effectively cover all core use cases.  

### Pull Model

Pulling metadata directly from the source is the most straightforward way of gathering it. However, an attempt to develop and maintain a centralized fleet of domain-specific crawlers can easily become a nightmare. Pulling data from multiple sources without having a standard for it means writing multiple source-specific crawlers for each adapter, which would be an overly complex and ineffective solution. ODD solves this issue by providing a universal API adapter (ODD Adapter). 

#### ODD Adapter

The ODD Adapter entity introduced by ODD is a lightweight service behind a data warehouse. It is a proxy layer for data that allows gathering metadata in a standardized format. ODD Adapter receives requests for data entities and returns those entities. ODD Adapters are designed to be source-specific and expose only the information that could be gathered from a particular data source.


<p align="center">
<img src="./images/open-data-discovery-pull-strategy-odd.jpg" width="600px" alt="open-data-discovery-pull-strategy-odd"/>&nbsp;
</p>


Pull model is preferred when: 

<ul>
<li>Latency on index update is ok</li>
<li>There is already an adapter</li> 
</ul>

### Push Model

Push model supports the process where individual metadata providers push the information to the central repository via APIs. The model is more preferred for use cases like Airflow job runs and quality check runs.

<p align="center">
<img src="./images/open-data-discovery-push-strategy-odd.jpg" width="600px" alt="open-data-discovery-push-strategy-odd"/>&nbsp;
</p>

## Data Discovery Federation

Federation allows scraping data entities from other Open Data Discovery servers.

### Use Cases

There are many different use cases for federation. Commonly, it is used to either build scalable Data Catalogs or pull related data entities from one ODD server to another.

### Hierarchical Federation

Hierarchical federation allows ODD servers to scale to environments with tens of data centers and millions of nodes. In this use case, the federation topology resembles a tree, with higher-level ODD servers collecting data entities from a larger number of subordinated servers.

For example, a setup might consist of many per-datacenter ODD servers that collect data in high detail (instance-level drill-down), and a set of global ODD servers that collect and store from those local servers. 

<p align="center">
<img src="./images/open-data-discovery-hierarchical-federation.jpg" width="600px" alt="open-data-discovery-hierarchical-federation"/>&nbsp;
</p>

### Cross-Service Federation

In the case of the cross-service federation, an ODD server of one service is configured to scrape selected data from another service's ODD server to enable queries against both datasets within a single server.

<p align="center">
<img src="./images/open-data-discovery-cross-service-federation.jpg" width="600px" alt="open-data-discovery-cross-service-federation"/>&nbsp;
</p>

# Data Model Specification

The goal of ODD is to provide a standard protocol on how metadata can be collected and correlated in the most automated way possible.

To enable many different data sources and tools to expose the metadata we need agreement on what data should be exposed and in what format (structures). 

The high-level entity of ODD is **DataEntity**.
It could be any of these entities:

<ol>
<li><b>DataInput</b> (sources of data)</li>
<li><b>DataSet</b> (collections of data)</li> 
<li><b>DataTransformer</b> (transformers of data: ETL or ML training jobs)</li> 
<li><b>DataTransformerRun</b> execution of: ETL or ML training jobs)</li> 
<li><b>DataConsumers</b> (consumers of data: ML model artifacts or BI dashboards)</li> 
<li><b>DataQualityTest</b> (describe tests for particular DataSets)</li>
<li><b>DataQualityTestRun</b> (execution of quality test)</li>
</ol>

 
Each entity has: 

<ul>
<li><b>ODDRN</b> (Open Data Discovery Resource Name) - a unique URL describing its place, system, and identifyer in this system</li>
<li>A human-friendly name</li> 
<li>List of metadata extension objects</li> 
</ul>

ODD Data Entity: 

```yaml
DataEntity:
     type: object
     properties:
       oddrn:
         type: string
         example: "//aws/glue/{account_id}/{database}/{tablename}"
       name:
         type: string
         example:
       owner:
         type: string
         example: "//aws/iam/{account_id}/user/name"
       metadata:
         type: array
         items:
           $ref: "#/components/schemas/MetadataExtension"
       dataset:
         $ref: '#/components/schemas/DataSet'
       data_transformer:
         $ref: '#/components/schemas/DataTransformer'
       data_transformer_run:
         $ref: '#/components/schemas/DataTransformerRun'
       data_quality_test:
         $ref: '#/components/schemas/DataQualityTest'
       data_quality_test_run:
         $ref: '#/components/schemas/DataQualityTestRun'
       data_input:
         $ref: '#/components/schemas/DataInput'
       data_consumer:
         $ref: '#/components/schemas/DataConsumer'
```  

ODD Metadata Extension:

```yaml
MetadataExtension:
     type: object
     properties:
       schema_url:
         description: "The JSON Pointer (https://tools.ietf.org/html/rfc6901) URL to the corresponding version of the schema definition for this extension"
         example: https://raw.githubusercontent.com/opendatadiscovery/opendatadiscovery-specification/main/specification/extensions/glue.json#/definitions/GlueDataSetExtension
         type: string
         format: uri
       metadata:
         type: object
         additionalProperties: true
     required:
       - schema_url
       - metadata
```  
## Data Inputs

**DataInputs** are sources of your data. They can be website URLs, external S3 bucket, or real-life data places.

```yaml
DataInput:
    properties:
        owner:
            example: //aws/iam/{account_id}/user/name
            type: string
        description:
            type: string
    required:
        - description
```  

Example:

```yaml
{
    "oddrn": "//http/www.amazon.com/goods",
    "name": "Amazon Goods Website",
    "metadata": [
        {
          “schema_url”: null,
          “metadata”: {
             "location": "internet"
          }
        }        
    ],
    “data_input”: {
      "owner": "Amazon",
      "description": "Amazon Goods website with api"
    }
}
```  

## DataSets

A **DataSet** is a collection of data stored in a structured, semi-structured, or unstructured format. It might be a table in a relational database, a parquet file on an S3 bucket, a Hive catalog table, and so on.

DataSets can have sub-datasets. For example, the Hive table is a dataset itself and it consists of DataSets in the format of folders/files on HDFS/S3.

ODD Dataset: 

```yaml
DataSet:
 properties:
   parentOddrn:
     type: string
   description:
     type: string
   updatedAt:
     type: string
     format: date-time
   subtype:
     type: string
     enum:
       - DATASET_TABLE
       - DATASET_FILE
       - DATASET_FEATURE_GROUP
       - DATASET_TOPIC
   fieldList:
     type: array
     items:
       $ref: '#/components/schemas/DataSetField'
 required:
   - description
   - subtype
   - fieldList


DataSetField:
 type: object
 properties:
   parentFieldOddrn:
     type: string
   type:
     $ref: '#/components/schemas/DataSetFieldType'
   isKey:
     type: boolean
   isValue:
     type: boolean           
   defaultValue:
     type: string
   description:
     type: string
  stats:
     $ref: '#/components/schemas/DataSetFieldStat'
 required:
   - name
   - type

DataSetFieldType:
 type: object
 properties:
   type:
     type: string
     enum:
       - TYPE_STRING
       - TYPE_NUMBER
       - TYPE_INTEGER
       - TYPE_BOOLEAN
       - TYPE_DATETIME
       - TYPE_STRUCT
       - TYPE_BINARY
       - TYPE_LIST
       - TYPE_MAP
   logicalType:
     type: string
   isNullable:
     type: boolean
 required:
   - type
   - isNullable
```  

### Tables

Example ODDRN:


```yaml
{
    "oddrn": "//postgresql/pg.sandbox.datacompany.domain/goods/public/items",
    "name": "public.items",
    "owner": "root",
    "metadata": {
        "location": "internet",        
    },
    "parentOddrn": null,    
    "description": "Amazon Goods table",
    "updatedAt": "2021-02-11T00:01:00Z",
    "subtype": "DATASET_TABLE",
    "fieldList": [
        {
           "oddrn": "//postgresql/pg.sandbox.datacompany.domain/goods/public/items/id",
           "name": "id",
           "owner": "root",
           "metadata": {},
           "parentFieldOddrn": null,
           "type": "TYPE_NUMBER",
           "isKey": false,
           "isValue": false,
           "defaultValue": null,
           "description": "Unique identifier field",
           "stats": {
               "numberStats": {
                   "lowValue": 1,
                   "highValue": 10000,
                   "meanValue": 5000,
                   "medianValue": 5000,
                   "nullsCount": 0,
                   "uniqueCount": 10000
               }
           }
        },
        {
           "oddrn": "//postgresql/pg.sandbox.datacompany.domain/goods/public/items/name",
           "name": "name",
           "owner": "root",
           "metadata": {},
           "parentFieldOddrn": null,
           "type": "TYPE_STRING",
           "isKey": false,
           "isValue": false,
           "defaultValue": null,
           "description": "Goods name",
           "stats": {
               "stringStats": {
                   "maxLength": 120,
                   "avgLength": 52,
                   "nullsCount": 0,
                   "uniqueCount": 10000
               }
           }
        }      
    ]
}
```  

### Files

Example ODDRN: 


```yaml
{
    "oddrn": "//aws/s3/sample.data/path/to/folder/file.csv",
    "name": "file.csv",
    "owner": "aws:iam:88898998/username",
    "metadata": {
        "location": "internet",        
    },
    "parentOddrn": null,    
    "description": "Amazon Goods table",
    "updatedAt": "2021-02-11T00:01:00Z",
    "subtype": "DATASET_TABLE",
    "fieldList": [
        {
           "oddrn": "//aws/s3/sample.data/path/to/folder/file.csv/id",
           "name": "id",
           "owner": "aws:iam:88898998/username",
           "metadata": {},
           "parentFieldOddrn": null,
           "type": "TYPE_NUMBER",
           "isKey": false,
           "isValue": false,
           "defaultValue": null,
           "description": "Unique identifier field",
           "stats": {
               "numberStats": {
                   "lowValue": 1,
                   "highValue": 10000,
                   "meanValue": 5000,
                   "medianValue": 5000,
                   "nullsCount": 0,
                   "uniqueCount": 10000
               }
           }
        },
        {
           "oddrn": "//aws/s3/sample.data/path/to/folder/file.csv/name",
           "name": "name",
           "owner": "aws:iam:88898998/username",
           "metadata": {},
           "parentFieldOddrn": null,
           "type": "TYPE_STRING",
           "isKey": false,
           "isValue": false,
           "defaultValue": null,
           "description": "Goods name",
           "stats": {
               "stringStats": {
                   "maxLength": 120,
                   "avgLength": 52,
                   "nullsCount": 0,
                   "uniqueCount": 10000
               }
           }
        }      
    ]
}
```  
### Feature Groups

Feature Groups are entities provided by Feature Stores. They are similar to a table in a database but can expose additional information. 

Example ODDRN: 

``` 
//feast/host/{namespace}/{featuregroup}
```  

## DataTransformers

Data transformers are any entities that can consume data and produce any other object. For example ETL job, ML Experiment, ML Training.


```yaml
DataTransformer:
 type: object
 properties:
   description:
       type: string
   sourceCodeUrl:
       type: string
   sql:
       type: string                       
   inputs:
       type: array
       items:
       type: string           
   outputs:
       type: array
       items:
       type: string
   subtype:
       type: string
       enum:
       - DATATRANSFORMER_JOB
       - DATATRANSFORMER_EXPERIMENT
       - DATATRANSFORMER_ML_MODEL_TRAINING
       - DATATRANSFORMER_ML_MODEL_INSTANCE
 required:
 - description
 - inputs
 - outputs
 - subtype

DataTransformerRun:
properties:
  transformerOddrn:
    type: string
  startTime:
    type: string
    format: date-time
  endTime:      
    type: string
    format: date-time
  statusReason:
    type: string
  status:
    type: string
    enum:
      - SUCCESS
      - FAIL
      - ABORTED
      - OTHER
required:
  - transformerOddrn
  - startTime
  - endTime
  - status

```  

### ETL Jobs


Example ODDRN: 

``` 
//airflow/{host}/{path}/{dag_id}/{job_id} 
```  

### ML Training Jobs

Example ODDRN: 

``` 
//kubeflow/{host}/{path}/{job_id}
```  

## DataConsumers

Any data entity built with one or many datasets, for example Dashboards, ML Models.

```yaml
DataConsumer:
 type: object
 properties:
   description:
     type: string
   inputs:
     type: array
     items:
       type: string
   subtype:
     type: string
     enum:
       - DATACONSUMER_DASHBOARD
       - DATACONSUMER_ML_MODEL_ARTIFACT              
 required:
   - description
   - subtype
```  

### ML Models

Example ODDRN: 

``` 
//aws/sagemaker/{account_id}/{model_id}
```  

### BI Dashboards

Example ODDRN: 

``` 
//tableau/{host}/{path}/{dashboard_id}
```  

## DataQualityTests

Data Quality Tests are assertions for data. They are the workhorse abstractions covering all kinds of common data issues. Each dataset could be linked to a test suite (like Jira ticket, Confluence page, or any other URL), which should be linked to one or many datasets. **DataQualityTestRun** describes test run status.

```yaml
DataQualityTest:
        type: object
        properties:
            name:
                type: string
            suite_name:
                type: string              
            suite_url:
                type: string
            dataset_list:
                type: array
                items:
                    type: string
            expectation:
                type: object
            linkedUrlList:
                type: array
                items:
                    $ref: '#/components/schemas/LinkedUrl'
        required:
            - description
            - datasetList

    DataQualityTestRun:  
        type: object
        properties:
            dataQualityTestOddrn:
              type: string
            startTime:
              type: string
              format: date-time
            endTime:        
              type: string
              format: date-time
            statusReason:
              type: string
            description:
              type: string
            status:
              type: string
              enum:
                - SUCCESS
                - FAIL
                - ABORTED
                - OTHER
        required:
            - dataQualityTestOddrn
            - startTime
            - endTime
            - status
```  

# Glossary


<b>Data Discovery</b> - the first step of working with data - finding the right data and evaluating it. 

<b>Open Data Discovery (ODD) Spec</b>  - a specification for the data discovery process. 

<b>Open Data Discovery (ODD) Catalog</b>  - a reference implementation of the ODD Standard built upon it.  

<b>ODD Adapter API<</b>  - an open API specification of the ODD Adapter to provide data to the ODD Puller.

<b>ODD Adapter</b> - a microservice that implements the ODD Adapter API and provides data source specific entities.

<b>ODD Ingestion API</b>  -an open API specification for push strategy ingestion.

<b>ODD Puller</b> - a service that regularly pulls metadata from ODD Adapters. 

<b>ODDRN</b>  - Open Data Discovery Resource Name (the unique identifier of the data resource).

<b>ETL tools</b>  - Extract, Transform, Load. These tools play a key role in data integration strategies allowing businesses to gather data from multiple sources and consolidate it into a single centralized location and make different types of data work together. ETLs collect and refine different types of data and deliver it to data warehouses or help to migrate it between different sources. 

# RFC Status

## Proposers

| Name            | GithHub                                     | 
|-----------------|---------------------------------------------|
|Stepan Pushkarev | [spushkarev](https://github.com/spushkarev) |
|German Osin      | [germanosin](https://github.com/germanosin) |
|Elena Goydina    | [Evanto](https://github.com/Evanto)         |
|Nikita Dementyev | [DementevNikita](https://github.com/DementevNikita) |
|Sofia Shnidman   | [soffest](https://github.com/soffest) |


## Commenters

Please feel free to comment and add yourself as a commenter in the table below. 

| Name | GithHub | 
|------|---------|
|      |         | 
|      |         | 

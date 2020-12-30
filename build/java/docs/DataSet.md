

# DataSet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oddrn** | **String** |  | 
**name** | **String** |  | 
**owner** | **String** |  | 
**metadata** | **Map&lt;String, String&gt;** |  |  [optional]
**parentOddrn** | **String** |  |  [optional]
**description** | **String** |  | 
**updatedAt** | **OffsetDateTime** |  |  [optional]
**subtype** | [**SubtypeEnum**](#SubtypeEnum) |  |  [optional]
**fieldList** | [**List&lt;DataSetField&gt;**](DataSetField.md) |  |  [optional]
**dataSetList** | [**List&lt;DataSet&gt;**](DataSet.md) |  |  [optional]



## Enum: SubtypeEnum

Name | Value
---- | -----
TABLE | &quot;DATASET_TABLE&quot;
FILE | &quot;DATASET_FILE&quot;
FEATURE_GROUP | &quot;DATASET_FEATURE_GROUP&quot;






# DataTransformerRun

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oddrn** | **String** |  | 
**name** | **String** |  | 
**owner** | **String** |  | 
**metadata** | **Map&lt;String, String&gt;** |  |  [optional]
**transformerOddrn** | **String** |  |  [optional]
**startTime** | **OffsetDateTime** |  |  [optional]
**endTime** | **OffsetDateTime** |  |  [optional]
**statusReason** | **String** |  |  [optional]
**status** | [**StatusEnum**](#StatusEnum) |  |  [optional]



## Enum: StatusEnum

Name | Value
---- | -----
SUCCESS | &quot;SUCCESS&quot;
FAIL | &quot;FAIL&quot;
ABORTED | &quot;ABORTED&quot;
OTHER | &quot;OTHER&quot;




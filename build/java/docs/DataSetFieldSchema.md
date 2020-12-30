

# DataSetFieldSchema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**TypeEnum**](#TypeEnum) |  | 
**logicalType** | **String** |  |  [optional]
**isNullable** | **Boolean** |  | 
**key** | [**DataSetFieldType**](DataSetFieldType.md) |  |  [optional]
**value** | [**DataSetFieldType**](DataSetFieldType.md) |  |  [optional]
**fieldList** | [**List&lt;DataSetField&gt;**](DataSetField.md) |  |  [optional]



## Enum: TypeEnum

Name | Value
---- | -----
STRING | &quot;TYPE_STRING&quot;
NUMBER | &quot;TYPE_NUMBER&quot;
INTEGER | &quot;TYPE_INTEGER&quot;
BOOLEAN | &quot;TYPE_BOOLEAN&quot;
DATETIME | &quot;TYPE_DATETIME&quot;
STRUCT | &quot;TYPE_STRUCT&quot;
BINARY | &quot;TYPE_BINARY&quot;
LIST | &quot;TYPE_LIST&quot;
MAP | &quot;TYPE_MAP&quot;




# OpenDataDiscoveryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDataConsumerList**](OpenDataDiscoveryApi.md#getDataConsumerList) | **POST** /ingesion/{datasourceOddrn}/consumers | 
[**getDataInputList**](OpenDataDiscoveryApi.md#getDataInputList) | **POST** /ingesion/{datasourceOddrn}/inputs | 
[**getDataQualityTestList**](OpenDataDiscoveryApi.md#getDataQualityTestList) | **POST** /ingesion/{datasourceOddrn}/qualitytests | 
[**getDataQualityTestRunList**](OpenDataDiscoveryApi.md#getDataQualityTestRunList) | **POST** /ingesion/{datasourceOddrn}/qualitytests/runs | 
[**getDataSetList**](OpenDataDiscoveryApi.md#getDataSetList) | **POST** /ingesion/{datasourceOddrn}/datasets | 
[**getDataTransformerList**](OpenDataDiscoveryApi.md#getDataTransformerList) | **POST** /ingesion/{datasourceOddrn}/transformers | 
[**getDataTransformerRunList**](OpenDataDiscoveryApi.md#getDataTransformerRunList) | **POST** /ingesion/{datasourceOddrn}/transformers/runs | 


<a name="getDataConsumerList"></a>
# **getDataConsumerList**
> getDataConsumerList(datasourceOddrn, dataConsumer)



Provides list of available consumers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OpenDataDiscoveryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    OpenDataDiscoveryApi apiInstance = new OpenDataDiscoveryApi(defaultClient);
    String datasourceOddrn = "datasourceOddrn_example"; // String | 
    List<DataConsumer> dataConsumer = Arrays.asList(null); // List<DataConsumer> | 
    try {
      apiInstance.getDataConsumerList(datasourceOddrn, dataConsumer);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpenDataDiscoveryApi#getDataConsumerList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasourceOddrn** | **String**|  |
 **dataConsumer** | [**List&lt;DataConsumer&gt;**](DataConsumer.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

<a name="getDataInputList"></a>
# **getDataInputList**
> getDataInputList(datasourceOddrn, dataInput)



Provides list of available inputs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OpenDataDiscoveryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    OpenDataDiscoveryApi apiInstance = new OpenDataDiscoveryApi(defaultClient);
    String datasourceOddrn = "datasourceOddrn_example"; // String | 
    List<DataInput> dataInput = Arrays.asList(null); // List<DataInput> | 
    try {
      apiInstance.getDataInputList(datasourceOddrn, dataInput);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpenDataDiscoveryApi#getDataInputList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasourceOddrn** | **String**|  |
 **dataInput** | [**List&lt;DataInput&gt;**](DataInput.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

<a name="getDataQualityTestList"></a>
# **getDataQualityTestList**
> getDataQualityTestList(datasourceOddrn, dataQualityTest)



Provides list of available data quality tests

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OpenDataDiscoveryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    OpenDataDiscoveryApi apiInstance = new OpenDataDiscoveryApi(defaultClient);
    String datasourceOddrn = "datasourceOddrn_example"; // String | 
    List<DataQualityTest> dataQualityTest = Arrays.asList(null); // List<DataQualityTest> | 
    try {
      apiInstance.getDataQualityTestList(datasourceOddrn, dataQualityTest);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpenDataDiscoveryApi#getDataQualityTestList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasourceOddrn** | **String**|  |
 **dataQualityTest** | [**List&lt;DataQualityTest&gt;**](DataQualityTest.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

<a name="getDataQualityTestRunList"></a>
# **getDataQualityTestRunList**
> getDataQualityTestRunList(datasourceOddrn, dataQualityTestRun)



Provides list of available data quality tests runs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OpenDataDiscoveryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    OpenDataDiscoveryApi apiInstance = new OpenDataDiscoveryApi(defaultClient);
    String datasourceOddrn = "datasourceOddrn_example"; // String | 
    List<DataQualityTestRun> dataQualityTestRun = Arrays.asList(null); // List<DataQualityTestRun> | 
    try {
      apiInstance.getDataQualityTestRunList(datasourceOddrn, dataQualityTestRun);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpenDataDiscoveryApi#getDataQualityTestRunList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasourceOddrn** | **String**|  |
 **dataQualityTestRun** | [**List&lt;DataQualityTestRun&gt;**](DataQualityTestRun.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

<a name="getDataSetList"></a>
# **getDataSetList**
> getDataSetList(datasourceOddrn, dataSet)



Provides list of available datasets

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OpenDataDiscoveryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    OpenDataDiscoveryApi apiInstance = new OpenDataDiscoveryApi(defaultClient);
    String datasourceOddrn = "datasourceOddrn_example"; // String | 
    List<DataSet> dataSet = Arrays.asList(null); // List<DataSet> | 
    try {
      apiInstance.getDataSetList(datasourceOddrn, dataSet);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpenDataDiscoveryApi#getDataSetList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasourceOddrn** | **String**|  |
 **dataSet** | [**List&lt;DataSet&gt;**](DataSet.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

<a name="getDataTransformerList"></a>
# **getDataTransformerList**
> getDataTransformerList(datasourceOddrn, dataTransformer)



Provides list of available transformers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OpenDataDiscoveryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    OpenDataDiscoveryApi apiInstance = new OpenDataDiscoveryApi(defaultClient);
    String datasourceOddrn = "datasourceOddrn_example"; // String | 
    List<DataTransformer> dataTransformer = Arrays.asList(null); // List<DataTransformer> | 
    try {
      apiInstance.getDataTransformerList(datasourceOddrn, dataTransformer);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpenDataDiscoveryApi#getDataTransformerList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasourceOddrn** | **String**|  |
 **dataTransformer** | [**List&lt;DataTransformer&gt;**](DataTransformer.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

<a name="getDataTransformerRunList"></a>
# **getDataTransformerRunList**
> getDataTransformerRunList(datasourceOddrn, dataTransformerRun)



Provides list of runs for all transformers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OpenDataDiscoveryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    OpenDataDiscoveryApi apiInstance = new OpenDataDiscoveryApi(defaultClient);
    String datasourceOddrn = "datasourceOddrn_example"; // String | 
    List<DataTransformerRun> dataTransformerRun = Arrays.asList(null); // List<DataTransformerRun> | 
    try {
      apiInstance.getDataTransformerRunList(datasourceOddrn, dataTransformerRun);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpenDataDiscoveryApi#getDataTransformerRunList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasourceOddrn** | **String**|  |
 **dataTransformerRun** | [**List&lt;DataTransformerRun&gt;**](DataTransformerRun.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |


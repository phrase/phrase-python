# phrase_api.QualityPerformanceScoreApi

All URIs are relative to *https://api.phrase.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projects_quality_performance_score**](QualityPerformanceScoreApi.md#projects_quality_performance_score) | **POST** /projects/{id}/quality_performance_score | Get project&#39;s translations&#39; quality performance scores


# **projects_quality_performance_score**
> ProjectsQualityPerformanceScore200Response projects_quality_performance_score(id, projects_quality_performance_score_request, x_phrase_app_otp=x_phrase_app_otp)

Get project's translations' quality performance scores

Get project's translations' quality performance scores

### Example

```python
from __future__ import print_function
import time
import phrase_api
from phrase_api.rest import ApiException
from pprint import pprint

configuration = phrase_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'token'

# Enter a context with an instance of the API client
with phrase_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = phrase_api.QualityPerformanceScoreApi(api_client)
    id = 'id_example' # str | ID (required)
    projects_quality_performance_score_request = phrase_api.ProjectsQualityPerformanceScoreRequest() # ProjectsQualityPerformanceScoreRequest |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Get project's translations' quality performance scores
        api_response = api_instance.projects_quality_performance_score(id, projects_quality_performance_score_request, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling QualityPerformanceScoreApi->projects_quality_performance_score: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID | 
 **projects_quality_performance_score_request** | [**ProjectsQualityPerformanceScoreRequest**](ProjectsQualityPerformanceScoreRequest.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**ProjectsQualityPerformanceScore200Response**](ProjectsQualityPerformanceScore200Response.md)

### Authorization

[Basic](../README.md#Basic), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**400** | Bad request |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**404** | Not Found |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**422** | Unprocessable entity |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**429** | Rate Limiting |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


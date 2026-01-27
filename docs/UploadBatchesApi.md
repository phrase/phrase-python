# phrase_api.UploadBatchesApi

All URIs are relative to *https://api.phrase.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**upload_batches_create**](UploadBatchesApi.md#upload_batches_create) | **POST** /projects/{project_id}/upload_batches | Create upload batch


# **upload_batches_create**
> UploadBatch upload_batches_create(project_id, upload_batches_create_parameters, x_phrase_app_otp=x_phrase_app_otp)

Create upload batch

Groups multiple file uploads into a single batch. Optionally, launches the deletion of unmentioned translation keys after all uploads in the batch are completed. 

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
    api_instance = phrase_api.UploadBatchesApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    upload_batches_create_parameters = phrase_api.UploadBatchesCreateParameters() # UploadBatchesCreateParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Create upload batch
        api_response = api_instance.upload_batches_create(project_id, upload_batches_create_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UploadBatchesApi->upload_batches_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **upload_batches_create_parameters** | [**UploadBatchesCreateParameters**](UploadBatchesCreateParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**UploadBatch**](UploadBatch.md)

### Authorization

[Basic](../README.md#Basic), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**400** | Bad request |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**404** | Not Found |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**429** | Rate Limiting |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


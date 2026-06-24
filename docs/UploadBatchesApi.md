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
**400** | Bad request. The request could not be parsed or a parameter failed validation. Verify the request body, the content type, and the parameter types, then retry. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**401** | Unauthorized. Authentication failed because the access token is missing, expired, or invalid. Supply a valid access token and retry. |  -  |
**403** | Forbidden. The credentials are valid but not permitted for this request: the access token may lack the required scope, the user may lack permission on the resource, or the account plan may not include the feature. Use a token with the required scope on an account and user that hold the necessary permissions. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**404** | Not found. The requested resource does not exist or is not visible to the authenticated user. Verify the identifiers in the request path and that the token has access to them, then retry. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**422** | Unprocessable entity. The request was well-formed but failed validation. The response body lists each offending field in the &#x60;errors&#x60; array, with its resource, field, and a human-readable message. Correct the listed fields and retry. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**429** | Too many requests. The rate limit has been exceeded. Wait until the time indicated by the &#x60;X-Rate-Limit-Reset&#x60; response header before retrying. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# phrase_api.FormatsApi

All URIs are relative to *https://api.phrase.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**formats_list**](FormatsApi.md#formats_list) | **GET** /formats | List formats


# **formats_list**
> List[Format] formats_list()

List formats

Returns all file formats that Phrase Strings supports. Use the api_name value from each format as the file_format parameter when uploading or downloading locale files. Not every format supports both directions: check the importable and exportable fields before using a format in a workflow. This endpoint does not require authentication and is not subject to rate limiting. 

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
    api_instance = phrase_api.FormatsApi(api_client)

    try:
        # List formats
        api_response = api_instance.formats_list()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FormatsApi->formats_list: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**List[Format]**](Format.md)

### Authorization

[Basic](../README.md#Basic), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**400** | Bad request. The request could not be parsed or a parameter failed validation. Verify the request body, the content type, and the parameter types, then retry. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


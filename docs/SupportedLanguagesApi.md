# phrase_api.SupportedLanguagesApi

All URIs are relative to *https://api.phrase.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**languages_list**](SupportedLanguagesApi.md#languages_list) | **GET** /languages | List supported languages


# **languages_list**
> Dict[str, str] languages_list()

List supported languages

Returns all languages/locale codes that Phrase Strings recognizes, mapped to their human-readable display name. This endpoint does not require authentication. 

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
    api_instance = phrase_api.SupportedLanguagesApi(api_client)

    try:
        # List supported languages
        api_response = api_instance.languages_list()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SupportedLanguagesApi->languages_list: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**Dict[str, str]**

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


# phrase_api.SearchApi

All URIs are relative to *https://api.phrase.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_in_account**](SearchApi.md#search_in_account) | **POST** /accounts/{account_id}/search | Search across projects


# **search_in_account**
> AccountSearchResult search_in_account(account_id, search_in_account_parameters, x_phrase_app_otp=x_phrase_app_otp)

Search across projects

Search for keys and translations in all account projects  *Note: Search is limited to 10000 results and may not include recently updated data depending on the project sizes.* 

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
    api_instance = phrase_api.SearchApi(api_client)
    account_id = 'account_id_example' # str | Account ID (required)
    search_in_account_parameters = phrase_api.SearchInAccountParameters() # SearchInAccountParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Search across projects
        api_response = api_instance.search_in_account(account_id, search_in_account_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SearchApi->search_in_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID | 
 **search_in_account_parameters** | [**SearchInAccountParameters**](SearchInAccountParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**AccountSearchResult**](AccountSearchResult.md)

### Authorization

[Basic](../README.md#Basic), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  * Pagination -  <br>  |
**400** | Bad request. The request could not be parsed or a parameter failed validation. Verify the request body, the content type, and the parameter types, then retry. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**401** | Unauthorized. Authentication failed because the access token is missing, expired, or invalid. Supply a valid access token and retry. |  -  |
**403** | Forbidden. The credentials are valid but not permitted for this request: the access token may lack the required scope, the user may lack permission on the resource, or the account plan may not include the feature. Use a token with the required scope on an account and user that hold the necessary permissions. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**404** | Not found. The requested resource does not exist or is not visible to the authenticated user. Verify the identifiers in the request path and that the token has access to them, then retry. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**429** | Too many requests. The rate limit has been exceeded. Wait until the time indicated by the &#x60;X-Rate-Limit-Reset&#x60; response header before retrying. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


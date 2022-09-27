# phrase_api.BitbucketSyncApi

All URIs are relative to *https://api.phrase.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bitbucket_sync_export**](BitbucketSyncApi.md#bitbucket_sync_export) | **POST** /bitbucket_syncs/{id}/export | Export from Phrase Strings to Bitbucket
[**bitbucket_sync_import**](BitbucketSyncApi.md#bitbucket_sync_import) | **POST** /bitbucket_syncs/{id}/import | Import to Phrase Strings from Bitbucket
[**bitbucket_syncs_list**](BitbucketSyncApi.md#bitbucket_syncs_list) | **GET** /bitbucket_syncs | List Bitbucket syncs


# **bitbucket_sync_export**
> BitbucketSyncExportResponse bitbucket_sync_export(id, bitbucket_sync_export_parameters, x_phrase_app_otp=x_phrase_app_otp)

Export from Phrase Strings to Bitbucket

Export translations from Phrase Strings to Bitbucket according to the .phraseapp.yml file within the Bitbucket Repository.

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
    api_instance = phrase_api.BitbucketSyncApi(api_client)
    id = 'id_example' # str | ID (required)
    bitbucket_sync_export_parameters = phrase_api.BitbucketSyncExportParameters() # BitbucketSyncExportParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Export from Phrase Strings to Bitbucket
        api_response = api_instance.bitbucket_sync_export(id, bitbucket_sync_export_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BitbucketSyncApi->bitbucket_sync_export: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID | 
 **bitbucket_sync_export_parameters** | [**BitbucketSyncExportParameters**](BitbucketSyncExportParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**BitbucketSyncExportResponse**](BitbucketSyncExportResponse.md)

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
**404** | Not Found |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**429** | Rate Limiting |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bitbucket_sync_import**
> bitbucket_sync_import(id, bitbucket_sync_import_parameters, x_phrase_app_otp=x_phrase_app_otp)

Import to Phrase Strings from Bitbucket

Import translations from Bitbucket to Phrase Strings according to the .phraseapp.yml file within the Bitbucket repository.

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
    api_instance = phrase_api.BitbucketSyncApi(api_client)
    id = 'id_example' # str | ID (required)
    bitbucket_sync_import_parameters = phrase_api.BitbucketSyncImportParameters() # BitbucketSyncImportParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Import to Phrase Strings from Bitbucket
        api_instance.bitbucket_sync_import(id, bitbucket_sync_import_parameters, x_phrase_app_otp=x_phrase_app_otp)
    except ApiException as e:
        print("Exception when calling BitbucketSyncApi->bitbucket_sync_import: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID | 
 **bitbucket_sync_import_parameters** | [**BitbucketSyncImportParameters**](BitbucketSyncImportParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**400** | Bad request |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**404** | Not Found |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**429** | Rate Limiting |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bitbucket_syncs_list**
> list[BitbucketSync] bitbucket_syncs_list(x_phrase_app_otp=x_phrase_app_otp, account_id=account_id)

List Bitbucket syncs

List all Bitbucket repositories for which synchronisation with Phrase Strings is activated.

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
    api_instance = phrase_api.BitbucketSyncApi(api_client)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    account_id = 'abcd1234' # str | Account ID to specify the actual account the project should be created in. Required if the requesting user is a member of multiple accounts.

    try:
        # List Bitbucket syncs
        api_response = api_instance.bitbucket_syncs_list(x_phrase_app_otp=x_phrase_app_otp, account_id=account_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BitbucketSyncApi->bitbucket_syncs_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **account_id** | **str**| Account ID to specify the actual account the project should be created in. Required if the requesting user is a member of multiple accounts. | [optional] 

### Return type

[**list[BitbucketSync]**](BitbucketSync.md)

### Authorization

[Basic](../README.md#Basic), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  * Link -  <br>  |
**400** | Bad request |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**404** | Not Found |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**429** | Rate Limiting |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


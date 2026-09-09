# phrase_api.MachineTranslationApi

All URIs are relative to *https://api.phrase.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**machine_translation_locale_provider_mappings_create**](MachineTranslationApi.md#machine_translation_locale_provider_mappings_create) | **POST** /accounts/{account_id}/machine_translation_locale_provider_mappings | Create a locale provider mapping
[**machine_translation_locale_provider_mappings_destroy**](MachineTranslationApi.md#machine_translation_locale_provider_mappings_destroy) | **DELETE** /accounts/{account_id}/machine_translation_locale_provider_mappings | Delete a locale provider mapping
[**machine_translation_settings_show**](MachineTranslationApi.md#machine_translation_settings_show) | **GET** /accounts/{account_id}/machine_translation_settings | Get machine translation settings
[**machine_translation_settings_update**](MachineTranslationApi.md#machine_translation_settings_update) | **PATCH** /accounts/{account_id}/machine_translation_settings | Update machine translation settings


# **machine_translation_locale_provider_mappings_create**
> MachineTranslationLocaleProviderMapping machine_translation_locale_provider_mappings_create(account_id, machine_translation_locale_provider_mappings_create_parameters, x_phrase_app_otp=x_phrase_app_otp)

Create a locale provider mapping

Creates a locale-pair-specific machine translation provider override for the account. When a mapping exists for a given source/target locale pair, that provider is used instead of the account default. Only one mapping may exist per source/target locale pair; attempting to create a duplicate returns a validation error. The source and target locale codes must differ. 

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
    api_instance = phrase_api.MachineTranslationApi(api_client)
    account_id = 'account_id_example' # str | Account ID (required)
    machine_translation_locale_provider_mappings_create_parameters = phrase_api.MachineTranslationLocaleProviderMappingsCreateParameters() # MachineTranslationLocaleProviderMappingsCreateParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Create a locale provider mapping
        api_response = api_instance.machine_translation_locale_provider_mappings_create(account_id, machine_translation_locale_provider_mappings_create_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MachineTranslationApi->machine_translation_locale_provider_mappings_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID | 
 **machine_translation_locale_provider_mappings_create_parameters** | [**MachineTranslationLocaleProviderMappingsCreateParameters**](MachineTranslationLocaleProviderMappingsCreateParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**MachineTranslationLocaleProviderMapping**](MachineTranslationLocaleProviderMapping.md)

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
**422** | Unprocessable entity. The request was well-formed but failed validation. The response body lists each offending field in the &#x60;errors&#x60; array, with its resource, field, and a human-readable message. Correct the listed fields and retry. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**429** | Too many requests. The rate limit has been exceeded. Wait until the time indicated by the &#x60;X-Rate-Limit-Reset&#x60; response header before retrying. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **machine_translation_locale_provider_mappings_destroy**
> machine_translation_locale_provider_mappings_destroy(account_id, source_locale_code, target_locale_code, x_phrase_app_otp=x_phrase_app_otp)

Delete a locale provider mapping

Removes the machine translation provider override for the specified source and target locale pair. The mapping is identified by locale codes supplied as query parameters rather than a path ID. 

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
    api_instance = phrase_api.MachineTranslationApi(api_client)
    account_id = 'account_id_example' # str | Account ID (required)
    source_locale_code = 'en' # str | The locale code of the source language of the mapping to delete. (required)
    target_locale_code = 'de' # str | The locale code of the target language of the mapping to delete. (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Delete a locale provider mapping
        api_instance.machine_translation_locale_provider_mappings_destroy(account_id, source_locale_code, target_locale_code, x_phrase_app_otp=x_phrase_app_otp)
    except ApiException as e:
        print("Exception when calling MachineTranslationApi->machine_translation_locale_provider_mappings_destroy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID | 
 **source_locale_code** | **str**| The locale code of the source language of the mapping to delete. | 
 **target_locale_code** | **str**| The locale code of the target language of the mapping to delete. | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**400** | Bad request. The request could not be parsed or a parameter failed validation. Verify the request body, the content type, and the parameter types, then retry. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**401** | Unauthorized. Authentication failed because the access token is missing, expired, or invalid. Supply a valid access token and retry. |  -  |
**403** | Forbidden. The credentials are valid but not permitted for this request: the access token may lack the required scope, the user may lack permission on the resource, or the account plan may not include the feature. Use a token with the required scope on an account and user that hold the necessary permissions. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**404** | Not found. The requested resource does not exist or is not visible to the authenticated user. Verify the identifiers in the request path and that the token has access to them, then retry. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**429** | Too many requests. The rate limit has been exceeded. Wait until the time indicated by the &#x60;X-Rate-Limit-Reset&#x60; response header before retrying. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **machine_translation_settings_show**
> MachineTranslationSettings machine_translation_settings_show(account_id, x_phrase_app_otp=x_phrase_app_otp)

Get machine translation settings

Returns the machine translation configuration for the account, including the default translation service, current machine translation unit usage, and any locale-pair-specific provider mappings. 

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
    api_instance = phrase_api.MachineTranslationApi(api_client)
    account_id = 'account_id_example' # str | Account ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Get machine translation settings
        api_response = api_instance.machine_translation_settings_show(account_id, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MachineTranslationApi->machine_translation_settings_show: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**MachineTranslationSettings**](MachineTranslationSettings.md)

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
**401** | Unauthorized. Authentication failed because the access token is missing, expired, or invalid. Supply a valid access token and retry. |  -  |
**403** | Forbidden. The credentials are valid but not permitted for this request: the access token may lack the required scope, the user may lack permission on the resource, or the account plan may not include the feature. Use a token with the required scope on an account and user that hold the necessary permissions. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**429** | Too many requests. The rate limit has been exceeded. Wait until the time indicated by the &#x60;X-Rate-Limit-Reset&#x60; response header before retrying. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **machine_translation_settings_update**
> MachineTranslationSettings machine_translation_settings_update(account_id, machine_translation_settings_update_parameters, x_phrase_app_otp=x_phrase_app_otp)

Update machine translation settings

Sets the default machine translation service for the account. Requires write access to the account's machine translation settings. Passing an empty or absent value for `default_service` resets the account to its plan default (Microsoft Translate). 

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
    api_instance = phrase_api.MachineTranslationApi(api_client)
    account_id = 'account_id_example' # str | Account ID (required)
    machine_translation_settings_update_parameters = phrase_api.MachineTranslationSettingsUpdateParameters() # MachineTranslationSettingsUpdateParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Update machine translation settings
        api_response = api_instance.machine_translation_settings_update(account_id, machine_translation_settings_update_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MachineTranslationApi->machine_translation_settings_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID | 
 **machine_translation_settings_update_parameters** | [**MachineTranslationSettingsUpdateParameters**](MachineTranslationSettingsUpdateParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**MachineTranslationSettings**](MachineTranslationSettings.md)

### Authorization

[Basic](../README.md#Basic), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**400** | Bad request. The request could not be parsed or a parameter failed validation. Verify the request body, the content type, and the parameter types, then retry. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**401** | Unauthorized. Authentication failed because the access token is missing, expired, or invalid. Supply a valid access token and retry. |  -  |
**403** | Forbidden. The credentials are valid but not permitted for this request: the access token may lack the required scope, the user may lack permission on the resource, or the account plan may not include the feature. Use a token with the required scope on an account and user that hold the necessary permissions. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**422** | Unprocessable entity. The request was well-formed but failed validation. The response body lists each offending field in the &#x60;errors&#x60; array, with its resource, field, and a human-readable message. Correct the listed fields and retry. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**429** | Too many requests. The rate limit has been exceeded. Wait until the time indicated by the &#x60;X-Rate-Limit-Reset&#x60; response header before retrying. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


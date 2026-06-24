# phrase_api.GlossaryTermTranslationsApi

All URIs are relative to *https://api.phrase.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**glossary_term_translation_create**](GlossaryTermTranslationsApi.md#glossary_term_translation_create) | **POST** /accounts/{account_id}/glossaries/{glossary_id}/terms/{term_id}/translations | Create a translation for a term
[**glossary_term_translation_delete**](GlossaryTermTranslationsApi.md#glossary_term_translation_delete) | **DELETE** /accounts/{account_id}/glossaries/{glossary_id}/terms/{term_id}/translations/{id} | Delete a translation for a term
[**glossary_term_translation_update**](GlossaryTermTranslationsApi.md#glossary_term_translation_update) | **PATCH** /accounts/{account_id}/glossaries/{glossary_id}/terms/{term_id}/translations/{id} | Update a translation for a term


# **glossary_term_translation_create**
> GlossaryTermTranslation glossary_term_translation_create(account_id, glossary_id, term_id, glossary_term_translation_create_parameters, x_phrase_app_otp=x_phrase_app_otp)

Create a translation for a term

Create a new translation for a term in a term base (previously: glossary).

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
    api_instance = phrase_api.GlossaryTermTranslationsApi(api_client)
    account_id = 'account_id_example' # str | Account ID (required)
    glossary_id = 'glossary_id_example' # str | Glossary ID (required)
    term_id = 'term_id_example' # str | Term ID (required)
    glossary_term_translation_create_parameters = phrase_api.GlossaryTermTranslationCreateParameters() # GlossaryTermTranslationCreateParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Create a translation for a term
        api_response = api_instance.glossary_term_translation_create(account_id, glossary_id, term_id, glossary_term_translation_create_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GlossaryTermTranslationsApi->glossary_term_translation_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID | 
 **glossary_id** | **str**| Glossary ID | 
 **term_id** | **str**| Term ID | 
 **glossary_term_translation_create_parameters** | [**GlossaryTermTranslationCreateParameters**](GlossaryTermTranslationCreateParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**GlossaryTermTranslation**](GlossaryTermTranslation.md)

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

# **glossary_term_translation_delete**
> glossary_term_translation_delete(account_id, glossary_id, term_id, id, x_phrase_app_otp=x_phrase_app_otp)

Delete a translation for a term

Delete an existing translation of a term in a term base (previously: glossary).

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
    api_instance = phrase_api.GlossaryTermTranslationsApi(api_client)
    account_id = 'account_id_example' # str | Account ID (required)
    glossary_id = 'glossary_id_example' # str | Glossary ID (required)
    term_id = 'term_id_example' # str | Term ID (required)
    id = 'id_example' # str | ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Delete a translation for a term
        api_instance.glossary_term_translation_delete(account_id, glossary_id, term_id, id, x_phrase_app_otp=x_phrase_app_otp)
    except ApiException as e:
        print("Exception when calling GlossaryTermTranslationsApi->glossary_term_translation_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID | 
 **glossary_id** | **str**| Glossary ID | 
 **term_id** | **str**| Term ID | 
 **id** | **str**| ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**400** | Bad request. The request could not be parsed or a parameter failed validation. Verify the request body, the content type, and the parameter types, then retry. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**401** | Unauthorized. Authentication failed because the access token is missing, expired, or invalid. Supply a valid access token and retry. |  -  |
**403** | Forbidden. The credentials are valid but not permitted for this request: the access token may lack the required scope, the user may lack permission on the resource, or the account plan may not include the feature. Use a token with the required scope on an account and user that hold the necessary permissions. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**404** | Not found. The requested resource does not exist or is not visible to the authenticated user. Verify the identifiers in the request path and that the token has access to them, then retry. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**422** | Unprocessable entity. The request was well-formed but failed validation. The response body lists each offending field in the &#x60;errors&#x60; array, with its resource, field, and a human-readable message. Correct the listed fields and retry. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**429** | Too many requests. The rate limit has been exceeded. Wait until the time indicated by the &#x60;X-Rate-Limit-Reset&#x60; response header before retrying. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **glossary_term_translation_update**
> GlossaryTermTranslation glossary_term_translation_update(account_id, glossary_id, term_id, id, glossary_term_translation_update_parameters, x_phrase_app_otp=x_phrase_app_otp)

Update a translation for a term

Update an existing translation for a term in a term base (previously: glossary).

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
    api_instance = phrase_api.GlossaryTermTranslationsApi(api_client)
    account_id = 'account_id_example' # str | Account ID (required)
    glossary_id = 'glossary_id_example' # str | Glossary ID (required)
    term_id = 'term_id_example' # str | Term ID (required)
    id = 'id_example' # str | ID (required)
    glossary_term_translation_update_parameters = phrase_api.GlossaryTermTranslationUpdateParameters() # GlossaryTermTranslationUpdateParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Update a translation for a term
        api_response = api_instance.glossary_term_translation_update(account_id, glossary_id, term_id, id, glossary_term_translation_update_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GlossaryTermTranslationsApi->glossary_term_translation_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID | 
 **glossary_id** | **str**| Glossary ID | 
 **term_id** | **str**| Term ID | 
 **id** | **str**| ID | 
 **glossary_term_translation_update_parameters** | [**GlossaryTermTranslationUpdateParameters**](GlossaryTermTranslationUpdateParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**GlossaryTermTranslation**](GlossaryTermTranslation.md)

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
**404** | Not found. The requested resource does not exist or is not visible to the authenticated user. Verify the identifiers in the request path and that the token has access to them, then retry. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**422** | Unprocessable entity. The request was well-formed but failed validation. The response body lists each offending field in the &#x60;errors&#x60; array, with its resource, field, and a human-readable message. Correct the listed fields and retry. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**429** | Too many requests. The rate limit has been exceeded. Wait until the time indicated by the &#x60;X-Rate-Limit-Reset&#x60; response header before retrying. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


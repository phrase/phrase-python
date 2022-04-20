# phrase_api.GlossaryTermsApi

All URIs are relative to *https://api.phrase.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**glossary_term_create**](GlossaryTermsApi.md#glossary_term_create) | **POST** /accounts/{account_id}/glossaries/{glossary_id}/terms | Create a glossary term
[**glossary_term_delete**](GlossaryTermsApi.md#glossary_term_delete) | **DELETE** /accounts/{account_id}/glossaries/{glossary_id}/terms/{id} | Delete a glossary term
[**glossary_term_show**](GlossaryTermsApi.md#glossary_term_show) | **GET** /accounts/{account_id}/glossaries/{glossary_id}/terms/{id} | Get a single glossary term
[**glossary_term_update**](GlossaryTermsApi.md#glossary_term_update) | **PATCH** /accounts/{account_id}/glossaries/{glossary_id}/terms/{id} | Update a glossary term
[**glossary_terms_list**](GlossaryTermsApi.md#glossary_terms_list) | **GET** /accounts/{account_id}/glossaries/{glossary_id}/terms | List glossary terms


# **glossary_term_create**
> GlossaryTerm glossary_term_create(account_id, glossary_id, glossary_term_create_parameters, x_phrase_app_otp=x_phrase_app_otp)

Create a glossary term

Create a new glossary term.

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
    api_instance = phrase_api.GlossaryTermsApi(api_client)
    account_id = 'account_id_example' # str | Account ID (required)
    glossary_id = 'glossary_id_example' # str | Glossary ID (required)
    glossary_term_create_parameters = phrase_api.GlossaryTermCreateParameters() # GlossaryTermCreateParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Create a glossary term
        api_response = api_instance.glossary_term_create(account_id, glossary_id, glossary_term_create_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GlossaryTermsApi->glossary_term_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID | 
 **glossary_id** | **str**| Glossary ID | 
 **glossary_term_create_parameters** | [**GlossaryTermCreateParameters**](GlossaryTermCreateParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**GlossaryTerm**](GlossaryTerm.md)

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

# **glossary_term_delete**
> glossary_term_delete(account_id, glossary_id, id, x_phrase_app_otp=x_phrase_app_otp)

Delete a glossary term

Delete an existing glossary term.

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
    api_instance = phrase_api.GlossaryTermsApi(api_client)
    account_id = 'account_id_example' # str | Account ID (required)
    glossary_id = 'glossary_id_example' # str | Glossary ID (required)
    id = 'id_example' # str | ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Delete a glossary term
        api_instance.glossary_term_delete(account_id, glossary_id, id, x_phrase_app_otp=x_phrase_app_otp)
    except ApiException as e:
        print("Exception when calling GlossaryTermsApi->glossary_term_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID | 
 **glossary_id** | **str**| Glossary ID | 
 **id** | **str**| ID | 
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
**400** | Bad request |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**404** | Not Found |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**429** | Rate Limiting |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **glossary_term_show**
> GlossaryTerm glossary_term_show(account_id, glossary_id, id, x_phrase_app_otp=x_phrase_app_otp)

Get a single glossary term

Get details on a single glossary term.

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
    api_instance = phrase_api.GlossaryTermsApi(api_client)
    account_id = 'account_id_example' # str | Account ID (required)
    glossary_id = 'glossary_id_example' # str | Glossary ID (required)
    id = 'id_example' # str | ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Get a single glossary term
        api_response = api_instance.glossary_term_show(account_id, glossary_id, id, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GlossaryTermsApi->glossary_term_show: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID | 
 **glossary_id** | **str**| Glossary ID | 
 **id** | **str**| ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**GlossaryTerm**](GlossaryTerm.md)

### Authorization

[Basic](../README.md#Basic), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**400** | Bad request |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**404** | Not Found |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**429** | Rate Limiting |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **glossary_term_update**
> GlossaryTerm glossary_term_update(account_id, glossary_id, id, glossary_term_update_parameters, x_phrase_app_otp=x_phrase_app_otp)

Update a glossary term

Update an existing glossary term.

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
    api_instance = phrase_api.GlossaryTermsApi(api_client)
    account_id = 'account_id_example' # str | Account ID (required)
    glossary_id = 'glossary_id_example' # str | Glossary ID (required)
    id = 'id_example' # str | ID (required)
    glossary_term_update_parameters = phrase_api.GlossaryTermUpdateParameters() # GlossaryTermUpdateParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Update a glossary term
        api_response = api_instance.glossary_term_update(account_id, glossary_id, id, glossary_term_update_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GlossaryTermsApi->glossary_term_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID | 
 **glossary_id** | **str**| Glossary ID | 
 **id** | **str**| ID | 
 **glossary_term_update_parameters** | [**GlossaryTermUpdateParameters**](GlossaryTermUpdateParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**GlossaryTerm**](GlossaryTerm.md)

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

# **glossary_terms_list**
> list[GlossaryTerm] glossary_terms_list(account_id, glossary_id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page)

List glossary terms

List all glossary terms the current user has access to.

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
    api_instance = phrase_api.GlossaryTermsApi(api_client)
    account_id = 'account_id_example' # str | Account ID (required)
    glossary_id = 'glossary_id_example' # str | Glossary ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    page = 1 # int | Page number
    per_page = 25 # int | allows you to specify a page size up to 100 items, 25 by default

    try:
        # List glossary terms
        api_response = api_instance.glossary_terms_list(account_id, glossary_id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GlossaryTermsApi->glossary_terms_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID | 
 **glossary_id** | **str**| Glossary ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| allows you to specify a page size up to 100 items, 25 by default | [optional] 

### Return type

[**list[GlossaryTerm]**](GlossaryTerm.md)

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


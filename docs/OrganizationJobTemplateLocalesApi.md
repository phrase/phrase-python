# phrase_api.OrganizationJobTemplateLocalesApi

All URIs are relative to *https://api.phrase.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organization_job_template_locale_delete**](OrganizationJobTemplateLocalesApi.md#organization_job_template_locale_delete) | **DELETE** /accounts/{account_id}/job_templates/{job_template_id}/locales/{job_template_locale_id} | Delete an organization job template locale
[**organization_job_template_locale_show**](OrganizationJobTemplateLocalesApi.md#organization_job_template_locale_show) | **GET** /accounts/{account_id}/job_templates/{job_template_id}/locales/{job_template_locale_id} | Get a single organization job template locale
[**organization_job_template_locale_update**](OrganizationJobTemplateLocalesApi.md#organization_job_template_locale_update) | **PATCH** /accounts/{account_id}/job_templates/{job_template_id}/locales/{job_template_locale_id} | Update an organization job template locale
[**organization_job_template_locales_create**](OrganizationJobTemplateLocalesApi.md#organization_job_template_locales_create) | **POST** /accounts/{account_id}/job_templates/{job_template_id}/locales | Create an organization job template locale
[**organization_job_template_locales_list**](OrganizationJobTemplateLocalesApi.md#organization_job_template_locales_list) | **GET** /accounts/{account_id}/job_templates/{job_template_id}/locales | List organization job template locales


# **organization_job_template_locale_delete**
> organization_job_template_locale_delete(account_id, job_template_id, job_template_locale_id, x_phrase_app_otp=x_phrase_app_otp)

Delete an organization job template locale

Delete an existing organization job template locale.

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
    api_instance = phrase_api.OrganizationJobTemplateLocalesApi(api_client)
    account_id = 'account_id_example' # str | Account ID (required)
    job_template_id = 'job_template_id_example' # str | Job Template ID (required)
    job_template_locale_id = 'job_template_locale_id_example' # str | Job Template Locale ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Delete an organization job template locale
        api_instance.organization_job_template_locale_delete(account_id, job_template_id, job_template_locale_id, x_phrase_app_otp=x_phrase_app_otp)
    except ApiException as e:
        print("Exception when calling OrganizationJobTemplateLocalesApi->organization_job_template_locale_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID | 
 **job_template_id** | **str**| Job Template ID | 
 **job_template_locale_id** | **str**| Job Template Locale ID | 
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

# **organization_job_template_locale_show**
> JobTemplateLocales organization_job_template_locale_show(account_id, job_template_id, job_template_locale_id, x_phrase_app_otp=x_phrase_app_otp)

Get a single organization job template locale

Get a single job template locale for a given organization job template.

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
    api_instance = phrase_api.OrganizationJobTemplateLocalesApi(api_client)
    account_id = 'account_id_example' # str | Account ID (required)
    job_template_id = 'job_template_id_example' # str | Job Template ID (required)
    job_template_locale_id = 'job_template_locale_id_example' # str | Job Template Locale ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Get a single organization job template locale
        api_response = api_instance.organization_job_template_locale_show(account_id, job_template_id, job_template_locale_id, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrganizationJobTemplateLocalesApi->organization_job_template_locale_show: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID | 
 **job_template_id** | **str**| Job Template ID | 
 **job_template_locale_id** | **str**| Job Template Locale ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**JobTemplateLocales**](JobTemplateLocales.md)

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

# **organization_job_template_locale_update**
> JobTemplateLocales organization_job_template_locale_update(account_id, job_template_id, job_template_locale_id, organization_job_template_locale_update_parameters, x_phrase_app_otp=x_phrase_app_otp)

Update an organization job template locale

Update an existing organization job template locale.

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
    api_instance = phrase_api.OrganizationJobTemplateLocalesApi(api_client)
    account_id = 'account_id_example' # str | Account ID (required)
    job_template_id = 'job_template_id_example' # str | Job Template ID (required)
    job_template_locale_id = 'job_template_locale_id_example' # str | Job Template Locale ID (required)
    organization_job_template_locale_update_parameters = phrase_api.OrganizationJobTemplateLocaleUpdateParameters() # OrganizationJobTemplateLocaleUpdateParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Update an organization job template locale
        api_response = api_instance.organization_job_template_locale_update(account_id, job_template_id, job_template_locale_id, organization_job_template_locale_update_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrganizationJobTemplateLocalesApi->organization_job_template_locale_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID | 
 **job_template_id** | **str**| Job Template ID | 
 **job_template_locale_id** | **str**| Job Template Locale ID | 
 **organization_job_template_locale_update_parameters** | [**OrganizationJobTemplateLocaleUpdateParameters**](OrganizationJobTemplateLocaleUpdateParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**JobTemplateLocales**](JobTemplateLocales.md)

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

# **organization_job_template_locales_create**
> JobTemplateLocales organization_job_template_locales_create(account_id, job_template_id, organization_job_template_locales_create_parameters, x_phrase_app_otp=x_phrase_app_otp)

Create an organization job template locale

Create a new organization job template locale.

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
    api_instance = phrase_api.OrganizationJobTemplateLocalesApi(api_client)
    account_id = 'account_id_example' # str | Account ID (required)
    job_template_id = 'job_template_id_example' # str | Job Template ID (required)
    organization_job_template_locales_create_parameters = phrase_api.OrganizationJobTemplateLocalesCreateParameters() # OrganizationJobTemplateLocalesCreateParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Create an organization job template locale
        api_response = api_instance.organization_job_template_locales_create(account_id, job_template_id, organization_job_template_locales_create_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrganizationJobTemplateLocalesApi->organization_job_template_locales_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID | 
 **job_template_id** | **str**| Job Template ID | 
 **organization_job_template_locales_create_parameters** | [**OrganizationJobTemplateLocalesCreateParameters**](OrganizationJobTemplateLocalesCreateParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**JobTemplateLocales**](JobTemplateLocales.md)

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

# **organization_job_template_locales_list**
> List[JobTemplateLocales] organization_job_template_locales_list(account_id, job_template_id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page)

List organization job template locales

List all job template locales for a given organization job template.

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
    api_instance = phrase_api.OrganizationJobTemplateLocalesApi(api_client)
    account_id = 'account_id_example' # str | Account ID (required)
    job_template_id = 'job_template_id_example' # str | Job Template ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    page = 1 # int | Page number
    per_page = 25 # int | Limit on the number of objects to be returned, between 1 and 100. 25 by default

    try:
        # List organization job template locales
        api_response = api_instance.organization_job_template_locales_list(account_id, job_template_id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrganizationJobTemplateLocalesApi->organization_job_template_locales_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID | 
 **job_template_id** | **str**| Job Template ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Limit on the number of objects to be returned, between 1 and 100. 25 by default | [optional] 

### Return type

[**List[JobTemplateLocales]**](JobTemplateLocales.md)

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


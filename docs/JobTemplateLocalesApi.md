# phrase_api.JobTemplateLocalesApi

All URIs are relative to *https://api.phrase.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**job_template_locale_delete**](JobTemplateLocalesApi.md#job_template_locale_delete) | **DELETE** /projects/{project_id}/job_templates/{job_template_id}/locales/{job_template_locale_id} | Delete a job template locale
[**job_template_locale_show**](JobTemplateLocalesApi.md#job_template_locale_show) | **GET** /projects/{project_id}/job_templates/{job_template_id}/locales/{job_template_locale_id} | Get a single job template locale
[**job_template_locale_update**](JobTemplateLocalesApi.md#job_template_locale_update) | **PATCH** /projects/{project_id}/job_templates/{job_template_id}/locales/{job_template_locale_id} | Update a job template locale
[**job_template_locales_create**](JobTemplateLocalesApi.md#job_template_locales_create) | **POST** /projects/{project_id}/job_templates/{job_template_id}/locales | Create a job template locale
[**job_template_locales_list**](JobTemplateLocalesApi.md#job_template_locales_list) | **GET** /projects/{project_id}/job_templates/{job_template_id}/locales | List job template locales


# **job_template_locale_delete**
> job_template_locale_delete(project_id, job_template_id, job_template_locale_id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)

Delete a job template locale

Delete an existing job template locale.

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
    api_instance = phrase_api.JobTemplateLocalesApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    job_template_id = 'job_template_id_example' # str | Job Template ID (required)
    job_template_locale_id = 'job_template_locale_id_example' # str | Job Template Locale ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    branch = 'my-feature-branch' # str | specify the branch to use

    try:
        # Delete a job template locale
        api_instance.job_template_locale_delete(project_id, job_template_id, job_template_locale_id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)
    except ApiException as e:
        print("Exception when calling JobTemplateLocalesApi->job_template_locale_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **job_template_id** | **str**| Job Template ID | 
 **job_template_locale_id** | **str**| Job Template Locale ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **branch** | **str**| specify the branch to use | [optional] 

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

# **job_template_locale_show**
> JobTemplateLocales job_template_locale_show(project_id, job_template_id, job_template_locale_id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)

Get a single job template locale

Get a single job template locale for a given job template.

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
    api_instance = phrase_api.JobTemplateLocalesApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    job_template_id = 'job_template_id_example' # str | Job Template ID (required)
    job_template_locale_id = 'job_template_locale_id_example' # str | Job Template Locale ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    branch = 'my-feature-branch' # str | specify the branch to use

    try:
        # Get a single job template locale
        api_response = api_instance.job_template_locale_show(project_id, job_template_id, job_template_locale_id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobTemplateLocalesApi->job_template_locale_show: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **job_template_id** | **str**| Job Template ID | 
 **job_template_locale_id** | **str**| Job Template Locale ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **branch** | **str**| specify the branch to use | [optional] 

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

# **job_template_locale_update**
> JobTemplateLocales job_template_locale_update(project_id, job_template_id, job_template_locale_id, job_template_locale_update_parameters, x_phrase_app_otp=x_phrase_app_otp)

Update a job template locale

Update an existing job template locale.

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
    api_instance = phrase_api.JobTemplateLocalesApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    job_template_id = 'job_template_id_example' # str | Job Template ID (required)
    job_template_locale_id = 'job_template_locale_id_example' # str | Job Template Locale ID (required)
    job_template_locale_update_parameters = phrase_api.JobTemplateLocaleUpdateParameters() # JobTemplateLocaleUpdateParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Update a job template locale
        api_response = api_instance.job_template_locale_update(project_id, job_template_id, job_template_locale_id, job_template_locale_update_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobTemplateLocalesApi->job_template_locale_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **job_template_id** | **str**| Job Template ID | 
 **job_template_locale_id** | **str**| Job Template Locale ID | 
 **job_template_locale_update_parameters** | [**JobTemplateLocaleUpdateParameters**](JobTemplateLocaleUpdateParameters.md)|  | 
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

# **job_template_locales_create**
> JobTemplateLocales job_template_locales_create(project_id, job_template_id, job_template_locales_create_parameters, x_phrase_app_otp=x_phrase_app_otp)

Create a job template locale

Create a new job template locale.

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
    api_instance = phrase_api.JobTemplateLocalesApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    job_template_id = 'job_template_id_example' # str | Job Template ID (required)
    job_template_locales_create_parameters = phrase_api.JobTemplateLocalesCreateParameters() # JobTemplateLocalesCreateParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Create a job template locale
        api_response = api_instance.job_template_locales_create(project_id, job_template_id, job_template_locales_create_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobTemplateLocalesApi->job_template_locales_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **job_template_id** | **str**| Job Template ID | 
 **job_template_locales_create_parameters** | [**JobTemplateLocalesCreateParameters**](JobTemplateLocalesCreateParameters.md)|  | 
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

# **job_template_locales_list**
> list[JobTemplateLocales] job_template_locales_list(project_id, job_template_id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page, branch=branch)

List job template locales

List all job template locales for a given job template.

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
    api_instance = phrase_api.JobTemplateLocalesApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    job_template_id = 'job_template_id_example' # str | Job Template ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    page = 1 # int | Page number
    per_page = 25 # int | Limit on the number of objects to be returned, between 1 and 100. 25 by default
    branch = 'my-feature-branch' # str | specify the branch to use

    try:
        # List job template locales
        api_response = api_instance.job_template_locales_list(project_id, job_template_id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page, branch=branch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobTemplateLocalesApi->job_template_locales_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **job_template_id** | **str**| Job Template ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Limit on the number of objects to be returned, between 1 and 100. 25 by default | [optional] 
 **branch** | **str**| specify the branch to use | [optional] 

### Return type

[**list[JobTemplateLocales]**](JobTemplateLocales.md)

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


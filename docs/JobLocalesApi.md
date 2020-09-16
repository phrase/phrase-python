# phrase_api.JobLocalesApi

All URIs are relative to *https://api.phrase.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**job_locale_complete**](JobLocalesApi.md#job_locale_complete) | **POST** /projects/{project_id}/jobs/{job_id}/locales/{id}/complete | Complete a job locale
[**job_locale_delete**](JobLocalesApi.md#job_locale_delete) | **DELETE** /projects/{project_id}/jobs/{job_id}/locales/{id} | Delete a job locale
[**job_locale_reopen**](JobLocalesApi.md#job_locale_reopen) | **POST** /projects/{project_id}/jobs/{job_id}/locales/{id}/reopen | Reopen a job locale
[**job_locale_show**](JobLocalesApi.md#job_locale_show) | **GET** /projects/{project_id}/jobs/{job_id}/locale/{id} | Get a single job locale
[**job_locale_update**](JobLocalesApi.md#job_locale_update) | **PATCH** /projects/{project_id}/jobs/{job_id}/locales/{id} | Update a job locale
[**job_locales_create**](JobLocalesApi.md#job_locales_create) | **POST** /projects/{project_id}/jobs/{job_id}/locales | Create a job locale
[**job_locales_list**](JobLocalesApi.md#job_locales_list) | **GET** /projects/{project_id}/jobs/{job_id}/locales | List job locales


# **job_locale_complete**
> JobLocale job_locale_complete(project_id, job_id, id, job_locale_complete_parameters, x_phrase_app_otp=x_phrase_app_otp)

Complete a job locale

Mark a job locale as completed.

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
    api_instance = phrase_api.JobLocalesApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    job_id = 'job_id_example' # str | Job ID (required)
    id = 'id_example' # str | ID (required)
    job_locale_complete_parameters = phrase_api.JobLocaleCompleteParameters() # JobLocaleCompleteParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Complete a job locale
        api_response = api_instance.job_locale_complete(project_id, job_id, id, job_locale_complete_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobLocalesApi->job_locale_complete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **job_id** | **str**| Job ID | 
 **id** | **str**| ID | 
 **job_locale_complete_parameters** | [**JobLocaleCompleteParameters**](JobLocaleCompleteParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**JobLocale**](JobLocale.md)

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

# **job_locale_delete**
> job_locale_delete(project_id, job_id, id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)

Delete a job locale

Delete an existing job locale.

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
    api_instance = phrase_api.JobLocalesApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    job_id = 'job_id_example' # str | Job ID (required)
    id = 'id_example' # str | ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    branch = 'my-feature-branch' # str | specify the branch to use

    try:
        # Delete a job locale
        api_instance.job_locale_delete(project_id, job_id, id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)
    except ApiException as e:
        print("Exception when calling JobLocalesApi->job_locale_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **job_id** | **str**| Job ID | 
 **id** | **str**| ID | 
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

# **job_locale_reopen**
> JobLocale job_locale_reopen(project_id, job_id, id, job_locale_reopen_parameters, x_phrase_app_otp=x_phrase_app_otp)

Reopen a job locale

Mark a job locale as uncompleted.

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
    api_instance = phrase_api.JobLocalesApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    job_id = 'job_id_example' # str | Job ID (required)
    id = 'id_example' # str | ID (required)
    job_locale_reopen_parameters = phrase_api.JobLocaleReopenParameters() # JobLocaleReopenParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Reopen a job locale
        api_response = api_instance.job_locale_reopen(project_id, job_id, id, job_locale_reopen_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobLocalesApi->job_locale_reopen: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **job_id** | **str**| Job ID | 
 **id** | **str**| ID | 
 **job_locale_reopen_parameters** | [**JobLocaleReopenParameters**](JobLocaleReopenParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**JobLocale**](JobLocale.md)

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

# **job_locale_show**
> JobLocale job_locale_show(project_id, job_id, id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)

Get a single job locale

Get a single job locale for a given job.

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
    api_instance = phrase_api.JobLocalesApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    job_id = 'job_id_example' # str | Job ID (required)
    id = 'id_example' # str | ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    branch = 'my-feature-branch' # str | specify the branch to use

    try:
        # Get a single job locale
        api_response = api_instance.job_locale_show(project_id, job_id, id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobLocalesApi->job_locale_show: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **job_id** | **str**| Job ID | 
 **id** | **str**| ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **branch** | **str**| specify the branch to use | [optional] 

### Return type

[**JobLocale**](JobLocale.md)

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

# **job_locale_update**
> JobLocale job_locale_update(project_id, job_id, id, job_locale_update_parameters, x_phrase_app_otp=x_phrase_app_otp)

Update a job locale

Update an existing job locale.

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
    api_instance = phrase_api.JobLocalesApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    job_id = 'job_id_example' # str | Job ID (required)
    id = 'id_example' # str | ID (required)
    job_locale_update_parameters = phrase_api.JobLocaleUpdateParameters() # JobLocaleUpdateParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Update a job locale
        api_response = api_instance.job_locale_update(project_id, job_id, id, job_locale_update_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobLocalesApi->job_locale_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **job_id** | **str**| Job ID | 
 **id** | **str**| ID | 
 **job_locale_update_parameters** | [**JobLocaleUpdateParameters**](JobLocaleUpdateParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**JobLocale**](JobLocale.md)

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

# **job_locales_create**
> JobLocale job_locales_create(project_id, job_id, job_locales_create_parameters, x_phrase_app_otp=x_phrase_app_otp)

Create a job locale

Create a new job locale.

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
    api_instance = phrase_api.JobLocalesApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    job_id = 'job_id_example' # str | Job ID (required)
    job_locales_create_parameters = phrase_api.JobLocalesCreateParameters() # JobLocalesCreateParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Create a job locale
        api_response = api_instance.job_locales_create(project_id, job_id, job_locales_create_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobLocalesApi->job_locales_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **job_id** | **str**| Job ID | 
 **job_locales_create_parameters** | [**JobLocalesCreateParameters**](JobLocalesCreateParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**JobLocale**](JobLocale.md)

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

# **job_locales_list**
> list[JobLocale] job_locales_list(project_id, job_id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page, branch=branch)

List job locales

List all job locales for a given job.

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
    api_instance = phrase_api.JobLocalesApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    job_id = 'job_id_example' # str | Job ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    page = 1 # int | Page number
    per_page = 25 # int | allows you to specify a page size up to 100 items, 25 by default
    branch = 'my-feature-branch' # str | specify the branch to use

    try:
        # List job locales
        api_response = api_instance.job_locales_list(project_id, job_id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page, branch=branch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobLocalesApi->job_locales_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **job_id** | **str**| Job ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| allows you to specify a page size up to 100 items, 25 by default | [optional] 
 **branch** | **str**| specify the branch to use | [optional] 

### Return type

[**list[JobLocale]**](JobLocale.md)

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


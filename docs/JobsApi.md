# Phrase.JobsApi

All URIs are relative to *https://api.phrase.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**job_complete**](JobsApi.md#job_complete) | **POST** /projects/{project_id}/jobs/{id}/complete | Complete a job
[**job_create**](JobsApi.md#job_create) | **POST** /projects/{project_id}/jobs | Create a job
[**job_delete**](JobsApi.md#job_delete) | **DELETE** /projects/{project_id}/jobs/{id} | Delete a job
[**job_keys_create**](JobsApi.md#job_keys_create) | **POST** /projects/{project_id}/jobs/{id}/keys | Add keys to job
[**job_keys_delete**](JobsApi.md#job_keys_delete) | **DELETE** /projects/{project_id}/jobs/{id}/keys | Remove keys from job
[**job_reopen**](JobsApi.md#job_reopen) | **POST** /projects/{project_id}/jobs/{id}/reopen | Reopen a job
[**job_show**](JobsApi.md#job_show) | **GET** /projects/{project_id}/jobs/{id} | Get a single job
[**job_start**](JobsApi.md#job_start) | **POST** /projects/{project_id}/jobs/{id}/start | Start a job
[**job_update**](JobsApi.md#job_update) | **PATCH** /projects/{project_id}/jobs/{id} | Update a job
[**jobs_list**](JobsApi.md#jobs_list) | **GET** /projects/{project_id}/jobs | List jobs


# **job_complete**
> JobDetails job_complete(project_id, id, job_complete_parameters, x_phrase_app_otp=x_phrase_app_otp)

Complete a job

Mark a job as completed.

### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import Phrase
from Phrase.rest import ApiException
from pprint import pprint
configuration = Phrase.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = Phrase.Configuration()
# Configure API key authorization: Token
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.phrase.com/v2
configuration.host = "https://api.phrase.com/v2"

# Enter a context with an instance of the API client
with Phrase.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = Phrase.JobsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
id = 'id_example' # str | ID
job_complete_parameters = Phrase.JobCompleteParameters() # JobCompleteParameters | 
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Complete a job
        api_response = api_instance.job_complete(project_id, id, job_complete_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->job_complete: %s\n" % e)
```

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import Phrase
from Phrase.rest import ApiException
from pprint import pprint
configuration = Phrase.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = Phrase.Configuration()
# Configure API key authorization: Token
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.phrase.com/v2
configuration.host = "https://api.phrase.com/v2"

# Enter a context with an instance of the API client
with Phrase.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = Phrase.JobsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
id = 'id_example' # str | ID
job_complete_parameters = Phrase.JobCompleteParameters() # JobCompleteParameters | 
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Complete a job
        api_response = api_instance.job_complete(project_id, id, job_complete_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->job_complete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **id** | **str**| ID | 
 **job_complete_parameters** | [**JobCompleteParameters**](JobCompleteParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**JobDetails**](JobDetails.md)

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

# **job_create**
> job_create(project_id, job_create_parameters, x_phrase_app_otp=x_phrase_app_otp)

Create a job

Create a new job.

### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import Phrase
from Phrase.rest import ApiException
from pprint import pprint
configuration = Phrase.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = Phrase.Configuration()
# Configure API key authorization: Token
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.phrase.com/v2
configuration.host = "https://api.phrase.com/v2"

# Enter a context with an instance of the API client
with Phrase.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = Phrase.JobsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
job_create_parameters = Phrase.JobCreateParameters() # JobCreateParameters | 
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Create a job
        api_instance.job_create(project_id, job_create_parameters, x_phrase_app_otp=x_phrase_app_otp)
    except ApiException as e:
        print("Exception when calling JobsApi->job_create: %s\n" % e)
```

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import Phrase
from Phrase.rest import ApiException
from pprint import pprint
configuration = Phrase.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = Phrase.Configuration()
# Configure API key authorization: Token
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.phrase.com/v2
configuration.host = "https://api.phrase.com/v2"

# Enter a context with an instance of the API client
with Phrase.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = Phrase.JobsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
job_create_parameters = Phrase.JobCreateParameters() # JobCreateParameters | 
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Create a job
        api_instance.job_create(project_id, job_create_parameters, x_phrase_app_otp=x_phrase_app_otp)
    except ApiException as e:
        print("Exception when calling JobsApi->job_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **job_create_parameters** | [**JobCreateParameters**](JobCreateParameters.md)|  | 
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
**201** | The resource has been created |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**400** | Bad request |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**404** | Not Found |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**429** | Rate Limiting |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_delete**
> job_delete(project_id, id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)

Delete a job

Delete an existing job.

### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import Phrase
from Phrase.rest import ApiException
from pprint import pprint
configuration = Phrase.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = Phrase.Configuration()
# Configure API key authorization: Token
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.phrase.com/v2
configuration.host = "https://api.phrase.com/v2"

# Enter a context with an instance of the API client
with Phrase.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = Phrase.JobsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
id = 'id_example' # str | ID
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)
branch = 'my-feature-branch' # str | specify the branch to use (optional)

    try:
        # Delete a job
        api_instance.job_delete(project_id, id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)
    except ApiException as e:
        print("Exception when calling JobsApi->job_delete: %s\n" % e)
```

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import Phrase
from Phrase.rest import ApiException
from pprint import pprint
configuration = Phrase.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = Phrase.Configuration()
# Configure API key authorization: Token
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.phrase.com/v2
configuration.host = "https://api.phrase.com/v2"

# Enter a context with an instance of the API client
with Phrase.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = Phrase.JobsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
id = 'id_example' # str | ID
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)
branch = 'my-feature-branch' # str | specify the branch to use (optional)

    try:
        # Delete a job
        api_instance.job_delete(project_id, id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)
    except ApiException as e:
        print("Exception when calling JobsApi->job_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
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

# **job_keys_create**
> JobDetails job_keys_create(project_id, id, job_keys_create_parameters, x_phrase_app_otp=x_phrase_app_otp)

Add keys to job

Add multiple keys to a existing job.

### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import Phrase
from Phrase.rest import ApiException
from pprint import pprint
configuration = Phrase.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = Phrase.Configuration()
# Configure API key authorization: Token
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.phrase.com/v2
configuration.host = "https://api.phrase.com/v2"

# Enter a context with an instance of the API client
with Phrase.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = Phrase.JobsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
id = 'id_example' # str | ID
job_keys_create_parameters = Phrase.JobKeysCreateParameters() # JobKeysCreateParameters | 
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Add keys to job
        api_response = api_instance.job_keys_create(project_id, id, job_keys_create_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->job_keys_create: %s\n" % e)
```

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import Phrase
from Phrase.rest import ApiException
from pprint import pprint
configuration = Phrase.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = Phrase.Configuration()
# Configure API key authorization: Token
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.phrase.com/v2
configuration.host = "https://api.phrase.com/v2"

# Enter a context with an instance of the API client
with Phrase.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = Phrase.JobsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
id = 'id_example' # str | ID
job_keys_create_parameters = Phrase.JobKeysCreateParameters() # JobKeysCreateParameters | 
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Add keys to job
        api_response = api_instance.job_keys_create(project_id, id, job_keys_create_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->job_keys_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **id** | **str**| ID | 
 **job_keys_create_parameters** | [**JobKeysCreateParameters**](JobKeysCreateParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**JobDetails**](JobDetails.md)

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

# **job_keys_delete**
> job_keys_delete(project_id, id, x_phrase_app_otp=x_phrase_app_otp, branch=branch, translation_key_ids=translation_key_ids)

Remove keys from job

Remove multiple keys from existing job.

### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import Phrase
from Phrase.rest import ApiException
from pprint import pprint
configuration = Phrase.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = Phrase.Configuration()
# Configure API key authorization: Token
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.phrase.com/v2
configuration.host = "https://api.phrase.com/v2"

# Enter a context with an instance of the API client
with Phrase.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = Phrase.JobsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
id = 'id_example' # str | ID
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)
branch = 'my-feature-branch' # str | specify the branch to use (optional)
translation_key_ids = ['[\"abcd1234cdef1234abcd1234cdef1234\"]'] # list[str] | ids of keys that should added to the job (optional)

    try:
        # Remove keys from job
        api_instance.job_keys_delete(project_id, id, x_phrase_app_otp=x_phrase_app_otp, branch=branch, translation_key_ids=translation_key_ids)
    except ApiException as e:
        print("Exception when calling JobsApi->job_keys_delete: %s\n" % e)
```

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import Phrase
from Phrase.rest import ApiException
from pprint import pprint
configuration = Phrase.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = Phrase.Configuration()
# Configure API key authorization: Token
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.phrase.com/v2
configuration.host = "https://api.phrase.com/v2"

# Enter a context with an instance of the API client
with Phrase.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = Phrase.JobsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
id = 'id_example' # str | ID
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)
branch = 'my-feature-branch' # str | specify the branch to use (optional)
translation_key_ids = ['[\"abcd1234cdef1234abcd1234cdef1234\"]'] # list[str] | ids of keys that should added to the job (optional)

    try:
        # Remove keys from job
        api_instance.job_keys_delete(project_id, id, x_phrase_app_otp=x_phrase_app_otp, branch=branch, translation_key_ids=translation_key_ids)
    except ApiException as e:
        print("Exception when calling JobsApi->job_keys_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **id** | **str**| ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **branch** | **str**| specify the branch to use | [optional] 
 **translation_key_ids** | [**list[str]**](str.md)| ids of keys that should added to the job | [optional] 

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

# **job_reopen**
> JobDetails job_reopen(project_id, id, job_reopen_parameters, x_phrase_app_otp=x_phrase_app_otp)

Reopen a job

Mark a job as uncompleted.

### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import Phrase
from Phrase.rest import ApiException
from pprint import pprint
configuration = Phrase.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = Phrase.Configuration()
# Configure API key authorization: Token
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.phrase.com/v2
configuration.host = "https://api.phrase.com/v2"

# Enter a context with an instance of the API client
with Phrase.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = Phrase.JobsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
id = 'id_example' # str | ID
job_reopen_parameters = Phrase.JobReopenParameters() # JobReopenParameters | 
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Reopen a job
        api_response = api_instance.job_reopen(project_id, id, job_reopen_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->job_reopen: %s\n" % e)
```

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import Phrase
from Phrase.rest import ApiException
from pprint import pprint
configuration = Phrase.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = Phrase.Configuration()
# Configure API key authorization: Token
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.phrase.com/v2
configuration.host = "https://api.phrase.com/v2"

# Enter a context with an instance of the API client
with Phrase.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = Phrase.JobsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
id = 'id_example' # str | ID
job_reopen_parameters = Phrase.JobReopenParameters() # JobReopenParameters | 
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Reopen a job
        api_response = api_instance.job_reopen(project_id, id, job_reopen_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->job_reopen: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **id** | **str**| ID | 
 **job_reopen_parameters** | [**JobReopenParameters**](JobReopenParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**JobDetails**](JobDetails.md)

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

# **job_show**
> JobDetails job_show(project_id, id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)

Get a single job

Get details on a single job for a given project.

### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import Phrase
from Phrase.rest import ApiException
from pprint import pprint
configuration = Phrase.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = Phrase.Configuration()
# Configure API key authorization: Token
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.phrase.com/v2
configuration.host = "https://api.phrase.com/v2"

# Enter a context with an instance of the API client
with Phrase.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = Phrase.JobsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
id = 'id_example' # str | ID
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)
branch = 'my-feature-branch' # str | specify the branch to use (optional)

    try:
        # Get a single job
        api_response = api_instance.job_show(project_id, id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->job_show: %s\n" % e)
```

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import Phrase
from Phrase.rest import ApiException
from pprint import pprint
configuration = Phrase.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = Phrase.Configuration()
# Configure API key authorization: Token
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.phrase.com/v2
configuration.host = "https://api.phrase.com/v2"

# Enter a context with an instance of the API client
with Phrase.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = Phrase.JobsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
id = 'id_example' # str | ID
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)
branch = 'my-feature-branch' # str | specify the branch to use (optional)

    try:
        # Get a single job
        api_response = api_instance.job_show(project_id, id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->job_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **id** | **str**| ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **branch** | **str**| specify the branch to use | [optional] 

### Return type

[**JobDetails**](JobDetails.md)

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

# **job_start**
> JobDetails job_start(project_id, id, job_start_parameters, x_phrase_app_otp=x_phrase_app_otp)

Start a job

Starts an existing job in state draft.

### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import Phrase
from Phrase.rest import ApiException
from pprint import pprint
configuration = Phrase.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = Phrase.Configuration()
# Configure API key authorization: Token
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.phrase.com/v2
configuration.host = "https://api.phrase.com/v2"

# Enter a context with an instance of the API client
with Phrase.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = Phrase.JobsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
id = 'id_example' # str | ID
job_start_parameters = Phrase.JobStartParameters() # JobStartParameters | 
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Start a job
        api_response = api_instance.job_start(project_id, id, job_start_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->job_start: %s\n" % e)
```

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import Phrase
from Phrase.rest import ApiException
from pprint import pprint
configuration = Phrase.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = Phrase.Configuration()
# Configure API key authorization: Token
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.phrase.com/v2
configuration.host = "https://api.phrase.com/v2"

# Enter a context with an instance of the API client
with Phrase.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = Phrase.JobsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
id = 'id_example' # str | ID
job_start_parameters = Phrase.JobStartParameters() # JobStartParameters | 
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Start a job
        api_response = api_instance.job_start(project_id, id, job_start_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->job_start: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **id** | **str**| ID | 
 **job_start_parameters** | [**JobStartParameters**](JobStartParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**JobDetails**](JobDetails.md)

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

# **job_update**
> JobDetails job_update(project_id, id, job_update_parameters, x_phrase_app_otp=x_phrase_app_otp)

Update a job

Update an existing job.

### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import Phrase
from Phrase.rest import ApiException
from pprint import pprint
configuration = Phrase.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = Phrase.Configuration()
# Configure API key authorization: Token
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.phrase.com/v2
configuration.host = "https://api.phrase.com/v2"

# Enter a context with an instance of the API client
with Phrase.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = Phrase.JobsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
id = 'id_example' # str | ID
job_update_parameters = Phrase.JobUpdateParameters() # JobUpdateParameters | 
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Update a job
        api_response = api_instance.job_update(project_id, id, job_update_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->job_update: %s\n" % e)
```

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import Phrase
from Phrase.rest import ApiException
from pprint import pprint
configuration = Phrase.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = Phrase.Configuration()
# Configure API key authorization: Token
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.phrase.com/v2
configuration.host = "https://api.phrase.com/v2"

# Enter a context with an instance of the API client
with Phrase.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = Phrase.JobsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
id = 'id_example' # str | ID
job_update_parameters = Phrase.JobUpdateParameters() # JobUpdateParameters | 
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Update a job
        api_response = api_instance.job_update(project_id, id, job_update_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->job_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **id** | **str**| ID | 
 **job_update_parameters** | [**JobUpdateParameters**](JobUpdateParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**JobDetails**](JobDetails.md)

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

# **jobs_list**
> list[Job] jobs_list(project_id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page, branch=branch, owned_by=owned_by, assigned_to=assigned_to, state=state)

List jobs

List all jobs for the given project.

### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import Phrase
from Phrase.rest import ApiException
from pprint import pprint
configuration = Phrase.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = Phrase.Configuration()
# Configure API key authorization: Token
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.phrase.com/v2
configuration.host = "https://api.phrase.com/v2"

# Enter a context with an instance of the API client
with Phrase.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = Phrase.JobsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)
page = 1 # int | Page number (optional)
per_page = 10 # int | allows you to specify a page size up to 100 items, 10 by default (optional)
branch = 'my-feature-branch' # str | specify the branch to use (optional)
owned_by = 'abcd1234cdef1234abcd1234cdef1234' # str | filter by user owning job (optional)
assigned_to = 'abcd1234cdef1234abcd1234cdef1234' # str | filter by user assigned to job (optional)
state = 'completed' # str | filter by state of job Valid states are <code>draft</code>, <code>in_progress</code>, <code>completed</code> (optional)

    try:
        # List jobs
        api_response = api_instance.jobs_list(project_id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page, branch=branch, owned_by=owned_by, assigned_to=assigned_to, state=state)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->jobs_list: %s\n" % e)
```

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import Phrase
from Phrase.rest import ApiException
from pprint import pprint
configuration = Phrase.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = Phrase.Configuration()
# Configure API key authorization: Token
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.phrase.com/v2
configuration.host = "https://api.phrase.com/v2"

# Enter a context with an instance of the API client
with Phrase.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = Phrase.JobsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)
page = 1 # int | Page number (optional)
per_page = 10 # int | allows you to specify a page size up to 100 items, 10 by default (optional)
branch = 'my-feature-branch' # str | specify the branch to use (optional)
owned_by = 'abcd1234cdef1234abcd1234cdef1234' # str | filter by user owning job (optional)
assigned_to = 'abcd1234cdef1234abcd1234cdef1234' # str | filter by user assigned to job (optional)
state = 'completed' # str | filter by state of job Valid states are <code>draft</code>, <code>in_progress</code>, <code>completed</code> (optional)

    try:
        # List jobs
        api_response = api_instance.jobs_list(project_id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page, branch=branch, owned_by=owned_by, assigned_to=assigned_to, state=state)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->jobs_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| allows you to specify a page size up to 100 items, 10 by default | [optional] 
 **branch** | **str**| specify the branch to use | [optional] 
 **owned_by** | **str**| filter by user owning job | [optional] 
 **assigned_to** | **str**| filter by user assigned to job | [optional] 
 **state** | **str**| filter by state of job Valid states are &lt;code&gt;draft&lt;/code&gt;, &lt;code&gt;in_progress&lt;/code&gt;, &lt;code&gt;completed&lt;/code&gt; | [optional] 

### Return type

[**list[Job]**](Job.md)

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


# phrase-api.ProjectsApi

All URIs are relative to *https://api.phrase.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**project_create**](ProjectsApi.md#project_create) | **POST** /projects | Create a project
[**project_delete**](ProjectsApi.md#project_delete) | **DELETE** /projects/{id} | Delete a project
[**project_show**](ProjectsApi.md#project_show) | **GET** /projects/{id} | Get a single project
[**project_update**](ProjectsApi.md#project_update) | **PATCH** /projects/{id} | Update a project
[**projects_list**](ProjectsApi.md#projects_list) | **GET** /projects | List projects


# **project_create**
> project_create(project_create_parameters, x_phrase_app_otp=x_phrase_app_otp)

Create a project

Create a new project.

### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import phrase-api
from phrase-api.rest import ApiException
from pprint import pprint
configuration = phrase-api.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = phrase-api.Configuration()
# Configure API key authorization: Token
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.phrase.com/v2
configuration.host = "https://api.phrase.com/v2"

# Enter a context with an instance of the API client
with phrase-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = phrase-api.ProjectsApi(api_client)
    project_create_parameters = phrase-api.ProjectCreateParameters() # ProjectCreateParameters | 
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Create a project
        api_instance.project_create(project_create_parameters, x_phrase_app_otp=x_phrase_app_otp)
    except ApiException as e:
        print("Exception when calling ProjectsApi->project_create: %s\n" % e)
```

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import phrase-api
from phrase-api.rest import ApiException
from pprint import pprint
configuration = phrase-api.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = phrase-api.Configuration()
# Configure API key authorization: Token
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.phrase.com/v2
configuration.host = "https://api.phrase.com/v2"

# Enter a context with an instance of the API client
with phrase-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = phrase-api.ProjectsApi(api_client)
    project_create_parameters = phrase-api.ProjectCreateParameters() # ProjectCreateParameters | 
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Create a project
        api_instance.project_create(project_create_parameters, x_phrase_app_otp=x_phrase_app_otp)
    except ApiException as e:
        print("Exception when calling ProjectsApi->project_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_create_parameters** | [**ProjectCreateParameters**](ProjectCreateParameters.md)|  | 
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

# **project_delete**
> project_delete(id, x_phrase_app_otp=x_phrase_app_otp)

Delete a project

Delete an existing project.

### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import phrase-api
from phrase-api.rest import ApiException
from pprint import pprint
configuration = phrase-api.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = phrase-api.Configuration()
# Configure API key authorization: Token
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.phrase.com/v2
configuration.host = "https://api.phrase.com/v2"

# Enter a context with an instance of the API client
with phrase-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = phrase-api.ProjectsApi(api_client)
    id = 'id_example' # str | ID
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Delete a project
        api_instance.project_delete(id, x_phrase_app_otp=x_phrase_app_otp)
    except ApiException as e:
        print("Exception when calling ProjectsApi->project_delete: %s\n" % e)
```

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import phrase-api
from phrase-api.rest import ApiException
from pprint import pprint
configuration = phrase-api.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = phrase-api.Configuration()
# Configure API key authorization: Token
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.phrase.com/v2
configuration.host = "https://api.phrase.com/v2"

# Enter a context with an instance of the API client
with phrase-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = phrase-api.ProjectsApi(api_client)
    id = 'id_example' # str | ID
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Delete a project
        api_instance.project_delete(id, x_phrase_app_otp=x_phrase_app_otp)
    except ApiException as e:
        print("Exception when calling ProjectsApi->project_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **project_show**
> ProjectDetails project_show(id, x_phrase_app_otp=x_phrase_app_otp)

Get a single project

Get details on a single project.

### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import phrase-api
from phrase-api.rest import ApiException
from pprint import pprint
configuration = phrase-api.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = phrase-api.Configuration()
# Configure API key authorization: Token
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.phrase.com/v2
configuration.host = "https://api.phrase.com/v2"

# Enter a context with an instance of the API client
with phrase-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = phrase-api.ProjectsApi(api_client)
    id = 'id_example' # str | ID
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Get a single project
        api_response = api_instance.project_show(id, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->project_show: %s\n" % e)
```

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import phrase-api
from phrase-api.rest import ApiException
from pprint import pprint
configuration = phrase-api.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = phrase-api.Configuration()
# Configure API key authorization: Token
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.phrase.com/v2
configuration.host = "https://api.phrase.com/v2"

# Enter a context with an instance of the API client
with phrase-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = phrase-api.ProjectsApi(api_client)
    id = 'id_example' # str | ID
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Get a single project
        api_response = api_instance.project_show(id, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->project_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**ProjectDetails**](ProjectDetails.md)

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

# **project_update**
> ProjectDetails project_update(id, project_update_parameters, x_phrase_app_otp=x_phrase_app_otp)

Update a project

Update an existing project.

### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import phrase-api
from phrase-api.rest import ApiException
from pprint import pprint
configuration = phrase-api.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = phrase-api.Configuration()
# Configure API key authorization: Token
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.phrase.com/v2
configuration.host = "https://api.phrase.com/v2"

# Enter a context with an instance of the API client
with phrase-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = phrase-api.ProjectsApi(api_client)
    id = 'id_example' # str | ID
project_update_parameters = phrase-api.ProjectUpdateParameters() # ProjectUpdateParameters | 
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Update a project
        api_response = api_instance.project_update(id, project_update_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->project_update: %s\n" % e)
```

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import phrase-api
from phrase-api.rest import ApiException
from pprint import pprint
configuration = phrase-api.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = phrase-api.Configuration()
# Configure API key authorization: Token
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.phrase.com/v2
configuration.host = "https://api.phrase.com/v2"

# Enter a context with an instance of the API client
with phrase-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = phrase-api.ProjectsApi(api_client)
    id = 'id_example' # str | ID
project_update_parameters = phrase-api.ProjectUpdateParameters() # ProjectUpdateParameters | 
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Update a project
        api_response = api_instance.project_update(id, project_update_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->project_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID | 
 **project_update_parameters** | [**ProjectUpdateParameters**](ProjectUpdateParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**ProjectDetails**](ProjectDetails.md)

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

# **projects_list**
> list[Project] projects_list(x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page)

List projects

List all projects the current user has access to.

### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import phrase-api
from phrase-api.rest import ApiException
from pprint import pprint
configuration = phrase-api.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = phrase-api.Configuration()
# Configure API key authorization: Token
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.phrase.com/v2
configuration.host = "https://api.phrase.com/v2"

# Enter a context with an instance of the API client
with phrase-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = phrase-api.ProjectsApi(api_client)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)
page = 1 # int | Page number (optional)
per_page = 10 # int | allows you to specify a page size up to 100 items, 10 by default (optional)

    try:
        # List projects
        api_response = api_instance.projects_list(x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->projects_list: %s\n" % e)
```

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import phrase-api
from phrase-api.rest import ApiException
from pprint import pprint
configuration = phrase-api.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = phrase-api.Configuration()
# Configure API key authorization: Token
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.phrase.com/v2
configuration.host = "https://api.phrase.com/v2"

# Enter a context with an instance of the API client
with phrase-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = phrase-api.ProjectsApi(api_client)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)
page = 1 # int | Page number (optional)
per_page = 10 # int | allows you to specify a page size up to 100 items, 10 by default (optional)

    try:
        # List projects
        api_response = api_instance.projects_list(x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->projects_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| allows you to specify a page size up to 100 items, 10 by default | [optional] 

### Return type

[**list[Project]**](Project.md)

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


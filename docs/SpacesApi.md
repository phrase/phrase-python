# phrase-api.SpacesApi

All URIs are relative to *https://api.phrase.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**space_create**](SpacesApi.md#space_create) | **POST** /accounts/{account_id}/spaces | Create a Space
[**space_delete**](SpacesApi.md#space_delete) | **DELETE** /accounts/{account_id}/spaces/{id} | Delete Space
[**space_show**](SpacesApi.md#space_show) | **GET** /accounts/{account_id}/spaces/{id} | Get Space
[**space_update**](SpacesApi.md#space_update) | **PATCH** /accounts/{account_id}/spaces/{id} | Update Space
[**spaces_list**](SpacesApi.md#spaces_list) | **GET** /accounts/{account_id}/spaces | List Spaces
[**spaces_projects_create**](SpacesApi.md#spaces_projects_create) | **POST** /accounts/{account_id}/spaces/{space_id}/projects | Add Project
[**spaces_projects_delete**](SpacesApi.md#spaces_projects_delete) | **DELETE** /accounts/{account_id}/spaces/{space_id}/projects/{id} | Remove Project
[**spaces_projects_list**](SpacesApi.md#spaces_projects_list) | **GET** /accounts/{account_id}/spaces/{space_id}/projects | List Projects


# **space_create**
> space_create(account_id, space_create_parameters, x_phrase_app_otp=x_phrase_app_otp)

Create a Space

Create a new Space.

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
    api_instance = phrase-api.SpacesApi(api_client)
    account_id = 'account_id_example' # str | Account ID
space_create_parameters = phrase-api.SpaceCreateParameters() # SpaceCreateParameters | 
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Create a Space
        api_instance.space_create(account_id, space_create_parameters, x_phrase_app_otp=x_phrase_app_otp)
    except ApiException as e:
        print("Exception when calling SpacesApi->space_create: %s\n" % e)
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
    api_instance = phrase-api.SpacesApi(api_client)
    account_id = 'account_id_example' # str | Account ID
space_create_parameters = phrase-api.SpaceCreateParameters() # SpaceCreateParameters | 
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Create a Space
        api_instance.space_create(account_id, space_create_parameters, x_phrase_app_otp=x_phrase_app_otp)
    except ApiException as e:
        print("Exception when calling SpacesApi->space_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID | 
 **space_create_parameters** | [**SpaceCreateParameters**](SpaceCreateParameters.md)|  | 
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

# **space_delete**
> space_delete(account_id, id, x_phrase_app_otp=x_phrase_app_otp)

Delete Space

Delete the specified Space.

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
    api_instance = phrase-api.SpacesApi(api_client)
    account_id = 'account_id_example' # str | Account ID
id = 'id_example' # str | ID
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Delete Space
        api_instance.space_delete(account_id, id, x_phrase_app_otp=x_phrase_app_otp)
    except ApiException as e:
        print("Exception when calling SpacesApi->space_delete: %s\n" % e)
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
    api_instance = phrase-api.SpacesApi(api_client)
    account_id = 'account_id_example' # str | Account ID
id = 'id_example' # str | ID
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Delete Space
        api_instance.space_delete(account_id, id, x_phrase_app_otp=x_phrase_app_otp)
    except ApiException as e:
        print("Exception when calling SpacesApi->space_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID | 
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

# **space_show**
> Space space_show(account_id, id, x_phrase_app_otp=x_phrase_app_otp)

Get Space

Show the specified Space.

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
    api_instance = phrase-api.SpacesApi(api_client)
    account_id = 'account_id_example' # str | Account ID
id = 'id_example' # str | ID
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Get Space
        api_response = api_instance.space_show(account_id, id, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SpacesApi->space_show: %s\n" % e)
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
    api_instance = phrase-api.SpacesApi(api_client)
    account_id = 'account_id_example' # str | Account ID
id = 'id_example' # str | ID
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Get Space
        api_response = api_instance.space_show(account_id, id, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SpacesApi->space_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID | 
 **id** | **str**| ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**Space**](Space.md)

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

# **space_update**
> Space space_update(account_id, id, space_update_parameters, x_phrase_app_otp=x_phrase_app_otp)

Update Space

Update the specified Space.

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
    api_instance = phrase-api.SpacesApi(api_client)
    account_id = 'account_id_example' # str | Account ID
id = 'id_example' # str | ID
space_update_parameters = phrase-api.SpaceUpdateParameters() # SpaceUpdateParameters | 
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Update Space
        api_response = api_instance.space_update(account_id, id, space_update_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SpacesApi->space_update: %s\n" % e)
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
    api_instance = phrase-api.SpacesApi(api_client)
    account_id = 'account_id_example' # str | Account ID
id = 'id_example' # str | ID
space_update_parameters = phrase-api.SpaceUpdateParameters() # SpaceUpdateParameters | 
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Update Space
        api_response = api_instance.space_update(account_id, id, space_update_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SpacesApi->space_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID | 
 **id** | **str**| ID | 
 **space_update_parameters** | [**SpaceUpdateParameters**](SpaceUpdateParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**Space**](Space.md)

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

# **spaces_list**
> list[Space] spaces_list(account_id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page)

List Spaces

List all Spaces for the given account.

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
    api_instance = phrase-api.SpacesApi(api_client)
    account_id = 'account_id_example' # str | Account ID
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)
page = 1 # int | Page number (optional)
per_page = 10 # int | allows you to specify a page size up to 100 items, 10 by default (optional)

    try:
        # List Spaces
        api_response = api_instance.spaces_list(account_id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SpacesApi->spaces_list: %s\n" % e)
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
    api_instance = phrase-api.SpacesApi(api_client)
    account_id = 'account_id_example' # str | Account ID
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)
page = 1 # int | Page number (optional)
per_page = 10 # int | allows you to specify a page size up to 100 items, 10 by default (optional)

    try:
        # List Spaces
        api_response = api_instance.spaces_list(account_id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SpacesApi->spaces_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| allows you to specify a page size up to 100 items, 10 by default | [optional] 

### Return type

[**list[Space]**](Space.md)

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

# **spaces_projects_create**
> spaces_projects_create(account_id, space_id, spaces_projects_create_parameters, x_phrase_app_otp=x_phrase_app_otp)

Add Project

Adds an existing project to the space.

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
    api_instance = phrase-api.SpacesApi(api_client)
    account_id = 'account_id_example' # str | Account ID
space_id = 'space_id_example' # str | Space ID
spaces_projects_create_parameters = phrase-api.SpacesProjectsCreateParameters() # SpacesProjectsCreateParameters | 
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Add Project
        api_instance.spaces_projects_create(account_id, space_id, spaces_projects_create_parameters, x_phrase_app_otp=x_phrase_app_otp)
    except ApiException as e:
        print("Exception when calling SpacesApi->spaces_projects_create: %s\n" % e)
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
    api_instance = phrase-api.SpacesApi(api_client)
    account_id = 'account_id_example' # str | Account ID
space_id = 'space_id_example' # str | Space ID
spaces_projects_create_parameters = phrase-api.SpacesProjectsCreateParameters() # SpacesProjectsCreateParameters | 
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Add Project
        api_instance.spaces_projects_create(account_id, space_id, spaces_projects_create_parameters, x_phrase_app_otp=x_phrase_app_otp)
    except ApiException as e:
        print("Exception when calling SpacesApi->spaces_projects_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID | 
 **space_id** | **str**| Space ID | 
 **spaces_projects_create_parameters** | [**SpacesProjectsCreateParameters**](SpacesProjectsCreateParameters.md)|  | 
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

# **spaces_projects_delete**
> spaces_projects_delete(account_id, space_id, id, x_phrase_app_otp=x_phrase_app_otp)

Remove Project

Removes a specified project from the specified space.

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
    api_instance = phrase-api.SpacesApi(api_client)
    account_id = 'account_id_example' # str | Account ID
space_id = 'space_id_example' # str | Space ID
id = 'id_example' # str | ID
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Remove Project
        api_instance.spaces_projects_delete(account_id, space_id, id, x_phrase_app_otp=x_phrase_app_otp)
    except ApiException as e:
        print("Exception when calling SpacesApi->spaces_projects_delete: %s\n" % e)
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
    api_instance = phrase-api.SpacesApi(api_client)
    account_id = 'account_id_example' # str | Account ID
space_id = 'space_id_example' # str | Space ID
id = 'id_example' # str | ID
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Remove Project
        api_instance.spaces_projects_delete(account_id, space_id, id, x_phrase_app_otp=x_phrase_app_otp)
    except ApiException as e:
        print("Exception when calling SpacesApi->spaces_projects_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID | 
 **space_id** | **str**| Space ID | 
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

# **spaces_projects_list**
> list[Project] spaces_projects_list(account_id, space_id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page)

List Projects

List all projects for the specified Space.

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
    api_instance = phrase-api.SpacesApi(api_client)
    account_id = 'account_id_example' # str | Account ID
space_id = 'space_id_example' # str | Space ID
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)
page = 1 # int | Page number (optional)
per_page = 10 # int | allows you to specify a page size up to 100 items, 10 by default (optional)

    try:
        # List Projects
        api_response = api_instance.spaces_projects_list(account_id, space_id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SpacesApi->spaces_projects_list: %s\n" % e)
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
    api_instance = phrase-api.SpacesApi(api_client)
    account_id = 'account_id_example' # str | Account ID
space_id = 'space_id_example' # str | Space ID
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)
page = 1 # int | Page number (optional)
per_page = 10 # int | allows you to specify a page size up to 100 items, 10 by default (optional)

    try:
        # List Projects
        api_response = api_instance.spaces_projects_list(account_id, space_id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SpacesApi->spaces_projects_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID | 
 **space_id** | **str**| Space ID | 
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


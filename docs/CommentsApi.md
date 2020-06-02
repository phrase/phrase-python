# phrase-api.CommentsApi

All URIs are relative to *https://api.phrase.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**comment_create**](CommentsApi.md#comment_create) | **POST** /projects/{project_id}/keys/{key_id}/comments | Create a comment
[**comment_delete**](CommentsApi.md#comment_delete) | **DELETE** /projects/{project_id}/keys/{key_id}/comments/{id} | Delete a comment
[**comment_mark_check**](CommentsApi.md#comment_mark_check) | **GET** /projects/{project_id}/keys/{key_id}/comments/{id}/read | Check if comment is read
[**comment_mark_read**](CommentsApi.md#comment_mark_read) | **PATCH** /projects/{project_id}/keys/{key_id}/comments/{id}/read | Mark a comment as read
[**comment_mark_unread**](CommentsApi.md#comment_mark_unread) | **DELETE** /projects/{project_id}/keys/{key_id}/comments/{id}/read | Mark a comment as unread
[**comment_show**](CommentsApi.md#comment_show) | **GET** /projects/{project_id}/keys/{key_id}/comments/{id} | Get a single comment
[**comment_update**](CommentsApi.md#comment_update) | **PATCH** /projects/{project_id}/keys/{key_id}/comments/{id} | Update a comment
[**comments_list**](CommentsApi.md#comments_list) | **GET** /projects/{project_id}/keys/{key_id}/comments | List comments


# **comment_create**
> comment_create(project_id, key_id, comment_create_parameters, x_phrase_app_otp=x_phrase_app_otp)

Create a comment

Create a new comment for a key.

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
    api_instance = phrase-api.CommentsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
key_id = 'key_id_example' # str | Translation Key ID
comment_create_parameters = phrase-api.CommentCreateParameters() # CommentCreateParameters | 
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Create a comment
        api_instance.comment_create(project_id, key_id, comment_create_parameters, x_phrase_app_otp=x_phrase_app_otp)
    except ApiException as e:
        print("Exception when calling CommentsApi->comment_create: %s\n" % e)
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
    api_instance = phrase-api.CommentsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
key_id = 'key_id_example' # str | Translation Key ID
comment_create_parameters = phrase-api.CommentCreateParameters() # CommentCreateParameters | 
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Create a comment
        api_instance.comment_create(project_id, key_id, comment_create_parameters, x_phrase_app_otp=x_phrase_app_otp)
    except ApiException as e:
        print("Exception when calling CommentsApi->comment_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **key_id** | **str**| Translation Key ID | 
 **comment_create_parameters** | [**CommentCreateParameters**](CommentCreateParameters.md)|  | 
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

# **comment_delete**
> comment_delete(project_id, key_id, id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)

Delete a comment

Delete an existing comment.

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
    api_instance = phrase-api.CommentsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
key_id = 'key_id_example' # str | Translation Key ID
id = 'id_example' # str | ID
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)
branch = 'my-feature-branch' # str | specify the branch to use (optional)

    try:
        # Delete a comment
        api_instance.comment_delete(project_id, key_id, id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)
    except ApiException as e:
        print("Exception when calling CommentsApi->comment_delete: %s\n" % e)
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
    api_instance = phrase-api.CommentsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
key_id = 'key_id_example' # str | Translation Key ID
id = 'id_example' # str | ID
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)
branch = 'my-feature-branch' # str | specify the branch to use (optional)

    try:
        # Delete a comment
        api_instance.comment_delete(project_id, key_id, id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)
    except ApiException as e:
        print("Exception when calling CommentsApi->comment_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **key_id** | **str**| Translation Key ID | 
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

# **comment_mark_check**
> comment_mark_check(project_id, key_id, id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)

Check if comment is read

Check if comment was marked as read. Returns 204 if read, 404 if unread.

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
    api_instance = phrase-api.CommentsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
key_id = 'key_id_example' # str | Translation Key ID
id = 'id_example' # str | ID
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)
branch = 'my-feature-branch' # str | specify the branch to use (optional)

    try:
        # Check if comment is read
        api_instance.comment_mark_check(project_id, key_id, id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)
    except ApiException as e:
        print("Exception when calling CommentsApi->comment_mark_check: %s\n" % e)
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
    api_instance = phrase-api.CommentsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
key_id = 'key_id_example' # str | Translation Key ID
id = 'id_example' # str | ID
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)
branch = 'my-feature-branch' # str | specify the branch to use (optional)

    try:
        # Check if comment is read
        api_instance.comment_mark_check(project_id, key_id, id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)
    except ApiException as e:
        print("Exception when calling CommentsApi->comment_mark_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **key_id** | **str**| Translation Key ID | 
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

# **comment_mark_read**
> comment_mark_read(project_id, key_id, id, comment_mark_read_parameters, x_phrase_app_otp=x_phrase_app_otp)

Mark a comment as read

Mark a comment as read.

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
    api_instance = phrase-api.CommentsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
key_id = 'key_id_example' # str | Translation Key ID
id = 'id_example' # str | ID
comment_mark_read_parameters = phrase-api.CommentMarkReadParameters() # CommentMarkReadParameters | 
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Mark a comment as read
        api_instance.comment_mark_read(project_id, key_id, id, comment_mark_read_parameters, x_phrase_app_otp=x_phrase_app_otp)
    except ApiException as e:
        print("Exception when calling CommentsApi->comment_mark_read: %s\n" % e)
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
    api_instance = phrase-api.CommentsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
key_id = 'key_id_example' # str | Translation Key ID
id = 'id_example' # str | ID
comment_mark_read_parameters = phrase-api.CommentMarkReadParameters() # CommentMarkReadParameters | 
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Mark a comment as read
        api_instance.comment_mark_read(project_id, key_id, id, comment_mark_read_parameters, x_phrase_app_otp=x_phrase_app_otp)
    except ApiException as e:
        print("Exception when calling CommentsApi->comment_mark_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **key_id** | **str**| Translation Key ID | 
 **id** | **str**| ID | 
 **comment_mark_read_parameters** | [**CommentMarkReadParameters**](CommentMarkReadParameters.md)|  | 
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
**204** | The resource was deleted successfully. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**400** | Bad request |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**404** | Not Found |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**429** | Rate Limiting |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **comment_mark_unread**
> comment_mark_unread(project_id, key_id, id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)

Mark a comment as unread

Mark a comment as unread.

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
    api_instance = phrase-api.CommentsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
key_id = 'key_id_example' # str | Translation Key ID
id = 'id_example' # str | ID
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)
branch = 'my-feature-branch' # str | specify the branch to use (optional)

    try:
        # Mark a comment as unread
        api_instance.comment_mark_unread(project_id, key_id, id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)
    except ApiException as e:
        print("Exception when calling CommentsApi->comment_mark_unread: %s\n" % e)
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
    api_instance = phrase-api.CommentsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
key_id = 'key_id_example' # str | Translation Key ID
id = 'id_example' # str | ID
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)
branch = 'my-feature-branch' # str | specify the branch to use (optional)

    try:
        # Mark a comment as unread
        api_instance.comment_mark_unread(project_id, key_id, id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)
    except ApiException as e:
        print("Exception when calling CommentsApi->comment_mark_unread: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **key_id** | **str**| Translation Key ID | 
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

# **comment_show**
> Comment comment_show(project_id, key_id, id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)

Get a single comment

Get details on a single comment.

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
    api_instance = phrase-api.CommentsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
key_id = 'key_id_example' # str | Translation Key ID
id = 'id_example' # str | ID
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)
branch = 'my-feature-branch' # str | specify the branch to use (optional)

    try:
        # Get a single comment
        api_response = api_instance.comment_show(project_id, key_id, id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommentsApi->comment_show: %s\n" % e)
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
    api_instance = phrase-api.CommentsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
key_id = 'key_id_example' # str | Translation Key ID
id = 'id_example' # str | ID
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)
branch = 'my-feature-branch' # str | specify the branch to use (optional)

    try:
        # Get a single comment
        api_response = api_instance.comment_show(project_id, key_id, id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommentsApi->comment_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **key_id** | **str**| Translation Key ID | 
 **id** | **str**| ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **branch** | **str**| specify the branch to use | [optional] 

### Return type

[**Comment**](Comment.md)

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

# **comment_update**
> Comment comment_update(project_id, key_id, id, comment_update_parameters, x_phrase_app_otp=x_phrase_app_otp)

Update a comment

Update an existing comment.

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
    api_instance = phrase-api.CommentsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
key_id = 'key_id_example' # str | Translation Key ID
id = 'id_example' # str | ID
comment_update_parameters = phrase-api.CommentUpdateParameters() # CommentUpdateParameters | 
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Update a comment
        api_response = api_instance.comment_update(project_id, key_id, id, comment_update_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommentsApi->comment_update: %s\n" % e)
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
    api_instance = phrase-api.CommentsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
key_id = 'key_id_example' # str | Translation Key ID
id = 'id_example' # str | ID
comment_update_parameters = phrase-api.CommentUpdateParameters() # CommentUpdateParameters | 
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Update a comment
        api_response = api_instance.comment_update(project_id, key_id, id, comment_update_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommentsApi->comment_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **key_id** | **str**| Translation Key ID | 
 **id** | **str**| ID | 
 **comment_update_parameters** | [**CommentUpdateParameters**](CommentUpdateParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**Comment**](Comment.md)

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

# **comments_list**
> list[Comment] comments_list(project_id, key_id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page, branch=branch)

List comments

List all comments for a key.

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
    api_instance = phrase-api.CommentsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
key_id = 'key_id_example' # str | Translation Key ID
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)
page = 1 # int | Page number (optional)
per_page = 10 # int | allows you to specify a page size up to 100 items, 10 by default (optional)
branch = 'my-feature-branch' # str | specify the branch to use (optional)

    try:
        # List comments
        api_response = api_instance.comments_list(project_id, key_id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page, branch=branch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommentsApi->comments_list: %s\n" % e)
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
    api_instance = phrase-api.CommentsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
key_id = 'key_id_example' # str | Translation Key ID
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)
page = 1 # int | Page number (optional)
per_page = 10 # int | allows you to specify a page size up to 100 items, 10 by default (optional)
branch = 'my-feature-branch' # str | specify the branch to use (optional)

    try:
        # List comments
        api_response = api_instance.comments_list(project_id, key_id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page, branch=branch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommentsApi->comments_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **key_id** | **str**| Translation Key ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| allows you to specify a page size up to 100 items, 10 by default | [optional] 
 **branch** | **str**| specify the branch to use | [optional] 

### Return type

[**list[Comment]**](Comment.md)

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


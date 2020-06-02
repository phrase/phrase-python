# phrase-api.AuthorizationsApi

All URIs are relative to *https://api.phrase.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorization_create**](AuthorizationsApi.md#authorization_create) | **POST** /authorizations | Create an authorization
[**authorization_delete**](AuthorizationsApi.md#authorization_delete) | **DELETE** /authorizations/{id} | Delete an authorization
[**authorization_show**](AuthorizationsApi.md#authorization_show) | **GET** /authorizations/{id} | Get a single authorization
[**authorization_update**](AuthorizationsApi.md#authorization_update) | **PATCH** /authorizations/{id} | Update an authorization
[**authorizations_list**](AuthorizationsApi.md#authorizations_list) | **GET** /authorizations | List authorizations


# **authorization_create**
> authorization_create(authorization_create_parameters, x_phrase_app_otp=x_phrase_app_otp)

Create an authorization

Create a new authorization.

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
    api_instance = phrase-api.AuthorizationsApi(api_client)
    authorization_create_parameters = phrase-api.AuthorizationCreateParameters() # AuthorizationCreateParameters | 
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Create an authorization
        api_instance.authorization_create(authorization_create_parameters, x_phrase_app_otp=x_phrase_app_otp)
    except ApiException as e:
        print("Exception when calling AuthorizationsApi->authorization_create: %s\n" % e)
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
    api_instance = phrase-api.AuthorizationsApi(api_client)
    authorization_create_parameters = phrase-api.AuthorizationCreateParameters() # AuthorizationCreateParameters | 
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Create an authorization
        api_instance.authorization_create(authorization_create_parameters, x_phrase_app_otp=x_phrase_app_otp)
    except ApiException as e:
        print("Exception when calling AuthorizationsApi->authorization_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_create_parameters** | [**AuthorizationCreateParameters**](AuthorizationCreateParameters.md)|  | 
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

# **authorization_delete**
> authorization_delete(id, x_phrase_app_otp=x_phrase_app_otp)

Delete an authorization

Delete an existing authorization. API calls using that token will stop working.

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
    api_instance = phrase-api.AuthorizationsApi(api_client)
    id = 'id_example' # str | ID
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Delete an authorization
        api_instance.authorization_delete(id, x_phrase_app_otp=x_phrase_app_otp)
    except ApiException as e:
        print("Exception when calling AuthorizationsApi->authorization_delete: %s\n" % e)
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
    api_instance = phrase-api.AuthorizationsApi(api_client)
    id = 'id_example' # str | ID
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Delete an authorization
        api_instance.authorization_delete(id, x_phrase_app_otp=x_phrase_app_otp)
    except ApiException as e:
        print("Exception when calling AuthorizationsApi->authorization_delete: %s\n" % e)
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

# **authorization_show**
> Authorization authorization_show(id, x_phrase_app_otp=x_phrase_app_otp)

Get a single authorization

Get details on a single authorization.

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
    api_instance = phrase-api.AuthorizationsApi(api_client)
    id = 'id_example' # str | ID
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Get a single authorization
        api_response = api_instance.authorization_show(id, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthorizationsApi->authorization_show: %s\n" % e)
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
    api_instance = phrase-api.AuthorizationsApi(api_client)
    id = 'id_example' # str | ID
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Get a single authorization
        api_response = api_instance.authorization_show(id, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthorizationsApi->authorization_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**Authorization**](Authorization.md)

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

# **authorization_update**
> Authorization authorization_update(id, authorization_update_parameters, x_phrase_app_otp=x_phrase_app_otp)

Update an authorization

Update an existing authorization.

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
    api_instance = phrase-api.AuthorizationsApi(api_client)
    id = 'id_example' # str | ID
authorization_update_parameters = phrase-api.AuthorizationUpdateParameters() # AuthorizationUpdateParameters | 
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Update an authorization
        api_response = api_instance.authorization_update(id, authorization_update_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthorizationsApi->authorization_update: %s\n" % e)
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
    api_instance = phrase-api.AuthorizationsApi(api_client)
    id = 'id_example' # str | ID
authorization_update_parameters = phrase-api.AuthorizationUpdateParameters() # AuthorizationUpdateParameters | 
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)

    try:
        # Update an authorization
        api_response = api_instance.authorization_update(id, authorization_update_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthorizationsApi->authorization_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID | 
 **authorization_update_parameters** | [**AuthorizationUpdateParameters**](AuthorizationUpdateParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**Authorization**](Authorization.md)

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

# **authorizations_list**
> list[Authorization] authorizations_list(x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page)

List authorizations

List all your authorizations.

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
    api_instance = phrase-api.AuthorizationsApi(api_client)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)
page = 1 # int | Page number (optional)
per_page = 10 # int | allows you to specify a page size up to 100 items, 10 by default (optional)

    try:
        # List authorizations
        api_response = api_instance.authorizations_list(x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthorizationsApi->authorizations_list: %s\n" % e)
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
    api_instance = phrase-api.AuthorizationsApi(api_client)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)
page = 1 # int | Page number (optional)
per_page = 10 # int | allows you to specify a page size up to 100 items, 10 by default (optional)

    try:
        # List authorizations
        api_response = api_instance.authorizations_list(x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthorizationsApi->authorizations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| allows you to specify a page size up to 100 items, 10 by default | [optional] 

### Return type

[**list[Authorization]**](Authorization.md)

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


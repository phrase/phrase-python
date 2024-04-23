# phrase_api.LinkedKeysApi

All URIs are relative to *https://api.phrase.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**key_links_batch_destroy**](LinkedKeysApi.md#key_links_batch_destroy) | **DELETE** /projects/{project_id}/keys/{id}/key_links | Batch unlink child keys from a parent key
[**key_links_create**](LinkedKeysApi.md#key_links_create) | **POST** /projects/{project_id}/keys/{id}/key_links | Link child keys to a parent key
[**key_links_destroy**](LinkedKeysApi.md#key_links_destroy) | **DELETE** /projects/{project_id}/keys/{id}/key_links/{child_key_id} | Unlink a child key from a parent key
[**key_links_index**](LinkedKeysApi.md#key_links_index) | **GET** /projects/{project_id}/keys/{id}/key_links | List child keys of a parent key


# **key_links_batch_destroy**
> key_links_batch_destroy(project_id, id, key_links_batch_destroy_parameters, x_phrase_app_otp=x_phrase_app_otp)

Batch unlink child keys from a parent key

Unlinks multiple child keys from a given parent key in a single operation.

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
    api_instance = phrase_api.LinkedKeysApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    id = 'id_example' # str | Parent Translation Key ID (required)
    key_links_batch_destroy_parameters = phrase_api.KeyLinksBatchDestroyParameters() # KeyLinksBatchDestroyParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Batch unlink child keys from a parent key
        api_instance.key_links_batch_destroy(project_id, id, key_links_batch_destroy_parameters, x_phrase_app_otp=x_phrase_app_otp)
    except ApiException as e:
        print("Exception when calling LinkedKeysApi->key_links_batch_destroy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **id** | **str**| Parent Translation Key ID | 
 **key_links_batch_destroy_parameters** | [**KeyLinksBatchDestroyParameters**](KeyLinksBatchDestroyParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**422** | Unprocessable entity |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **key_links_create**
> KeyLink key_links_create(project_id, id, key_links_create_parameters, x_phrase_app_otp=x_phrase_app_otp)

Link child keys to a parent key

Creates links between a given parent key and one or more child keys.

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
    api_instance = phrase_api.LinkedKeysApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    id = 'id_example' # str | Parent Translation Key ID (required)
    key_links_create_parameters = phrase_api.KeyLinksCreateParameters() # KeyLinksCreateParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Link child keys to a parent key
        api_response = api_instance.key_links_create(project_id, id, key_links_create_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LinkedKeysApi->key_links_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **id** | **str**| Parent Translation Key ID | 
 **key_links_create_parameters** | [**KeyLinksCreateParameters**](KeyLinksCreateParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**KeyLink**](KeyLink.md)

### Authorization

[Basic](../README.md#Basic), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**422** | Unprocessable entity |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **key_links_destroy**
> key_links_destroy(project_id, id, child_key_id, x_phrase_app_otp=x_phrase_app_otp)

Unlink a child key from a parent key

Unlinks a single child key from a given parent key.

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
    api_instance = phrase_api.LinkedKeysApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    id = 'id_example' # str | Parent Translation Key ID (required)
    child_key_id = 'child_key_id_example' # str | The ID of the child key to unlink. (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Unlink a child key from a parent key
        api_instance.key_links_destroy(project_id, id, child_key_id, x_phrase_app_otp=x_phrase_app_otp)
    except ApiException as e:
        print("Exception when calling LinkedKeysApi->key_links_destroy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **id** | **str**| Parent Translation Key ID | 
 **child_key_id** | **str**| The ID of the child key to unlink. | 
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
**200** | OK |  -  |
**422** | Unprocessable entity |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **key_links_index**
> KeyLink key_links_index(project_id, id, x_phrase_app_otp=x_phrase_app_otp)

List child keys of a parent key

Returns detailed information about a parent key, including its linked child keys.

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
    api_instance = phrase_api.LinkedKeysApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    id = 'id_example' # str | Parent Translation Key ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # List child keys of a parent key
        api_response = api_instance.key_links_index(project_id, id, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LinkedKeysApi->key_links_index: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **id** | **str**| Parent Translation Key ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**KeyLink**](KeyLink.md)

### Authorization

[Basic](../README.md#Basic), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


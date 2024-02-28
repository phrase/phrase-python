# phrase_api.ScreenshotMarkersApi

All URIs are relative to *https://api.phrase.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**screenshot_marker_create**](ScreenshotMarkersApi.md#screenshot_marker_create) | **POST** /projects/{project_id}/screenshots/{screenshot_id}/markers | Create a screenshot marker
[**screenshot_marker_delete**](ScreenshotMarkersApi.md#screenshot_marker_delete) | **DELETE** /projects/{project_id}/screenshots/{screenshot_id}/markers | Delete a screenshot marker
[**screenshot_marker_show**](ScreenshotMarkersApi.md#screenshot_marker_show) | **GET** /projects/{project_id}/screenshots/{screenshot_id}/markers/{id} | Get a single screenshot marker
[**screenshot_marker_update**](ScreenshotMarkersApi.md#screenshot_marker_update) | **PATCH** /projects/{project_id}/screenshots/{screenshot_id}/markers | Update a screenshot marker
[**screenshot_markers_list**](ScreenshotMarkersApi.md#screenshot_markers_list) | **GET** /projects/{project_id}/screenshots/{id}/markers | List screenshot markers


# **screenshot_marker_create**
> ScreenshotMarker screenshot_marker_create(project_id, screenshot_id, screenshot_marker_create_parameters, x_phrase_app_otp=x_phrase_app_otp)

Create a screenshot marker

Create a new screenshot marker.

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
    api_instance = phrase_api.ScreenshotMarkersApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    screenshot_id = 'screenshot_id_example' # str | Screenshot ID (required)
    screenshot_marker_create_parameters = phrase_api.ScreenshotMarkerCreateParameters() # ScreenshotMarkerCreateParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Create a screenshot marker
        api_response = api_instance.screenshot_marker_create(project_id, screenshot_id, screenshot_marker_create_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScreenshotMarkersApi->screenshot_marker_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **screenshot_id** | **str**| Screenshot ID | 
 **screenshot_marker_create_parameters** | [**ScreenshotMarkerCreateParameters**](ScreenshotMarkerCreateParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**ScreenshotMarker**](ScreenshotMarker.md)

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

# **screenshot_marker_delete**
> screenshot_marker_delete(project_id, screenshot_id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)

Delete a screenshot marker

Delete an existing screenshot marker.

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
    api_instance = phrase_api.ScreenshotMarkersApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    screenshot_id = 'screenshot_id_example' # str | Screenshot ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    branch = 'my-feature-branch' # str | specify the branch to use

    try:
        # Delete a screenshot marker
        api_instance.screenshot_marker_delete(project_id, screenshot_id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)
    except ApiException as e:
        print("Exception when calling ScreenshotMarkersApi->screenshot_marker_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **screenshot_id** | **str**| Screenshot ID | 
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

# **screenshot_marker_show**
> ScreenshotMarker screenshot_marker_show(project_id, screenshot_id, id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)

Get a single screenshot marker

Get details on a single screenshot marker for a given project.

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
    api_instance = phrase_api.ScreenshotMarkersApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    screenshot_id = 'screenshot_id_example' # str | Screenshot ID (required)
    id = 'id_example' # str | ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    branch = 'my-feature-branch' # str | specify the branch to use

    try:
        # Get a single screenshot marker
        api_response = api_instance.screenshot_marker_show(project_id, screenshot_id, id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScreenshotMarkersApi->screenshot_marker_show: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **screenshot_id** | **str**| Screenshot ID | 
 **id** | **str**| ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **branch** | **str**| specify the branch to use | [optional] 

### Return type

[**ScreenshotMarker**](ScreenshotMarker.md)

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

# **screenshot_marker_update**
> ScreenshotMarker screenshot_marker_update(project_id, screenshot_id, screenshot_marker_update_parameters, x_phrase_app_otp=x_phrase_app_otp)

Update a screenshot marker

Update an existing screenshot marker.

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
    api_instance = phrase_api.ScreenshotMarkersApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    screenshot_id = 'screenshot_id_example' # str | Screenshot ID (required)
    screenshot_marker_update_parameters = phrase_api.ScreenshotMarkerUpdateParameters() # ScreenshotMarkerUpdateParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Update a screenshot marker
        api_response = api_instance.screenshot_marker_update(project_id, screenshot_id, screenshot_marker_update_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScreenshotMarkersApi->screenshot_marker_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **screenshot_id** | **str**| Screenshot ID | 
 **screenshot_marker_update_parameters** | [**ScreenshotMarkerUpdateParameters**](ScreenshotMarkerUpdateParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**ScreenshotMarker**](ScreenshotMarker.md)

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

# **screenshot_markers_list**
> List[ScreenshotMarker] screenshot_markers_list(project_id, id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page, branch=branch)

List screenshot markers

List all screenshot markers for the given project.

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
    api_instance = phrase_api.ScreenshotMarkersApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    id = 'id_example' # str | ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    page = 1 # int | Page number
    per_page = 25 # int | Limit on the number of objects to be returned, between 1 and 100. 25 by default
    branch = 'my-feature-branch' # str | specify the branch to use

    try:
        # List screenshot markers
        api_response = api_instance.screenshot_markers_list(project_id, id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page, branch=branch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScreenshotMarkersApi->screenshot_markers_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **id** | **str**| ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Limit on the number of objects to be returned, between 1 and 100. 25 by default | [optional] 
 **branch** | **str**| specify the branch to use | [optional] 

### Return type

[**List[ScreenshotMarker]**](ScreenshotMarker.md)

### Authorization

[Basic](../README.md#Basic), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  * Link -  <br>  * Pagination -  <br>  |
**400** | Bad request |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**404** | Not Found |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**429** | Rate Limiting |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


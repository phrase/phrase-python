# phrase_api.JobAnnotationsApi

All URIs are relative to *https://api.phrase.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**job_annotation_delete**](JobAnnotationsApi.md#job_annotation_delete) | **DELETE** /projects/{project_id}/jobs/{job_id}/annotations/{id} | Delete a job annotation
[**job_annotation_update**](JobAnnotationsApi.md#job_annotation_update) | **PATCH** /projects/{project_id}/jobs/{job_id}/annotations/{id} | Create/Update a job annotation
[**job_annotations_list**](JobAnnotationsApi.md#job_annotations_list) | **GET** /projects/{project_id}/jobs/{job_id}/annotations | List job annotations
[**job_locale_annotation_delete**](JobAnnotationsApi.md#job_locale_annotation_delete) | **DELETE** /projects/{project_id}/jobs/{job_id}/locales/{job_locale_id}/annotations/{id} | Delete a job locale annotation
[**job_locale_annotation_update**](JobAnnotationsApi.md#job_locale_annotation_update) | **PATCH** /projects/{project_id}/jobs/{job_id}/locales/{job_locale_id}/annotations/{id} | Create/Update a job locale annotation
[**job_locale_annotations_list**](JobAnnotationsApi.md#job_locale_annotations_list) | **GET** /projects/{project_id}/jobs/{job_id}/locales/{job_locale_id}/annotations | List job locale annotations


# **job_annotation_delete**
> job_annotation_delete(project_id, job_id, id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)

Delete a job annotation

Delete an annotation for a job.

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
    api_instance = phrase_api.JobAnnotationsApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    job_id = 'job_id_example' # str | Job ID (required)
    id = 'id_example' # str | Name of the annotation to delete. (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    branch = 'my-feature-branch' # str | Branch to use

    try:
        # Delete a job annotation
        api_instance.job_annotation_delete(project_id, job_id, id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)
    except ApiException as e:
        print("Exception when calling JobAnnotationsApi->job_annotation_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **job_id** | **str**| Job ID | 
 **id** | **str**| Name of the annotation to delete. | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **branch** | **str**| Branch to use | [optional] 

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
**204** | No Content |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**400** | Bad request |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**404** | Not Found |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**429** | Rate Limiting |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_annotation_update**
> JobAnnotation job_annotation_update(project_id, job_id, id, job_annotation_update_parameters, x_phrase_app_otp=x_phrase_app_otp)

Create/Update a job annotation

Create or update an annotation for a job. If the annotation already exists, it will be updated; otherwise, a new annotation will be created.

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
    api_instance = phrase_api.JobAnnotationsApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    job_id = 'job_id_example' # str | Job ID (required)
    id = 'id_example' # str | Name of the annotation to set or update. (required)
    job_annotation_update_parameters = phrase_api.JobAnnotationUpdateParameters() # JobAnnotationUpdateParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Create/Update a job annotation
        api_response = api_instance.job_annotation_update(project_id, job_id, id, job_annotation_update_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobAnnotationsApi->job_annotation_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **job_id** | **str**| Job ID | 
 **id** | **str**| Name of the annotation to set or update. | 
 **job_annotation_update_parameters** | [**JobAnnotationUpdateParameters**](JobAnnotationUpdateParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**JobAnnotation**](JobAnnotation.md)

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

# **job_annotations_list**
> List[JobAnnotation] job_annotations_list(project_id, job_id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)

List job annotations

Retrieve a list of annotations for a job.

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
    api_instance = phrase_api.JobAnnotationsApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    job_id = 'job_id_example' # str | Job ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    branch = 'my-feature-branch' # str | Branch to use

    try:
        # List job annotations
        api_response = api_instance.job_annotations_list(project_id, job_id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobAnnotationsApi->job_annotations_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **job_id** | **str**| Job ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **branch** | **str**| Branch to use | [optional] 

### Return type

[**List[JobAnnotation]**](JobAnnotation.md)

### Authorization

[Basic](../README.md#Basic), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_locale_annotation_delete**
> job_locale_annotation_delete(project_id, job_id, job_locale_id, id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)

Delete a job locale annotation

Delete an annotation for a job locale.

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
    api_instance = phrase_api.JobAnnotationsApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    job_id = 'job_id_example' # str | Job ID (required)
    job_locale_id = 'job_locale_id_example' # str | Job Locale ID (required)
    id = 'id_example' # str | Name of the annotation to delete. (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    branch = 'my-feature-branch' # str | Branch to use

    try:
        # Delete a job locale annotation
        api_instance.job_locale_annotation_delete(project_id, job_id, job_locale_id, id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)
    except ApiException as e:
        print("Exception when calling JobAnnotationsApi->job_locale_annotation_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **job_id** | **str**| Job ID | 
 **job_locale_id** | **str**| Job Locale ID | 
 **id** | **str**| Name of the annotation to delete. | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **branch** | **str**| Branch to use | [optional] 

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
**204** | No Content |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**400** | Bad request |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**404** | Not Found |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**429** | Rate Limiting |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_locale_annotation_update**
> JobAnnotation job_locale_annotation_update(project_id, job_id, job_locale_id, id, job_annotation_update_parameters, x_phrase_app_otp=x_phrase_app_otp)

Create/Update a job locale annotation

Create or update an annotation for a job locale. If the annotation already exists, it will be updated; otherwise, a new annotation will be created.

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
    api_instance = phrase_api.JobAnnotationsApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    job_id = 'job_id_example' # str | Job ID (required)
    job_locale_id = 'job_locale_id_example' # str | Job Locale ID (required)
    id = 'id_example' # str | Name of the annotation to set or update. (required)
    job_annotation_update_parameters = phrase_api.JobAnnotationUpdateParameters() # JobAnnotationUpdateParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Create/Update a job locale annotation
        api_response = api_instance.job_locale_annotation_update(project_id, job_id, job_locale_id, id, job_annotation_update_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobAnnotationsApi->job_locale_annotation_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **job_id** | **str**| Job ID | 
 **job_locale_id** | **str**| Job Locale ID | 
 **id** | **str**| Name of the annotation to set or update. | 
 **job_annotation_update_parameters** | [**JobAnnotationUpdateParameters**](JobAnnotationUpdateParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**JobAnnotation**](JobAnnotation.md)

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

# **job_locale_annotations_list**
> List[JobAnnotation] job_locale_annotations_list(project_id, job_id, job_locale_id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)

List job locale annotations

Retrieve a list of annotations for a job locale.

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
    api_instance = phrase_api.JobAnnotationsApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    job_id = 'job_id_example' # str | Job ID (required)
    job_locale_id = 'job_locale_id_example' # str | Job Locale ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    branch = 'my-feature-branch' # str | Branch to use

    try:
        # List job locale annotations
        api_response = api_instance.job_locale_annotations_list(project_id, job_id, job_locale_id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobAnnotationsApi->job_locale_annotations_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **job_id** | **str**| Job ID | 
 **job_locale_id** | **str**| Job Locale ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **branch** | **str**| Branch to use | [optional] 

### Return type

[**List[JobAnnotation]**](JobAnnotation.md)

### Authorization

[Basic](../README.md#Basic), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


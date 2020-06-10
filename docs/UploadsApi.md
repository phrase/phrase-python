# phrase-api.UploadsApi

All URIs are relative to *https://api.phrase.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**upload_create**](UploadsApi.md#upload_create) | **POST** /projects/{project_id}/uploads | Upload a new file
[**upload_show**](UploadsApi.md#upload_show) | **GET** /projects/{project_id}/uploads/{id} | View upload details
[**uploads_list**](UploadsApi.md#uploads_list) | **GET** /projects/{project_id}/uploads | List uploads


# **upload_create**
> Upload upload_create(project_id, x_phrase_app_otp=x_phrase_app_otp, branch=branch, file=file, file_format=file_format, locale_id=locale_id, tags=tags, update_translations=update_translations, update_descriptions=update_descriptions, convert_emoji=convert_emoji, skip_upload_tags=skip_upload_tags, skip_unverification=skip_unverification, file_encoding=file_encoding, locale_mapping=locale_mapping, format_options=format_options, autotranslate=autotranslate, mark_reviewed=mark_reviewed)

Upload a new file

Upload a new language file. Creates necessary resources in your project.

### Example

```python
from __future__ import print_function
import time
import phrase-api
from phrase-api.rest import ApiException
from pprint import pprint

configuration = phrase-api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'token'

# Enter a context with an instance of the API client
with phrase-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = phrase-api.UploadsApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    branch = 'branch_example' # str | specify the branch to use
    file = '/path/to/file' # file | File to be imported
    file_format = 'file_format_example' # str | File format. Auto-detected when possible and not specified.
    locale_id = 'locale_id_example' # str | Locale of the file's content. Can be the name or public id of the locale. Preferred is the public id.
    tags = 'tags_example' # str | List of tags separated by comma to be associated with the new keys contained in the upload.
    update_translations = True # bool | Indicates whether existing translations should be updated with the file content.
    update_descriptions = True # bool | Existing key descriptions will be updated with the file content. Empty descriptions overwrite existing descriptions.
    convert_emoji = True # bool | This option is obsolete. Providing the option will cause a bad request error.
    skip_upload_tags = True # bool | Indicates whether the upload should not create upload tags.
    skip_unverification = True # bool | Indicates whether the upload should unverify updated translations.
    file_encoding = 'file_encoding_example' # str | Enforces a specific encoding on the file contents. Valid options are \\\"UTF-8\\\", \\\"UTF-16\\\" and \\\"ISO-8859-1\\\".
    locale_mapping = None # object | Optional, format specific mapping between locale names and the columns the translations to those locales are contained in.
    format_options = None # object | Additional options available for specific formats. See our format guide for complete list.
    autotranslate = True # bool | If set, translations for the uploaded language will be fetched automatically.
    mark_reviewed = True # bool | Indicated whether the imported translations should be marked as reviewed. This setting is available if the review workflow (currently beta) is enabled for the project.

    try:
        # Upload a new file
        api_response = api_instance.upload_create(project_id, x_phrase_app_otp=x_phrase_app_otp, branch=branch, file=file, file_format=file_format, locale_id=locale_id, tags=tags, update_translations=update_translations, update_descriptions=update_descriptions, convert_emoji=convert_emoji, skip_upload_tags=skip_upload_tags, skip_unverification=skip_unverification, file_encoding=file_encoding, locale_mapping=locale_mapping, format_options=format_options, autotranslate=autotranslate, mark_reviewed=mark_reviewed)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UploadsApi->upload_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **branch** | **str**| specify the branch to use | [optional] 
 **file** | **file**| File to be imported | [optional] 
 **file_format** | **str**| File format. Auto-detected when possible and not specified. | [optional] 
 **locale_id** | **str**| Locale of the file&#39;s content. Can be the name or public id of the locale. Preferred is the public id. | [optional] 
 **tags** | **str**| List of tags separated by comma to be associated with the new keys contained in the upload. | [optional] 
 **update_translations** | **bool**| Indicates whether existing translations should be updated with the file content. | [optional] 
 **update_descriptions** | **bool**| Existing key descriptions will be updated with the file content. Empty descriptions overwrite existing descriptions. | [optional] 
 **convert_emoji** | **bool**| This option is obsolete. Providing the option will cause a bad request error. | [optional] 
 **skip_upload_tags** | **bool**| Indicates whether the upload should not create upload tags. | [optional] 
 **skip_unverification** | **bool**| Indicates whether the upload should unverify updated translations. | [optional] 
 **file_encoding** | **str**| Enforces a specific encoding on the file contents. Valid options are \\\&quot;UTF-8\\\&quot;, \\\&quot;UTF-16\\\&quot; and \\\&quot;ISO-8859-1\\\&quot;. | [optional] 
 **locale_mapping** | [**object**](object.md)| Optional, format specific mapping between locale names and the columns the translations to those locales are contained in. | [optional] 
 **format_options** | [**object**](object.md)| Additional options available for specific formats. See our format guide for complete list. | [optional] 
 **autotranslate** | **bool**| If set, translations for the uploaded language will be fetched automatically. | [optional] 
 **mark_reviewed** | **bool**| Indicated whether the imported translations should be marked as reviewed. This setting is available if the review workflow (currently beta) is enabled for the project. | [optional] 

### Return type

[**Upload**](Upload.md)

### Authorization

[Basic](../README.md#Basic), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**400** | Bad request |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**404** | Not Found |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**429** | Rate Limiting |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_show**
> Upload upload_show(project_id, id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)

View upload details

View details and summary for a single upload.

### Example

```python
from __future__ import print_function
import time
import phrase-api
from phrase-api.rest import ApiException
from pprint import pprint

configuration = phrase-api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'token'

# Enter a context with an instance of the API client
with phrase-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = phrase-api.UploadsApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    id = 'id_example' # str | ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    branch = 'my-feature-branch' # str | specify the branch to use

    try:
        # View upload details
        api_response = api_instance.upload_show(project_id, id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UploadsApi->upload_show: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **id** | **str**| ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **branch** | **str**| specify the branch to use | [optional] 

### Return type

[**Upload**](Upload.md)

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

# **uploads_list**
> list[Upload] uploads_list(project_id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page, branch=branch)

List uploads

List all uploads for the given project.

### Example

```python
from __future__ import print_function
import time
import phrase-api
from phrase-api.rest import ApiException
from pprint import pprint

configuration = phrase-api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'token'

# Enter a context with an instance of the API client
with phrase-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = phrase-api.UploadsApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    page = 1 # int | Page number
    per_page = 10 # int | allows you to specify a page size up to 100 items, 10 by default
    branch = 'my-feature-branch' # str | specify the branch to use

    try:
        # List uploads
        api_response = api_instance.uploads_list(project_id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page, branch=branch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UploadsApi->uploads_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| allows you to specify a page size up to 100 items, 10 by default | [optional] 
 **branch** | **str**| specify the branch to use | [optional] 

### Return type

[**list[Upload]**](Upload.md)

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


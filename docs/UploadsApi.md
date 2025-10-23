# phrase_api.UploadsApi

All URIs are relative to *https://api.phrase.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**upload_create**](UploadsApi.md#upload_create) | **POST** /projects/{project_id}/uploads | Upload a new file
[**upload_show**](UploadsApi.md#upload_show) | **GET** /projects/{project_id}/uploads/{id} | Get a single upload
[**uploads_list**](UploadsApi.md#uploads_list) | **GET** /projects/{project_id}/uploads | List uploads


# **upload_create**
> Upload upload_create(project_id, file, file_format, locale_id, x_phrase_app_otp=x_phrase_app_otp, branch=branch, tags=tags, update_translations=update_translations, update_custom_metadata=update_custom_metadata, update_translation_keys=update_translation_keys, update_translations_on_source_match=update_translations_on_source_match, source_locale_id=source_locale_id, update_descriptions=update_descriptions, convert_emoji=convert_emoji, skip_upload_tags=skip_upload_tags, skip_unverification=skip_unverification, file_encoding=file_encoding, locale_mapping=locale_mapping, format_options=format_options, autotranslate=autotranslate, verify_mentioned_translations=verify_mentioned_translations, mark_reviewed=mark_reviewed, tag_only_affected_keys=tag_only_affected_keys, translation_key_prefix=translation_key_prefix)

Upload a new file

Upload a new language file. Creates necessary resources in your project.

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
    api_instance = phrase_api.UploadsApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    file = None # bytearray | File to be imported (required)
    file_format = 'file_format_example' # str | File format. Auto-detected when possible and not specified. (required)
    locale_id = 'locale_id_example' # str | Locale of the file's content. Can be the name or id of the locale. Preferred is id. (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    branch = 'branch_example' # str | specify the branch to use
    tags = 'tags_example' # str | List of tags separated by comma to be associated with the new keys contained in the upload.
    update_translations = True # bool | Indicates whether existing translations should be updated with the file content.
    update_custom_metadata = True # bool | Determines whether to update custom metadata values when uploading a file. If set to true, existing metadata can be changed or removed. Passing an empty value deletes the corresponding metadata property. (default to True)
    update_translation_keys = True # bool | Pass `false` here to prevent new keys from being created and existing keys updated. (default to True)
    update_translations_on_source_match = False # bool | Update target translations only if the source translations of the uploaded multilingual file match the stored translations. (default to False)
    source_locale_id = 'source_locale_id_example' # str | Specifies the source locale for multilingual files. Can be the name or id of the locale. Preferred is id.
    update_descriptions = True # bool | Existing key descriptions will be updated with the file content. Empty descriptions overwrite existing descriptions.
    convert_emoji = True # bool | This option is obsolete. Providing the option will cause a bad request error.
    skip_upload_tags = True # bool | Indicates whether the upload should not create upload tags.
    skip_unverification = True # bool | Indicates whether the upload should unverify updated translations.
    file_encoding = 'file_encoding_example' # str | Enforces a specific encoding on the file contents. Valid options are \\\"UTF-8\\\", \\\"UTF-16\\\" and \\\"ISO-8859-1\\\".
    locale_mapping = None # object | Mapping between locale names and translation columns. Required in some formats like CSV or XLSX.
    format_options = None # object | Additional options available for specific formats. See our format guide for the [complete list](https://support.phrase.com/hc/en-us/articles/9652464547740-List-of-Supported-File-Types-Strings).
    autotranslate = True # bool | If set, translations for the uploaded language will be fetched automatically.
    verify_mentioned_translations = False # bool | Indicates whether all translations mentioned in the upload should be verified. (default to False)
    mark_reviewed = True # bool | Indicated whether the imported translations should be marked as reviewed. This setting is available if the review workflow is enabled for the project.
    tag_only_affected_keys = False # bool | Indicates whether only keys affected (created or updated) by the upload should be tagged. The default is `false` (default to False)
    translation_key_prefix = 'translation_key_prefix_example' # str | This prefix will be added to all uploaded translation key names to prevent collisions. Use a meaningful prefix related to your project or file to keep key names organized.

    try:
        # Upload a new file
        api_response = api_instance.upload_create(project_id, file, file_format, locale_id, x_phrase_app_otp=x_phrase_app_otp, branch=branch, tags=tags, update_translations=update_translations, update_custom_metadata=update_custom_metadata, update_translation_keys=update_translation_keys, update_translations_on_source_match=update_translations_on_source_match, source_locale_id=source_locale_id, update_descriptions=update_descriptions, convert_emoji=convert_emoji, skip_upload_tags=skip_upload_tags, skip_unverification=skip_unverification, file_encoding=file_encoding, locale_mapping=locale_mapping, format_options=format_options, autotranslate=autotranslate, verify_mentioned_translations=verify_mentioned_translations, mark_reviewed=mark_reviewed, tag_only_affected_keys=tag_only_affected_keys, translation_key_prefix=translation_key_prefix)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UploadsApi->upload_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **file** | **bytearray**| File to be imported | 
 **file_format** | **str**| File format. Auto-detected when possible and not specified. | 
 **locale_id** | **str**| Locale of the file&#39;s content. Can be the name or id of the locale. Preferred is id. | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **branch** | **str**| specify the branch to use | [optional] 
 **tags** | **str**| List of tags separated by comma to be associated with the new keys contained in the upload. | [optional] 
 **update_translations** | **bool**| Indicates whether existing translations should be updated with the file content. | [optional] 
 **update_custom_metadata** | **bool**| Determines whether to update custom metadata values when uploading a file. If set to true, existing metadata can be changed or removed. Passing an empty value deletes the corresponding metadata property. | [optional] [default to True]
 **update_translation_keys** | **bool**| Pass &#x60;false&#x60; here to prevent new keys from being created and existing keys updated. | [optional] [default to True]
 **update_translations_on_source_match** | **bool**| Update target translations only if the source translations of the uploaded multilingual file match the stored translations. | [optional] [default to False]
 **source_locale_id** | **str**| Specifies the source locale for multilingual files. Can be the name or id of the locale. Preferred is id. | [optional] 
 **update_descriptions** | **bool**| Existing key descriptions will be updated with the file content. Empty descriptions overwrite existing descriptions. | [optional] 
 **convert_emoji** | **bool**| This option is obsolete. Providing the option will cause a bad request error. | [optional] 
 **skip_upload_tags** | **bool**| Indicates whether the upload should not create upload tags. | [optional] 
 **skip_unverification** | **bool**| Indicates whether the upload should unverify updated translations. | [optional] 
 **file_encoding** | **str**| Enforces a specific encoding on the file contents. Valid options are \\\&quot;UTF-8\\\&quot;, \\\&quot;UTF-16\\\&quot; and \\\&quot;ISO-8859-1\\\&quot;. | [optional] 
 **locale_mapping** | [**object**](object.md)| Mapping between locale names and translation columns. Required in some formats like CSV or XLSX. | [optional] 
 **format_options** | [**object**](object.md)| Additional options available for specific formats. See our format guide for the [complete list](https://support.phrase.com/hc/en-us/articles/9652464547740-List-of-Supported-File-Types-Strings). | [optional] 
 **autotranslate** | **bool**| If set, translations for the uploaded language will be fetched automatically. | [optional] 
 **verify_mentioned_translations** | **bool**| Indicates whether all translations mentioned in the upload should be verified. | [optional] [default to False]
 **mark_reviewed** | **bool**| Indicated whether the imported translations should be marked as reviewed. This setting is available if the review workflow is enabled for the project. | [optional] 
 **tag_only_affected_keys** | **bool**| Indicates whether only keys affected (created or updated) by the upload should be tagged. The default is &#x60;false&#x60; | [optional] [default to False]
 **translation_key_prefix** | **str**| This prefix will be added to all uploaded translation key names to prevent collisions. Use a meaningful prefix related to your project or file to keep key names organized. | [optional] 

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

Get a single upload

View details and summary for a single upload.

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
    api_instance = phrase_api.UploadsApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    id = 'id_example' # str | ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    branch = 'my-feature-branch' # str | specify the branch to use

    try:
        # Get a single upload
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
> List[Upload] uploads_list(project_id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page, branch=branch)

List uploads

List all uploads for the given project.

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
    api_instance = phrase_api.UploadsApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    page = 1 # int | Page number
    per_page = 25 # int | Limit on the number of objects to be returned, between 1 and 100. 25 by default
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
 **per_page** | **int**| Limit on the number of objects to be returned, between 1 and 100. 25 by default | [optional] 
 **branch** | **str**| specify the branch to use | [optional] 

### Return type

[**List[Upload]**](Upload.md)

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


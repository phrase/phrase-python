# phrase_api.LocalesApi

All URIs are relative to *https://api.phrase.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_locales**](LocalesApi.md#account_locales) | **GET** /accounts/{id}/locales | List locales used in account
[**locale_create**](LocalesApi.md#locale_create) | **POST** /projects/{project_id}/locales | Create a locale
[**locale_delete**](LocalesApi.md#locale_delete) | **DELETE** /projects/{project_id}/locales/{id} | Delete a locale
[**locale_download**](LocalesApi.md#locale_download) | **GET** /projects/{project_id}/locales/{id}/download | Download a locale
[**locale_show**](LocalesApi.md#locale_show) | **GET** /projects/{project_id}/locales/{id} | Get a single locale
[**locale_update**](LocalesApi.md#locale_update) | **PATCH** /projects/{project_id}/locales/{id} | Update a locale
[**locales_list**](LocalesApi.md#locales_list) | **GET** /projects/{project_id}/locales | List locales


# **account_locales**
> List[LocalePreview1] account_locales(id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page)

List locales used in account

List all locales unique by locale code used across all projects within an account.

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
    api_instance = phrase_api.LocalesApi(api_client)
    id = 'id_example' # str | ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    page = 1 # int | Page number
    per_page = 25 # int | Limit on the number of objects to be returned, between 1 and 100. 25 by default

    try:
        # List locales used in account
        api_response = api_instance.account_locales(id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LocalesApi->account_locales: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Limit on the number of objects to be returned, between 1 and 100. 25 by default | [optional] 

### Return type

[**List[LocalePreview1]**](LocalePreview1.md)

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

# **locale_create**
> LocaleDetails locale_create(project_id, locale_create_parameters, x_phrase_app_otp=x_phrase_app_otp)

Create a locale

Create a new locale.

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
    api_instance = phrase_api.LocalesApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    locale_create_parameters = phrase_api.LocaleCreateParameters() # LocaleCreateParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Create a locale
        api_response = api_instance.locale_create(project_id, locale_create_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LocalesApi->locale_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **locale_create_parameters** | [**LocaleCreateParameters**](LocaleCreateParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**LocaleDetails**](LocaleDetails.md)

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

# **locale_delete**
> locale_delete(project_id, id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)

Delete a locale

Delete an existing locale.

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
    api_instance = phrase_api.LocalesApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    id = 'id_example' # str | Locale ID or locale name (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    branch = 'my-feature-branch' # str | specify the branch to use

    try:
        # Delete a locale
        api_instance.locale_delete(project_id, id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)
    except ApiException as e:
        print("Exception when calling LocalesApi->locale_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **id** | **str**| Locale ID or locale name | 
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

# **locale_download**
> bytearray locale_download(project_id, id, x_phrase_app_otp=x_phrase_app_otp, if_modified_since=if_modified_since, if_none_match=if_none_match, branch=branch, file_format=file_format, tags=tags, tag=tag, include_empty_translations=include_empty_translations, exclude_empty_zero_forms=exclude_empty_zero_forms, include_translated_keys=include_translated_keys, keep_notranslate_tags=keep_notranslate_tags, convert_emoji=convert_emoji, format_options=format_options, encoding=encoding, skip_unverified_translations=skip_unverified_translations, include_unverified_translations=include_unverified_translations, use_last_reviewed_version=use_last_reviewed_version, fallback_locale_id=fallback_locale_id, source_locale_id=source_locale_id, translation_key_prefix=translation_key_prefix, filter_by_prefix=filter_by_prefix, custom_metadata_filters=custom_metadata_filters, locale_ids=locale_ids, updated_since=updated_since)

Download a locale

Download a locale in a specific file format.

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
    api_instance = phrase_api.LocalesApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    id = 'id_example' # str | Locale ID or locale name (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    if_modified_since = 'if_modified_since_example' # str | Last modified condition, see [Conditional GET requests / HTTP Caching](/en/api/strings/pagination#conditional-get-requests-%2F-http-caching) (optional)
    if_none_match = 'if_none_match_example' # str | ETag condition, see [Conditional GET requests / HTTP Caching](/en/api/strings/pagination#conditional-get-requests-%2F-http-caching) (optional)
    branch = 'my-feature-branch' # str | specify the branch to use
    file_format = 'yml' # str | File format name. See the [format guide](https://support.phrase.com/hc/en-us/sections/6111343326364) for all supported file formats.
    tags = 'feature1,feature2' # str | Limit results to keys tagged with a list of comma separated tag names.
    tag = 'feature' # str | Limit download to tagged keys. This parameter is deprecated. Please use the \"tags\" parameter instead
    include_empty_translations = True # bool | Indicates whether keys without translations should be included in the output as well.
    exclude_empty_zero_forms = True # bool | Indicates whether zero forms should be included when empty in pluralized keys.
    include_translated_keys = True # bool | Include translated keys in the locale file. Use in combination with include_empty_translations to obtain only untranslated keys.
    keep_notranslate_tags = True # bool | Indicates whether [NOTRANSLATE] tags should be kept.
    convert_emoji = True # bool | This option is obsolete. Projects that were created on or after Nov 29th 2019 or that did not contain emoji by then will not require this flag any longer since emoji are now supported natively.
    format_options = None # object | Additional formatting and render options. See the [format guide](https://support.phrase.com/hc/en-us/sections/6111343326364) for a list of options available for each format. Specify format options like this: `...&format_options[foo]=bar`
    encoding = 'encoding_example' # str | Enforces a specific encoding on the file contents. Valid options are \"UTF-8\", \"UTF-16\" and \"ISO-8859-1\".
    skip_unverified_translations = True # bool | Indicates whether the locale file should skip all unverified translations. This parameter is deprecated and should be replaced with `include_unverified_translations`.
    include_unverified_translations = True # bool | if set to false unverified translations are excluded
    use_last_reviewed_version = True # bool | If set to true the last reviewed version of a translation is used. This is only available if the review workflow is enabled for the project.
    fallback_locale_id = 'fallback_locale_id_example' # str | If a key has no translation in the locale being downloaded the translation in the fallback locale will be used. Provide the ID of the locale that should be used as the fallback. Requires include_empty_translations to be set to `true`.
    source_locale_id = 'source_locale_id_example' # str | Provides the source language of a corresponding job as the source language of the generated locale file. This parameter will be ignored unless used in combination with a `tag` parameter indicating a specific job.
    translation_key_prefix = 'prefix_' # str | Download all translation keys, and remove the specified prefix where possible. Warning: this may create duplicate key names if other keys share the same name after the prefix is removed.
    filter_by_prefix = True # bool | Only download translation keys containing the specified prefix, and remove the prefix from the generated file.
    custom_metadata_filters = None # object | Custom metadata filters. Provide the name of the metadata field and the value to filter by. Only keys with matching metadata will be included in the download. 
    locale_ids = ['[\"de\",\"en\"]'] # List[str] | Locale IDs or locale names
    updated_since = '2023-01-01T00:00:00Z' # str | Only include translations and keys that have been updated since the given date. The date must be in ISO 8601 format (e.g., `2023-01-01T00:00:00Z`). 

    try:
        # Download a locale
        api_response = api_instance.locale_download(project_id, id, x_phrase_app_otp=x_phrase_app_otp, if_modified_since=if_modified_since, if_none_match=if_none_match, branch=branch, file_format=file_format, tags=tags, tag=tag, include_empty_translations=include_empty_translations, exclude_empty_zero_forms=exclude_empty_zero_forms, include_translated_keys=include_translated_keys, keep_notranslate_tags=keep_notranslate_tags, convert_emoji=convert_emoji, format_options=format_options, encoding=encoding, skip_unverified_translations=skip_unverified_translations, include_unverified_translations=include_unverified_translations, use_last_reviewed_version=use_last_reviewed_version, fallback_locale_id=fallback_locale_id, source_locale_id=source_locale_id, translation_key_prefix=translation_key_prefix, filter_by_prefix=filter_by_prefix, custom_metadata_filters=custom_metadata_filters, locale_ids=locale_ids, updated_since=updated_since)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LocalesApi->locale_download: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **id** | **str**| Locale ID or locale name | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **if_modified_since** | **str**| Last modified condition, see [Conditional GET requests / HTTP Caching](/en/api/strings/pagination#conditional-get-requests-%2F-http-caching) (optional) | [optional] 
 **if_none_match** | **str**| ETag condition, see [Conditional GET requests / HTTP Caching](/en/api/strings/pagination#conditional-get-requests-%2F-http-caching) (optional) | [optional] 
 **branch** | **str**| specify the branch to use | [optional] 
 **file_format** | **str**| File format name. See the [format guide](https://support.phrase.com/hc/en-us/sections/6111343326364) for all supported file formats. | [optional] 
 **tags** | **str**| Limit results to keys tagged with a list of comma separated tag names. | [optional] 
 **tag** | **str**| Limit download to tagged keys. This parameter is deprecated. Please use the \&quot;tags\&quot; parameter instead | [optional] 
 **include_empty_translations** | **bool**| Indicates whether keys without translations should be included in the output as well. | [optional] 
 **exclude_empty_zero_forms** | **bool**| Indicates whether zero forms should be included when empty in pluralized keys. | [optional] 
 **include_translated_keys** | **bool**| Include translated keys in the locale file. Use in combination with include_empty_translations to obtain only untranslated keys. | [optional] 
 **keep_notranslate_tags** | **bool**| Indicates whether [NOTRANSLATE] tags should be kept. | [optional] 
 **convert_emoji** | **bool**| This option is obsolete. Projects that were created on or after Nov 29th 2019 or that did not contain emoji by then will not require this flag any longer since emoji are now supported natively. | [optional] 
 **format_options** | [**object**](.md)| Additional formatting and render options. See the [format guide](https://support.phrase.com/hc/en-us/sections/6111343326364) for a list of options available for each format. Specify format options like this: &#x60;...&amp;format_options[foo]&#x3D;bar&#x60; | [optional] 
 **encoding** | **str**| Enforces a specific encoding on the file contents. Valid options are \&quot;UTF-8\&quot;, \&quot;UTF-16\&quot; and \&quot;ISO-8859-1\&quot;. | [optional] 
 **skip_unverified_translations** | **bool**| Indicates whether the locale file should skip all unverified translations. This parameter is deprecated and should be replaced with &#x60;include_unverified_translations&#x60;. | [optional] 
 **include_unverified_translations** | **bool**| if set to false unverified translations are excluded | [optional] 
 **use_last_reviewed_version** | **bool**| If set to true the last reviewed version of a translation is used. This is only available if the review workflow is enabled for the project. | [optional] 
 **fallback_locale_id** | **str**| If a key has no translation in the locale being downloaded the translation in the fallback locale will be used. Provide the ID of the locale that should be used as the fallback. Requires include_empty_translations to be set to &#x60;true&#x60;. | [optional] 
 **source_locale_id** | **str**| Provides the source language of a corresponding job as the source language of the generated locale file. This parameter will be ignored unless used in combination with a &#x60;tag&#x60; parameter indicating a specific job. | [optional] 
 **translation_key_prefix** | **str**| Download all translation keys, and remove the specified prefix where possible. Warning: this may create duplicate key names if other keys share the same name after the prefix is removed. | [optional] 
 **filter_by_prefix** | **bool**| Only download translation keys containing the specified prefix, and remove the prefix from the generated file. | [optional] 
 **custom_metadata_filters** | [**object**](.md)| Custom metadata filters. Provide the name of the metadata field and the value to filter by. Only keys with matching metadata will be included in the download.  | [optional] 
 **locale_ids** | [**List[str]**](str.md)| Locale IDs or locale names | [optional] 
 **updated_since** | **str**| Only include translations and keys that have been updated since the given date. The date must be in ISO 8601 format (e.g., &#x60;2023-01-01T00:00:00Z&#x60;).  | [optional] 

### Return type

**bytearray**

### Authorization

[Basic](../README.md#Basic), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: *

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**400** | Bad request |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**404** | Not Found |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**429** | Rate Limiting |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locale_show**
> LocaleDetails locale_show(project_id, id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)

Get a single locale

Get details on a single locale for a given project.

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
    api_instance = phrase_api.LocalesApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    id = 'id_example' # str | Locale ID or locale name (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    branch = 'my-feature-branch' # str | specify the branch to use

    try:
        # Get a single locale
        api_response = api_instance.locale_show(project_id, id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LocalesApi->locale_show: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **id** | **str**| Locale ID or locale name | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **branch** | **str**| specify the branch to use | [optional] 

### Return type

[**LocaleDetails**](LocaleDetails.md)

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

# **locale_update**
> LocaleDetails locale_update(project_id, id, locale_update_parameters, x_phrase_app_otp=x_phrase_app_otp)

Update a locale

Update an existing locale.

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
    api_instance = phrase_api.LocalesApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    id = 'id_example' # str | Locale ID or locale name (required)
    locale_update_parameters = phrase_api.LocaleUpdateParameters() # LocaleUpdateParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Update a locale
        api_response = api_instance.locale_update(project_id, id, locale_update_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LocalesApi->locale_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **id** | **str**| Locale ID or locale name | 
 **locale_update_parameters** | [**LocaleUpdateParameters**](LocaleUpdateParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**LocaleDetails**](LocaleDetails.md)

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

# **locales_list**
> List[Locale] locales_list(project_id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page, sort_by=sort_by, branch=branch)

List locales

List all locales for the given project.

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
    api_instance = phrase_api.LocalesApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    page = 1 # int | Page number
    per_page = 25 # int | Limit on the number of objects to be returned, between 1 and 100. 25 by default
    sort_by = 'sort_by_example' # str | Sort locales. Valid options are \"name_asc\", \"name_desc\", \"default_asc\", \"default_desc\".
    branch = 'my-feature-branch' # str | specify the branch to use

    try:
        # List locales
        api_response = api_instance.locales_list(project_id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page, sort_by=sort_by, branch=branch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LocalesApi->locales_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Limit on the number of objects to be returned, between 1 and 100. 25 by default | [optional] 
 **sort_by** | **str**| Sort locales. Valid options are \&quot;name_asc\&quot;, \&quot;name_desc\&quot;, \&quot;default_asc\&quot;, \&quot;default_desc\&quot;. | [optional] 
 **branch** | **str**| specify the branch to use | [optional] 

### Return type

[**List[Locale]**](Locale.md)

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


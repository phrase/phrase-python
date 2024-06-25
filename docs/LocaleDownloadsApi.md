# phrase_api.LocaleDownloadsApi

All URIs are relative to *https://api.phrase.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**locale_download_create**](LocaleDownloadsApi.md#locale_download_create) | **POST** /projects/{project_id}/locales/{locale_id}/downloads | Initiate async download of a locale
[**locale_download_show**](LocaleDownloadsApi.md#locale_download_show) | **GET** /projects/{project_id}/locales/{locale_id}/downloads/{id} | Show status of an async locale download


# **locale_download_create**
> LocaleDownload locale_download_create(project_id, locale_id, locale_download_create_parameters, x_phrase_app_otp=x_phrase_app_otp, if_modified_since=if_modified_since, if_none_match=if_none_match)

Initiate async download of a locale

Prepare a locale for download in a specific file format.

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
    api_instance = phrase_api.LocaleDownloadsApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    locale_id = 'locale_id_example' # str | Locale ID (required)
    locale_download_create_parameters = phrase_api.LocaleDownloadCreateParameters() # LocaleDownloadCreateParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    if_modified_since = 'if_modified_since_example' # str | Last modified condition, see <a href=\"#overview--conditional-get-requests--http-caching\">Conditional GET requests / HTTP Caching</a> (optional)
    if_none_match = 'if_none_match_example' # str | ETag condition, see <a href=\"#overview--conditional-get-requests--http-caching\">Conditional GET requests / HTTP Caching</a> (optional)

    try:
        # Initiate async download of a locale
        api_response = api_instance.locale_download_create(project_id, locale_id, locale_download_create_parameters, x_phrase_app_otp=x_phrase_app_otp, if_modified_since=if_modified_since, if_none_match=if_none_match)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LocaleDownloadsApi->locale_download_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **locale_id** | **str**| Locale ID | 
 **locale_download_create_parameters** | [**LocaleDownloadCreateParameters**](LocaleDownloadCreateParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **if_modified_since** | **str**| Last modified condition, see &lt;a href&#x3D;\&quot;#overview--conditional-get-requests--http-caching\&quot;&gt;Conditional GET requests / HTTP Caching&lt;/a&gt; (optional) | [optional] 
 **if_none_match** | **str**| ETag condition, see &lt;a href&#x3D;\&quot;#overview--conditional-get-requests--http-caching\&quot;&gt;Conditional GET requests / HTTP Caching&lt;/a&gt; (optional) | [optional] 

### Return type

[**LocaleDownload**](LocaleDownload.md)

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

# **locale_download_show**
> LocaleDownload locale_download_show(project_id, locale_id, id, x_phrase_app_otp=x_phrase_app_otp, if_modified_since=if_modified_since, if_none_match=if_none_match)

Show status of an async locale download

Show status of already started async locale download. If the download is finished, the download link will be returned.

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
    api_instance = phrase_api.LocaleDownloadsApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    locale_id = 'locale_id_example' # str | Locale ID (required)
    id = 'id_example' # str | ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    if_modified_since = 'if_modified_since_example' # str | Last modified condition, see <a href=\"#overview--conditional-get-requests--http-caching\">Conditional GET requests / HTTP Caching</a> (optional)
    if_none_match = 'if_none_match_example' # str | ETag condition, see <a href=\"#overview--conditional-get-requests--http-caching\">Conditional GET requests / HTTP Caching</a> (optional)

    try:
        # Show status of an async locale download
        api_response = api_instance.locale_download_show(project_id, locale_id, id, x_phrase_app_otp=x_phrase_app_otp, if_modified_since=if_modified_since, if_none_match=if_none_match)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LocaleDownloadsApi->locale_download_show: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **locale_id** | **str**| Locale ID | 
 **id** | **str**| ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **if_modified_since** | **str**| Last modified condition, see &lt;a href&#x3D;\&quot;#overview--conditional-get-requests--http-caching\&quot;&gt;Conditional GET requests / HTTP Caching&lt;/a&gt; (optional) | [optional] 
 **if_none_match** | **str**| ETag condition, see &lt;a href&#x3D;\&quot;#overview--conditional-get-requests--http-caching\&quot;&gt;Conditional GET requests / HTTP Caching&lt;/a&gt; (optional) | [optional] 

### Return type

[**LocaleDownload**](LocaleDownload.md)

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


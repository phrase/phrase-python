# phrase-api.VersionsHistoryApi

All URIs are relative to *https://api.phrase.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**version_show**](VersionsHistoryApi.md#version_show) | **GET** /projects/{project_id}/translations/{translation_id}/versions/{id} | Get a single version
[**versions_list**](VersionsHistoryApi.md#versions_list) | **GET** /projects/{project_id}/translations/{translation_id}/versions | List all versions


# **version_show**
> TranslationVersionWithUser version_show(project_id, translation_id, id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)

Get a single version

Get details on a single version.

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
    api_instance = phrase-api.VersionsHistoryApi(api_client)
    project_id = 'project_id_example' # str | Project ID
translation_id = 'translation_id_example' # str | Translation ID
id = 'id_example' # str | ID
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)
branch = 'my-feature-branch' # str | specify the branch to use (optional)

    try:
        # Get a single version
        api_response = api_instance.version_show(project_id, translation_id, id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VersionsHistoryApi->version_show: %s\n" % e)
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
    api_instance = phrase-api.VersionsHistoryApi(api_client)
    project_id = 'project_id_example' # str | Project ID
translation_id = 'translation_id_example' # str | Translation ID
id = 'id_example' # str | ID
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)
branch = 'my-feature-branch' # str | specify the branch to use (optional)

    try:
        # Get a single version
        api_response = api_instance.version_show(project_id, translation_id, id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VersionsHistoryApi->version_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **translation_id** | **str**| Translation ID | 
 **id** | **str**| ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **branch** | **str**| specify the branch to use | [optional] 

### Return type

[**TranslationVersionWithUser**](TranslationVersionWithUser.md)

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

# **versions_list**
> list[TranslationVersion] versions_list(project_id, translation_id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page, branch=branch)

List all versions

List all versions for the given translation.

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
    api_instance = phrase-api.VersionsHistoryApi(api_client)
    project_id = 'project_id_example' # str | Project ID
translation_id = 'translation_id_example' # str | Translation ID
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)
page = 1 # int | Page number (optional)
per_page = 10 # int | allows you to specify a page size up to 100 items, 10 by default (optional)
branch = 'my-feature-branch' # str | specify the branch to use (optional)

    try:
        # List all versions
        api_response = api_instance.versions_list(project_id, translation_id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page, branch=branch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VersionsHistoryApi->versions_list: %s\n" % e)
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
    api_instance = phrase-api.VersionsHistoryApi(api_client)
    project_id = 'project_id_example' # str | Project ID
translation_id = 'translation_id_example' # str | Translation ID
x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional) (optional)
page = 1 # int | Page number (optional)
per_page = 10 # int | allows you to specify a page size up to 100 items, 10 by default (optional)
branch = 'my-feature-branch' # str | specify the branch to use (optional)

    try:
        # List all versions
        api_response = api_instance.versions_list(project_id, translation_id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page, branch=branch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VersionsHistoryApi->versions_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **translation_id** | **str**| Translation ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| allows you to specify a page size up to 100 items, 10 by default | [optional] 
 **branch** | **str**| specify the branch to use | [optional] 

### Return type

[**list[TranslationVersion]**](TranslationVersion.md)

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


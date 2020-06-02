# phrase-api.GitLabSyncApi

All URIs are relative to *https://api.phrase.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gitlab_sync_delete**](GitLabSyncApi.md#gitlab_sync_delete) | **DELETE** /gitlab_syncs/{id} | Delete single Sync Setting
[**gitlab_sync_export**](GitLabSyncApi.md#gitlab_sync_export) | **POST** /gitlab_syncs/{gitlab_sync_id}/export | Export from Phrase to GitLab
[**gitlab_sync_history**](GitLabSyncApi.md#gitlab_sync_history) | **GET** /gitlab_syncs/{gitlab_sync_id}/history | History of single Sync Setting
[**gitlab_sync_import**](GitLabSyncApi.md#gitlab_sync_import) | **POST** /gitlab_syncs/{gitlab_sync_id}/import | Import from GitLab to Phrase
[**gitlab_sync_list**](GitLabSyncApi.md#gitlab_sync_list) | **GET** /gitlab_syncs | List GitLab syncs
[**gitlab_sync_show**](GitLabSyncApi.md#gitlab_sync_show) | **GET** /gitlab_syncs/{id} | Get single Sync Setting
[**gitlab_sync_update**](GitLabSyncApi.md#gitlab_sync_update) | **PUT** /gitlab_syncs/{id} | Update single Sync Setting


# **gitlab_sync_delete**
> gitlab_sync_delete(id, x_phrase_app_otp=x_phrase_app_otp, account_id=account_id)

Delete single Sync Setting

Deletes a single GitLab Sync Setting.

### Example

* Basic Authentication (Basic):
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
    api_instance = phrase-api.GitLabSyncApi(api_client)
    id = 'id_example' # str | ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    account_id = 'abcd1234' # str | Account ID to specify the actual account the GitLab Sync should be created in. Required if the requesting user is a member of multiple accounts.

    try:
        # Delete single Sync Setting
        api_instance.gitlab_sync_delete(id, x_phrase_app_otp=x_phrase_app_otp, account_id=account_id)
    except ApiException as e:
        print("Exception when calling GitLabSyncApi->gitlab_sync_delete: %s\n" % e)
```

* Api Key Authentication (Token):
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
    api_instance = phrase-api.GitLabSyncApi(api_client)
    id = 'id_example' # str | ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    account_id = 'abcd1234' # str | Account ID to specify the actual account the GitLab Sync should be created in. Required if the requesting user is a member of multiple accounts.

    try:
        # Delete single Sync Setting
        api_instance.gitlab_sync_delete(id, x_phrase_app_otp=x_phrase_app_otp, account_id=account_id)
    except ApiException as e:
        print("Exception when calling GitLabSyncApi->gitlab_sync_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **account_id** | **str**| Account ID to specify the actual account the GitLab Sync should be created in. Required if the requesting user is a member of multiple accounts. | [optional] 

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

# **gitlab_sync_export**
> GitlabSyncExport gitlab_sync_export(gitlab_sync_id, gitlab_sync_export_parameters, x_phrase_app_otp=x_phrase_app_otp)

Export from Phrase to GitLab

Export translations from Phrase to GitLab according to the .phraseapp.yml file within the GitLab repository.

### Example

* Basic Authentication (Basic):
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
    api_instance = phrase-api.GitLabSyncApi(api_client)
    gitlab_sync_id = 'gitlab_sync_id_example' # str | Gitlab Sync ID (required)
    gitlab_sync_export_parameters = phrase-api.GitlabSyncExportParameters() # GitlabSyncExportParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Export from Phrase to GitLab
        api_response = api_instance.gitlab_sync_export(gitlab_sync_id, gitlab_sync_export_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GitLabSyncApi->gitlab_sync_export: %s\n" % e)
```

* Api Key Authentication (Token):
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
    api_instance = phrase-api.GitLabSyncApi(api_client)
    gitlab_sync_id = 'gitlab_sync_id_example' # str | Gitlab Sync ID (required)
    gitlab_sync_export_parameters = phrase-api.GitlabSyncExportParameters() # GitlabSyncExportParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Export from Phrase to GitLab
        api_response = api_instance.gitlab_sync_export(gitlab_sync_id, gitlab_sync_export_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GitLabSyncApi->gitlab_sync_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gitlab_sync_id** | **str**| Gitlab Sync ID | 
 **gitlab_sync_export_parameters** | [**GitlabSyncExportParameters**](GitlabSyncExportParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**GitlabSyncExport**](GitlabSyncExport.md)

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

# **gitlab_sync_history**
> list[GitlabSyncHistory] gitlab_sync_history(gitlab_sync_id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page, account_id=account_id)

History of single Sync Setting

List history for a single Sync Setting.

### Example

* Basic Authentication (Basic):
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
    api_instance = phrase-api.GitLabSyncApi(api_client)
    gitlab_sync_id = 'gitlab_sync_id_example' # str | Gitlab Sync ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    page = 1 # int | Page number
    per_page = 10 # int | allows you to specify a page size up to 100 items, 10 by default
    account_id = 'abcd1234' # str | Account ID to specify the actual account the GitLab Sync should be created in. Required if the requesting user is a member of multiple accounts.

    try:
        # History of single Sync Setting
        api_response = api_instance.gitlab_sync_history(gitlab_sync_id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page, account_id=account_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GitLabSyncApi->gitlab_sync_history: %s\n" % e)
```

* Api Key Authentication (Token):
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
    api_instance = phrase-api.GitLabSyncApi(api_client)
    gitlab_sync_id = 'gitlab_sync_id_example' # str | Gitlab Sync ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    page = 1 # int | Page number
    per_page = 10 # int | allows you to specify a page size up to 100 items, 10 by default
    account_id = 'abcd1234' # str | Account ID to specify the actual account the GitLab Sync should be created in. Required if the requesting user is a member of multiple accounts.

    try:
        # History of single Sync Setting
        api_response = api_instance.gitlab_sync_history(gitlab_sync_id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page, account_id=account_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GitLabSyncApi->gitlab_sync_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gitlab_sync_id** | **str**| Gitlab Sync ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| allows you to specify a page size up to 100 items, 10 by default | [optional] 
 **account_id** | **str**| Account ID to specify the actual account the GitLab Sync should be created in. Required if the requesting user is a member of multiple accounts. | [optional] 

### Return type

[**list[GitlabSyncHistory]**](GitlabSyncHistory.md)

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

# **gitlab_sync_import**
> list[Upload] gitlab_sync_import(gitlab_sync_id, gitlab_sync_import_parameters, x_phrase_app_otp=x_phrase_app_otp)

Import from GitLab to Phrase

Import translations from GitLab to Phrase according to the .phraseapp.yml file within the GitLab repository.

### Example

* Basic Authentication (Basic):
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
    api_instance = phrase-api.GitLabSyncApi(api_client)
    gitlab_sync_id = 'gitlab_sync_id_example' # str | Gitlab Sync ID (required)
    gitlab_sync_import_parameters = phrase-api.GitlabSyncImportParameters() # GitlabSyncImportParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Import from GitLab to Phrase
        api_response = api_instance.gitlab_sync_import(gitlab_sync_id, gitlab_sync_import_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GitLabSyncApi->gitlab_sync_import: %s\n" % e)
```

* Api Key Authentication (Token):
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
    api_instance = phrase-api.GitLabSyncApi(api_client)
    gitlab_sync_id = 'gitlab_sync_id_example' # str | Gitlab Sync ID (required)
    gitlab_sync_import_parameters = phrase-api.GitlabSyncImportParameters() # GitlabSyncImportParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Import from GitLab to Phrase
        api_response = api_instance.gitlab_sync_import(gitlab_sync_id, gitlab_sync_import_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GitLabSyncApi->gitlab_sync_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gitlab_sync_id** | **str**| Gitlab Sync ID | 
 **gitlab_sync_import_parameters** | [**GitlabSyncImportParameters**](GitlabSyncImportParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**list[Upload]**](Upload.md)

### Authorization

[Basic](../README.md#Basic), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  * Link -  <br>  |
**400** | Bad request |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**404** | Not Found |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**429** | Rate Limiting |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gitlab_sync_list**
> list[GitlabSync] gitlab_sync_list(x_phrase_app_otp=x_phrase_app_otp, account_id=account_id)

List GitLab syncs

List all GitLab Sync Settings for which synchronisation with Phrase and GitLab is activated.

### Example

* Basic Authentication (Basic):
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
    api_instance = phrase-api.GitLabSyncApi(api_client)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    account_id = 'abcd1234' # str | Account ID to specify the actual account the GitLab Sync should be created in. Required if the requesting user is a member of multiple accounts.

    try:
        # List GitLab syncs
        api_response = api_instance.gitlab_sync_list(x_phrase_app_otp=x_phrase_app_otp, account_id=account_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GitLabSyncApi->gitlab_sync_list: %s\n" % e)
```

* Api Key Authentication (Token):
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
    api_instance = phrase-api.GitLabSyncApi(api_client)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    account_id = 'abcd1234' # str | Account ID to specify the actual account the GitLab Sync should be created in. Required if the requesting user is a member of multiple accounts.

    try:
        # List GitLab syncs
        api_response = api_instance.gitlab_sync_list(x_phrase_app_otp=x_phrase_app_otp, account_id=account_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GitLabSyncApi->gitlab_sync_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **account_id** | **str**| Account ID to specify the actual account the GitLab Sync should be created in. Required if the requesting user is a member of multiple accounts. | [optional] 

### Return type

[**list[GitlabSync]**](GitlabSync.md)

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

# **gitlab_sync_show**
> GitlabSync gitlab_sync_show(id, x_phrase_app_otp=x_phrase_app_otp, account_id=account_id)

Get single Sync Setting

Shows a single GitLab Sync Setting.

### Example

* Basic Authentication (Basic):
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
    api_instance = phrase-api.GitLabSyncApi(api_client)
    id = 'id_example' # str | ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    account_id = 'abcd1234' # str | Account ID to specify the actual account the GitLab Sync should be created in. Required if the requesting user is a member of multiple accounts.

    try:
        # Get single Sync Setting
        api_response = api_instance.gitlab_sync_show(id, x_phrase_app_otp=x_phrase_app_otp, account_id=account_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GitLabSyncApi->gitlab_sync_show: %s\n" % e)
```

* Api Key Authentication (Token):
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
    api_instance = phrase-api.GitLabSyncApi(api_client)
    id = 'id_example' # str | ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    account_id = 'abcd1234' # str | Account ID to specify the actual account the GitLab Sync should be created in. Required if the requesting user is a member of multiple accounts.

    try:
        # Get single Sync Setting
        api_response = api_instance.gitlab_sync_show(id, x_phrase_app_otp=x_phrase_app_otp, account_id=account_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GitLabSyncApi->gitlab_sync_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **account_id** | **str**| Account ID to specify the actual account the GitLab Sync should be created in. Required if the requesting user is a member of multiple accounts. | [optional] 

### Return type

[**GitlabSync**](GitlabSync.md)

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

# **gitlab_sync_update**
> GitlabSync gitlab_sync_update(id, x_phrase_app_otp=x_phrase_app_otp, account_id=account_id, phrase_project_code=phrase_project_code, gitlab_project_id=gitlab_project_id, gitlab_branch_name=gitlab_branch_name)

Update single Sync Setting

Updates a single GitLab Sync Setting.

### Example

* Basic Authentication (Basic):
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
    api_instance = phrase-api.GitLabSyncApi(api_client)
    id = 'id_example' # str | ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    account_id = 'abcd1234' # str | Account ID to specify the actual account the GitLab Sync should be created in. Required if the requesting user is a member of multiple accounts.
    phrase_project_code = '3456abcd' # str | Code of the related Phrase Project.
    gitlab_project_id = 12345 # int | ID of the related GitLab Project.
    gitlab_branch_name = 'feature-development' # str | Name of the GitLab Branch.

    try:
        # Update single Sync Setting
        api_response = api_instance.gitlab_sync_update(id, x_phrase_app_otp=x_phrase_app_otp, account_id=account_id, phrase_project_code=phrase_project_code, gitlab_project_id=gitlab_project_id, gitlab_branch_name=gitlab_branch_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GitLabSyncApi->gitlab_sync_update: %s\n" % e)
```

* Api Key Authentication (Token):
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
    api_instance = phrase-api.GitLabSyncApi(api_client)
    id = 'id_example' # str | ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    account_id = 'abcd1234' # str | Account ID to specify the actual account the GitLab Sync should be created in. Required if the requesting user is a member of multiple accounts.
    phrase_project_code = '3456abcd' # str | Code of the related Phrase Project.
    gitlab_project_id = 12345 # int | ID of the related GitLab Project.
    gitlab_branch_name = 'feature-development' # str | Name of the GitLab Branch.

    try:
        # Update single Sync Setting
        api_response = api_instance.gitlab_sync_update(id, x_phrase_app_otp=x_phrase_app_otp, account_id=account_id, phrase_project_code=phrase_project_code, gitlab_project_id=gitlab_project_id, gitlab_branch_name=gitlab_branch_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GitLabSyncApi->gitlab_sync_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **account_id** | **str**| Account ID to specify the actual account the GitLab Sync should be created in. Required if the requesting user is a member of multiple accounts. | [optional] 
 **phrase_project_code** | **str**| Code of the related Phrase Project. | [optional] 
 **gitlab_project_id** | **int**| ID of the related GitLab Project. | [optional] 
 **gitlab_branch_name** | **str**| Name of the GitLab Branch. | [optional] 

### Return type

[**GitlabSync**](GitlabSync.md)

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


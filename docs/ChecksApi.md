# phrase_api.ChecksApi

All URIs are relative to *https://api.phrase.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_issue_dismiss**](ChecksApi.md#check_issue_dismiss) | **PATCH** /projects/{project_id}/checks/issues/{id}/dismiss | Dismiss a check issue
[**check_issues_list**](ChecksApi.md#check_issues_list) | **GET** /projects/{project_id}/checks/issues | List check issues


# **check_issue_dismiss**
> CheckIssue check_issue_dismiss(project_id, id, x_phrase_app_otp=x_phrase_app_otp)

Dismiss a check issue

**Note:** The Checks API is still in development and might change in subsequent releases.  Mark a check issue as dismissed so it no longer appears on the list of active check issues.

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
    api_instance = phrase_api.ChecksApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    id = 'id_example' # str | Check Issue ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Dismiss a check issue
        api_response = api_instance.check_issue_dismiss(project_id, id, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChecksApi->check_issue_dismiss: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **id** | **str**| Check Issue ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**CheckIssue**](CheckIssue.md)

### Authorization

[Basic](../README.md#Basic), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**400** | Bad request. The request could not be parsed or a parameter failed validation. Verify the request body, the content type, and the parameter types, then retry. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**401** | Unauthorized. Authentication failed because the access token is missing, expired, or invalid. Supply a valid access token and retry. |  -  |
**403** | Forbidden. The credentials are valid but not permitted for this request: the access token may lack the required scope, the user may lack permission on the resource, or the account plan may not include the feature. Use a token with the required scope on an account and user that hold the necessary permissions. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**404** | Not found. The requested resource does not exist or is not visible to the authenticated user. Verify the identifiers in the request path and that the token has access to them, then retry. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**422** | Unprocessable entity. The request was well-formed but failed validation. The response body lists each offending field in the &#x60;errors&#x60; array, with its resource, field, and a human-readable message. Correct the listed fields and retry. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**429** | Too many requests. The rate limit has been exceeded. Wait until the time indicated by the &#x60;X-Rate-Limit-Reset&#x60; response header before retrying. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_issues_list**
> List[CheckIssue] check_issues_list(project_id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page, state=state, locale_ids=locale_ids, check_names=check_names, created_since=created_since)

List check issues

**Note:** The Checks API is still in development and might change in subsequent releases.  List check issues for the given project. Results can be filtered by locale, check name, and state.

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
    api_instance = phrase_api.ChecksApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    page = 1 # int | Page number
    per_page = 25 # int | Limit on the number of objects to be returned, between 1 and 100. 25 by default
    state = 'active' # str | Filter by state of the check issue. Can be one of: `active`, `solved`, `dismissed`, `all`. Defaults to `active`. (default to 'active')
    locale_ids = ['[\"abcd1234cdef1234abcd1234cdef1234\"]'] # List[str] | Filter by one or more locale IDs.
    check_names = ['[\"translation_placeholder_usage\"]'] # List[str] | Filter by one or more check names. Valid values are:  - `translation_content_length` — the translation exceeds the maximum character limit configured for the key. - `translation_placeholder_usage` — the translation is missing placeholders present in the source, or contains unexpected ones. - `translation_glossary_usage` — the translation does not follow the glossary term translations.
    created_since = '2026-01-01T12:00:00Z' # str | Return only check issues created on or after this ISO 8601 datetime. Returns 400 if the value is not a valid date-time.

    try:
        # List check issues
        api_response = api_instance.check_issues_list(project_id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page, state=state, locale_ids=locale_ids, check_names=check_names, created_since=created_since)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChecksApi->check_issues_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Limit on the number of objects to be returned, between 1 and 100. 25 by default | [optional] 
 **state** | **str**| Filter by state of the check issue. Can be one of: &#x60;active&#x60;, &#x60;solved&#x60;, &#x60;dismissed&#x60;, &#x60;all&#x60;. Defaults to &#x60;active&#x60;. | [optional] [default to &#39;active&#39;]
 **locale_ids** | [**List[str]**](str.md)| Filter by one or more locale IDs. | [optional] 
 **check_names** | [**List[str]**](str.md)| Filter by one or more check names. Valid values are:  - &#x60;translation_content_length&#x60; — the translation exceeds the maximum character limit configured for the key. - &#x60;translation_placeholder_usage&#x60; — the translation is missing placeholders present in the source, or contains unexpected ones. - &#x60;translation_glossary_usage&#x60; — the translation does not follow the glossary term translations. | [optional] 
 **created_since** | **str**| Return only check issues created on or after this ISO 8601 datetime. Returns 400 if the value is not a valid date-time. | [optional] 

### Return type

[**List[CheckIssue]**](CheckIssue.md)

### Authorization

[Basic](../README.md#Basic), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  * Link -  <br>  * Pagination -  <br>  |
**400** | Bad request. The request could not be parsed or a parameter failed validation. Verify the request body, the content type, and the parameter types, then retry. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**401** | Unauthorized. Authentication failed because the access token is missing, expired, or invalid. Supply a valid access token and retry. |  -  |
**403** | Forbidden. The credentials are valid but not permitted for this request: the access token may lack the required scope, the user may lack permission on the resource, or the account plan may not include the feature. Use a token with the required scope on an account and user that hold the necessary permissions. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**404** | Not found. The requested resource does not exist or is not visible to the authenticated user. Verify the identifiers in the request path and that the token has access to them, then retry. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**429** | Too many requests. The rate limit has been exceeded. Wait until the time indicated by the &#x60;X-Rate-Limit-Reset&#x60; response header before retrying. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


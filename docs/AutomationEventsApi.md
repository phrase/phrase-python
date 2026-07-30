# phrase_api.AutomationEventsApi

All URIs are relative to *https://api.phrase.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_automation_events_list**](AutomationEventsApi.md#account_automation_events_list) | **GET** /accounts/{account_id}/automation_events | List automation events for an account
[**automation_events_list**](AutomationEventsApi.md#automation_events_list) | **GET** /accounts/{account_id}/automations/{automation_id}/events | List events for an automation


# **account_automation_events_list**
> List[AutomationEvent] account_automation_events_list(account_id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page, automation_id=automation_id, state=state, triggered_by=triggered_by, project_id=project_id, project_ids=project_ids, created_after=created_after, created_before=created_before)

List automation events for an account

Returns the run history across all automations in the account, newest-first.  Use `automation_id` to narrow results to a single automation. Use `project_id` or `project_ids` to narrow by project.  For feature availability, see [Jobs (Strings)](https://support.phrase.com/hc/en-us/articles/5784100517788-Jobs-Strings). 

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
    api_instance = phrase_api.AutomationEventsApi(api_client)
    account_id = 'account_id_example' # str | Account ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    page = 1 # int | Page number
    per_page = 25 # int | Limit on the number of objects to be returned, between 1 and 100. 25 by default
    automation_id = 'automation_id_example' # str | Filter events to a single automation by its ID.
    state = 'state_example' # str | Filter events by outcome state. Unrecognized values are ignored.
    triggered_by = 'triggered_by_example' # str | Filter events by what triggered the automation run. Unrecognized values are ignored.
    project_id = 'project_id_example' # str | Filter events by project ID. Accepts a single ID or a comma-separated list of IDs.
    project_ids = ['project_ids_example'] # List[str] | Filter events by one or more project IDs.
    created_after = '2023-01-01T00:00:00Z' # str | Return only events created after this ISO 8601 timestamp. Returns 400 if the value is not a valid date-time.
    created_before = '2023-01-01T00:00:00Z' # str | Return only events created before this ISO 8601 timestamp. Returns 400 if the value is not a valid date-time.

    try:
        # List automation events for an account
        api_response = api_instance.account_automation_events_list(account_id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page, automation_id=automation_id, state=state, triggered_by=triggered_by, project_id=project_id, project_ids=project_ids, created_after=created_after, created_before=created_before)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutomationEventsApi->account_automation_events_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Limit on the number of objects to be returned, between 1 and 100. 25 by default | [optional] 
 **automation_id** | **str**| Filter events to a single automation by its ID. | [optional] 
 **state** | **str**| Filter events by outcome state. Unrecognized values are ignored. | [optional] 
 **triggered_by** | **str**| Filter events by what triggered the automation run. Unrecognized values are ignored. | [optional] 
 **project_id** | **str**| Filter events by project ID. Accepts a single ID or a comma-separated list of IDs. | [optional] 
 **project_ids** | [**List[str]**](str.md)| Filter events by one or more project IDs. | [optional] 
 **created_after** | **str**| Return only events created after this ISO 8601 timestamp. Returns 400 if the value is not a valid date-time. | [optional] 
 **created_before** | **str**| Return only events created before this ISO 8601 timestamp. Returns 400 if the value is not a valid date-time. | [optional] 

### Return type

[**List[AutomationEvent]**](AutomationEvent.md)

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
**429** | Too many requests. The rate limit has been exceeded. Wait until the time indicated by the &#x60;X-Rate-Limit-Reset&#x60; response header before retrying. |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **automation_events_list**
> List[AutomationEvent] automation_events_list(account_id, id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page, state=state, triggered_by=triggered_by, project_id=project_id, project_ids=project_ids, created_after=created_after, created_before=created_before)

List events for an automation

Returns the run history for a specific automation, newest-first.  For feature availability, see [Jobs (Strings)](https://support.phrase.com/hc/en-us/articles/5784100517788-Jobs-Strings). 

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
    api_instance = phrase_api.AutomationEventsApi(api_client)
    account_id = 'account_id_example' # str | Account ID (required)
    id = 'id_example' # str | ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    page = 1 # int | Page number
    per_page = 25 # int | Limit on the number of objects to be returned, between 1 and 100. 25 by default
    state = 'state_example' # str | Filter events by outcome state. Unrecognized values are ignored.
    triggered_by = 'triggered_by_example' # str | Filter events by what triggered the automation run. Unrecognized values are ignored.
    project_id = 'project_id_example' # str | Filter events by project ID. Accepts a single ID or a comma-separated list of IDs.
    project_ids = ['project_ids_example'] # List[str] | Filter events by one or more project IDs.
    created_after = '2023-01-01T00:00:00Z' # str | Return only events created after this ISO 8601 timestamp. Returns 400 if the value is not a valid date-time.
    created_before = '2023-01-01T00:00:00Z' # str | Return only events created before this ISO 8601 timestamp. Returns 400 if the value is not a valid date-time.

    try:
        # List events for an automation
        api_response = api_instance.automation_events_list(account_id, id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page, state=state, triggered_by=triggered_by, project_id=project_id, project_ids=project_ids, created_after=created_after, created_before=created_before)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutomationEventsApi->automation_events_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID | 
 **id** | **str**| ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Limit on the number of objects to be returned, between 1 and 100. 25 by default | [optional] 
 **state** | **str**| Filter events by outcome state. Unrecognized values are ignored. | [optional] 
 **triggered_by** | **str**| Filter events by what triggered the automation run. Unrecognized values are ignored. | [optional] 
 **project_id** | **str**| Filter events by project ID. Accepts a single ID or a comma-separated list of IDs. | [optional] 
 **project_ids** | [**List[str]**](str.md)| Filter events by one or more project IDs. | [optional] 
 **created_after** | **str**| Return only events created after this ISO 8601 timestamp. Returns 400 if the value is not a valid date-time. | [optional] 
 **created_before** | **str**| Return only events created before this ISO 8601 timestamp. Returns 400 if the value is not a valid date-time. | [optional] 

### Return type

[**List[AutomationEvent]**](AutomationEvent.md)

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


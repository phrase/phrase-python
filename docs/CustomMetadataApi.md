# phrase_api.CustomMetadataApi

All URIs are relative to *https://api.phrase.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_metadata_properties_delete**](CustomMetadataApi.md#custom_metadata_properties_delete) | **DELETE** /accounts/{account_id}/custom_metadata/properties/{id} | Destroy property
[**custom_metadata_properties_list**](CustomMetadataApi.md#custom_metadata_properties_list) | **GET** /accounts/{account_id}/custom_metadata/properties | List properties
[**custom_metadata_property_create**](CustomMetadataApi.md#custom_metadata_property_create) | **POST** /accounts/{account_id}/custom_metadata/properties | Create a property
[**custom_metadata_property_show**](CustomMetadataApi.md#custom_metadata_property_show) | **GET** /accounts/{account_id}/custom_metadata/properties/{id} | Get a single property
[**custom_metadata_property_update**](CustomMetadataApi.md#custom_metadata_property_update) | **PATCH** /accounts/{account_id}/custom_metadata/properties/{id} | Update a property


# **custom_metadata_properties_delete**
> custom_metadata_properties_delete(account_id, id, x_phrase_app_otp=x_phrase_app_otp)

Destroy property

Destroy a custom metadata property of an account.  This endpoint is only available to accounts with advanced plans or above. 

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
    api_instance = phrase_api.CustomMetadataApi(api_client)
    account_id = 'account_id_example' # str | Account ID (required)
    id = 'id_example' # str | ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Destroy property
        api_instance.custom_metadata_properties_delete(account_id, id, x_phrase_app_otp=x_phrase_app_otp)
    except ApiException as e:
        print("Exception when calling CustomMetadataApi->custom_metadata_properties_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID | 
 **id** | **str**| ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

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

# **custom_metadata_properties_list**
> List[CustomMetadataProperty] custom_metadata_properties_list(account_id, x_phrase_app_otp=x_phrase_app_otp, data_type=data_type, project_id=project_id, page=page, per_page=per_page, sort=sort, order=order)

List properties

List all custom metadata properties for an account.  This endpoint is only available to accounts with advanced plans or above. 

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
    api_instance = phrase_api.CustomMetadataApi(api_client)
    account_id = 'account_id_example' # str | Account ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    data_type = phrase_api.CustomMetadataDataType() # CustomMetadataDataType | Data Type of Custom Metadata Property
    project_id = 'abcd1234cdef1234abcd1234cdef1234' # str | id of project that the properties belong to
    page = 1 # int | Page number
    per_page = 25 # int | Limit on the number of objects to be returned, between 1 and 100. 25 by default
    sort = 'updated_at' # str | Sort criteria. Can be one of: name, data_type, created_at.
    order = 'desc' # str | Order direction. Can be one of: asc, desc.

    try:
        # List properties
        api_response = api_instance.custom_metadata_properties_list(account_id, x_phrase_app_otp=x_phrase_app_otp, data_type=data_type, project_id=project_id, page=page, per_page=per_page, sort=sort, order=order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CustomMetadataApi->custom_metadata_properties_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **data_type** | [**CustomMetadataDataType**](.md)| Data Type of Custom Metadata Property | [optional] 
 **project_id** | **str**| id of project that the properties belong to | [optional] 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Limit on the number of objects to be returned, between 1 and 100. 25 by default | [optional] 
 **sort** | **str**| Sort criteria. Can be one of: name, data_type, created_at. | [optional] 
 **order** | **str**| Order direction. Can be one of: asc, desc. | [optional] 

### Return type

[**List[CustomMetadataProperty]**](CustomMetadataProperty.md)

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

# **custom_metadata_property_create**
> CustomMetadataProperty custom_metadata_property_create(account_id, name, data_type, x_phrase_app_otp=x_phrase_app_otp, description=description, project_ids=project_ids, value_options=value_options)

Create a property

Create a new custom metadata property.

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
    api_instance = phrase_api.CustomMetadataApi(api_client)
    account_id = 'account_id_example' # str | Account ID (required)
    name = '[\"Fruit\"]' # str | name of the property (required)
    data_type = phrase_api.CustomMetadataDataType() # CustomMetadataDataType | Data Type of Custom Metadata Property (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    description = '[\"A healthy snack for all ages\"]' # str | description of property
    project_ids = ['[\"abcd1234cdef1234abcd1234cdef1234\"]'] # List[str] | ids of projects that the property belongs to
    value_options = ['[\"Apple\",\"Banana\",\"Coconut\"]'] # List[str] | value options of property (only applies to single or multi select properties)

    try:
        # Create a property
        api_response = api_instance.custom_metadata_property_create(account_id, name, data_type, x_phrase_app_otp=x_phrase_app_otp, description=description, project_ids=project_ids, value_options=value_options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CustomMetadataApi->custom_metadata_property_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID | 
 **name** | **str**| name of the property | 
 **data_type** | [**CustomMetadataDataType**](.md)| Data Type of Custom Metadata Property | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **description** | **str**| description of property | [optional] 
 **project_ids** | [**List[str]**](str.md)| ids of projects that the property belongs to | [optional] 
 **value_options** | [**List[str]**](str.md)| value options of property (only applies to single or multi select properties) | [optional] 

### Return type

[**CustomMetadataProperty**](CustomMetadataProperty.md)

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
**422** | Unprocessable entity |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**429** | Rate Limiting |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_metadata_property_show**
> CustomMetadataProperty custom_metadata_property_show(account_id, id, x_phrase_app_otp=x_phrase_app_otp)

Get a single property

Get details of a single custom property.

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
    api_instance = phrase_api.CustomMetadataApi(api_client)
    account_id = 'account_id_example' # str | Account ID (required)
    id = 'id_example' # str | ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Get a single property
        api_response = api_instance.custom_metadata_property_show(account_id, id, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CustomMetadataApi->custom_metadata_property_show: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID | 
 **id** | **str**| ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**CustomMetadataProperty**](CustomMetadataProperty.md)

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

# **custom_metadata_property_update**
> CustomMetadataProperty custom_metadata_property_update(account_id, id, x_phrase_app_otp=x_phrase_app_otp, name=name, description=description, project_ids=project_ids, value_options=value_options)

Update a property

Update an existing custom metadata property.

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
    api_instance = phrase_api.CustomMetadataApi(api_client)
    account_id = 'account_id_example' # str | Account ID (required)
    id = 'id_example' # str | ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    name = '[\"Fruit\"]' # str | name of the property
    description = '[\"A healthy snack for all ages\"]' # str | description of property
    project_ids = ['[\"abcd1234cdef1234abcd1234cdef1234\"]'] # List[str] | ids of projects that the property belongs to
    value_options = ['[\"Apple\",\"Banana\",\"Coconut\"]'] # List[str] | value options of property (only applies to single or multi select properties)

    try:
        # Update a property
        api_response = api_instance.custom_metadata_property_update(account_id, id, x_phrase_app_otp=x_phrase_app_otp, name=name, description=description, project_ids=project_ids, value_options=value_options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CustomMetadataApi->custom_metadata_property_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID | 
 **id** | **str**| ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **name** | **str**| name of the property | [optional] 
 **description** | **str**| description of property | [optional] 
 **project_ids** | [**List[str]**](str.md)| ids of projects that the property belongs to | [optional] 
 **value_options** | [**List[str]**](str.md)| value options of property (only applies to single or multi select properties) | [optional] 

### Return type

[**CustomMetadataProperty**](CustomMetadataProperty.md)

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


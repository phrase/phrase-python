# phrase_api.TranslationsApi

All URIs are relative to *https://api.phrase.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**translation_create**](TranslationsApi.md#translation_create) | **POST** /projects/{project_id}/translations | Create a translation
[**translation_exclude**](TranslationsApi.md#translation_exclude) | **PATCH** /projects/{project_id}/translations/{id}/exclude | Exclude a translation from export
[**translation_include**](TranslationsApi.md#translation_include) | **PATCH** /projects/{project_id}/translations/{id}/include | Include a translation
[**translation_review**](TranslationsApi.md#translation_review) | **PATCH** /projects/{project_id}/translations/{id}/review | Review a translation
[**translation_show**](TranslationsApi.md#translation_show) | **GET** /projects/{project_id}/translations/{id} | Get a single translation
[**translation_unverify**](TranslationsApi.md#translation_unverify) | **PATCH** /projects/{project_id}/translations/{id}/unverify | Mark a translation as unverified
[**translation_update**](TranslationsApi.md#translation_update) | **PATCH** /projects/{project_id}/translations/{id} | Update a translation
[**translation_verify**](TranslationsApi.md#translation_verify) | **PATCH** /projects/{project_id}/translations/{id}/verify | Verify a translation
[**translations_by_key**](TranslationsApi.md#translations_by_key) | **GET** /projects/{project_id}/keys/{key_id}/translations | List translations by key
[**translations_by_locale**](TranslationsApi.md#translations_by_locale) | **GET** /projects/{project_id}/locales/{locale_id}/translations | List translations by locale
[**translations_exclude_collection**](TranslationsApi.md#translations_exclude_collection) | **PATCH** /projects/{project_id}/translations/exclude | Exclude translations by query
[**translations_include_collection**](TranslationsApi.md#translations_include_collection) | **PATCH** /projects/{project_id}/translations/include | Include translations by query
[**translations_list**](TranslationsApi.md#translations_list) | **GET** /projects/{project_id}/translations | List all translations
[**translations_review_collection**](TranslationsApi.md#translations_review_collection) | **PATCH** /projects/{project_id}/translations/review | Review translations selected by query
[**translations_search**](TranslationsApi.md#translations_search) | **POST** /projects/{project_id}/translations/search | Search translations
[**translations_unverify_collection**](TranslationsApi.md#translations_unverify_collection) | **PATCH** /projects/{project_id}/translations/unverify | Unverify translations by query
[**translations_verify_collection**](TranslationsApi.md#translations_verify_collection) | **PATCH** /projects/{project_id}/translations/verify | Verify translations by query


# **translation_create**
> TranslationDetails translation_create(project_id, translation_create_parameters, x_phrase_app_otp=x_phrase_app_otp)

Create a translation

Create a translation.

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
    api_instance = phrase_api.TranslationsApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    translation_create_parameters = phrase_api.TranslationCreateParameters() # TranslationCreateParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Create a translation
        api_response = api_instance.translation_create(project_id, translation_create_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TranslationsApi->translation_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **translation_create_parameters** | [**TranslationCreateParameters**](TranslationCreateParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**TranslationDetails**](TranslationDetails.md)

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

# **translation_exclude**
> TranslationDetails translation_exclude(project_id, id, translation_exclude_parameters, x_phrase_app_otp=x_phrase_app_otp)

Exclude a translation from export

Set exclude from export flag on an existing translation.

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
    api_instance = phrase_api.TranslationsApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    id = 'id_example' # str | ID (required)
    translation_exclude_parameters = phrase_api.TranslationExcludeParameters() # TranslationExcludeParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Exclude a translation from export
        api_response = api_instance.translation_exclude(project_id, id, translation_exclude_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TranslationsApi->translation_exclude: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **id** | **str**| ID | 
 **translation_exclude_parameters** | [**TranslationExcludeParameters**](TranslationExcludeParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**TranslationDetails**](TranslationDetails.md)

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

# **translation_include**
> TranslationDetails translation_include(project_id, id, translation_include_parameters, x_phrase_app_otp=x_phrase_app_otp)

Include a translation

Remove exclude from export flag from an existing translation.

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
    api_instance = phrase_api.TranslationsApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    id = 'id_example' # str | ID (required)
    translation_include_parameters = phrase_api.TranslationIncludeParameters() # TranslationIncludeParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Include a translation
        api_response = api_instance.translation_include(project_id, id, translation_include_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TranslationsApi->translation_include: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **id** | **str**| ID | 
 **translation_include_parameters** | [**TranslationIncludeParameters**](TranslationIncludeParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**TranslationDetails**](TranslationDetails.md)

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

# **translation_review**
> TranslationDetails translation_review(project_id, id, translation_review_parameters, x_phrase_app_otp=x_phrase_app_otp)

Review a translation

Mark an existing translation as reviewed.

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
    api_instance = phrase_api.TranslationsApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    id = 'id_example' # str | ID (required)
    translation_review_parameters = phrase_api.TranslationReviewParameters() # TranslationReviewParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Review a translation
        api_response = api_instance.translation_review(project_id, id, translation_review_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TranslationsApi->translation_review: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **id** | **str**| ID | 
 **translation_review_parameters** | [**TranslationReviewParameters**](TranslationReviewParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**TranslationDetails**](TranslationDetails.md)

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

# **translation_show**
> TranslationDetails translation_show(project_id, id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)

Get a single translation

Get details on a single translation.

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
    api_instance = phrase_api.TranslationsApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    id = 'id_example' # str | ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    branch = 'my-feature-branch' # str | specify the branch to use

    try:
        # Get a single translation
        api_response = api_instance.translation_show(project_id, id, x_phrase_app_otp=x_phrase_app_otp, branch=branch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TranslationsApi->translation_show: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **id** | **str**| ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **branch** | **str**| specify the branch to use | [optional] 

### Return type

[**TranslationDetails**](TranslationDetails.md)

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

# **translation_unverify**
> TranslationDetails translation_unverify(project_id, id, translation_unverify_parameters, x_phrase_app_otp=x_phrase_app_otp)

Mark a translation as unverified

Mark an existing translation as unverified.

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
    api_instance = phrase_api.TranslationsApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    id = 'id_example' # str | ID (required)
    translation_unverify_parameters = phrase_api.TranslationUnverifyParameters() # TranslationUnverifyParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Mark a translation as unverified
        api_response = api_instance.translation_unverify(project_id, id, translation_unverify_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TranslationsApi->translation_unverify: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **id** | **str**| ID | 
 **translation_unverify_parameters** | [**TranslationUnverifyParameters**](TranslationUnverifyParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**TranslationDetails**](TranslationDetails.md)

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

# **translation_update**
> TranslationDetails translation_update(project_id, id, translation_update_parameters, x_phrase_app_otp=x_phrase_app_otp)

Update a translation

Update an existing translation.

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
    api_instance = phrase_api.TranslationsApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    id = 'id_example' # str | ID (required)
    translation_update_parameters = phrase_api.TranslationUpdateParameters() # TranslationUpdateParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Update a translation
        api_response = api_instance.translation_update(project_id, id, translation_update_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TranslationsApi->translation_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **id** | **str**| ID | 
 **translation_update_parameters** | [**TranslationUpdateParameters**](TranslationUpdateParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**TranslationDetails**](TranslationDetails.md)

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

# **translation_verify**
> TranslationDetails translation_verify(project_id, id, translation_verify_parameters, x_phrase_app_otp=x_phrase_app_otp)

Verify a translation

Verify an existing translation.

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
    api_instance = phrase_api.TranslationsApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    id = 'id_example' # str | ID (required)
    translation_verify_parameters = phrase_api.TranslationVerifyParameters() # TranslationVerifyParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Verify a translation
        api_response = api_instance.translation_verify(project_id, id, translation_verify_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TranslationsApi->translation_verify: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **id** | **str**| ID | 
 **translation_verify_parameters** | [**TranslationVerifyParameters**](TranslationVerifyParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**TranslationDetails**](TranslationDetails.md)

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

# **translations_by_key**
> List[Translation] translations_by_key(project_id, key_id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page, branch=branch, sort=sort, order=order, q=q)

List translations by key

List translations for a specific key.

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
    api_instance = phrase_api.TranslationsApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    key_id = 'key_id_example' # str | Translation Key ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    page = 1 # int | Page number
    per_page = 25 # int | Limit on the number of objects to be returned, between 1 and 100. 25 by default
    branch = 'my-feature-branch' # str | specify the branch to use
    sort = 'updated_at' # str | Sort criteria. Can be one of: key_name, created_at, updated_at.
    order = 'desc' # str | Order direction. Can be one of: asc, desc.
    q = 'PhraseApp*%20unverified:true%20excluded:true%20tags:feature,center' # str | Specify a query to find translations by content (including wildcards).<br><br> The following qualifiers are supported in the query:<br> <ul>   <li><code>id:translation_id,...</code> for queries on a comma-separated list of ids</li>   <li><code>unverified:{true|false}</code> for verification status</li>   <li><code>tags:XYZ</code> for tags on the translation</li>   <li><code>excluded:{true|false}</code> for exclusion status</li>   <li><code>updated_at:{>=|<=}2013-02-21T00:00:00Z</code> for date range queries</li> </ul> Find more examples <a href=\"#overview--usage-examples\">here</a>. 

    try:
        # List translations by key
        api_response = api_instance.translations_by_key(project_id, key_id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page, branch=branch, sort=sort, order=order, q=q)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TranslationsApi->translations_by_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **key_id** | **str**| Translation Key ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Limit on the number of objects to be returned, between 1 and 100. 25 by default | [optional] 
 **branch** | **str**| specify the branch to use | [optional] 
 **sort** | **str**| Sort criteria. Can be one of: key_name, created_at, updated_at. | [optional] 
 **order** | **str**| Order direction. Can be one of: asc, desc. | [optional] 
 **q** | **str**| Specify a query to find translations by content (including wildcards).&lt;br&gt;&lt;br&gt; The following qualifiers are supported in the query:&lt;br&gt; &lt;ul&gt;   &lt;li&gt;&lt;code&gt;id:translation_id,...&lt;/code&gt; for queries on a comma-separated list of ids&lt;/li&gt;   &lt;li&gt;&lt;code&gt;unverified:{true|false}&lt;/code&gt; for verification status&lt;/li&gt;   &lt;li&gt;&lt;code&gt;tags:XYZ&lt;/code&gt; for tags on the translation&lt;/li&gt;   &lt;li&gt;&lt;code&gt;excluded:{true|false}&lt;/code&gt; for exclusion status&lt;/li&gt;   &lt;li&gt;&lt;code&gt;updated_at:{&gt;&#x3D;|&lt;&#x3D;}2013-02-21T00:00:00Z&lt;/code&gt; for date range queries&lt;/li&gt; &lt;/ul&gt; Find more examples &lt;a href&#x3D;\&quot;#overview--usage-examples\&quot;&gt;here&lt;/a&gt;.  | [optional] 

### Return type

[**List[Translation]**](Translation.md)

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

# **translations_by_locale**
> List[Translation] translations_by_locale(project_id, locale_id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page, branch=branch, sort=sort, order=order, q=q)

List translations by locale

List translations for a specific locale. If you want to download all translations for one locale we recommend to use the <code>locales#download</code> endpoint.

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
    api_instance = phrase_api.TranslationsApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    locale_id = 'locale_id_example' # str | Locale ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    page = 1 # int | Page number
    per_page = 25 # int | Limit on the number of objects to be returned, between 1 and 100. 25 by default
    branch = 'my-feature-branch' # str | specify the branch to use
    sort = 'updated_at' # str | Sort criteria. Can be one of: key_name, created_at, updated_at.
    order = 'desc' # str | Order direction. Can be one of: asc, desc.
    q = 'PhraseApp*%20unverified:true%20excluded:true%20tags:feature,center' # str | Specify a query to find translations by content (including wildcards).<br><br> <i>Note: Search is limited to 10000 results and may not include recently updated data (depending on the project size).</i><br> The following qualifiers are supported in the query:<br> <ul>   <li><code>id:translation_id,...</code> for queries on a comma-separated list of ids</li>   <li><code>unverified:{true|false}</code> for verification status</li>   <li><code>tags:XYZ</code> for tags on the translation</li>   <li><code>excluded:{true|false}</code> for exclusion status</li>   <li><code>updated_at:{>=|<=}2013-02-21T00:00:00Z</code> for date range queries</li> </ul> Find more examples <a href=\"#overview--usage-examples\">here</a>. 

    try:
        # List translations by locale
        api_response = api_instance.translations_by_locale(project_id, locale_id, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page, branch=branch, sort=sort, order=order, q=q)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TranslationsApi->translations_by_locale: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **locale_id** | **str**| Locale ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Limit on the number of objects to be returned, between 1 and 100. 25 by default | [optional] 
 **branch** | **str**| specify the branch to use | [optional] 
 **sort** | **str**| Sort criteria. Can be one of: key_name, created_at, updated_at. | [optional] 
 **order** | **str**| Order direction. Can be one of: asc, desc. | [optional] 
 **q** | **str**| Specify a query to find translations by content (including wildcards).&lt;br&gt;&lt;br&gt; &lt;i&gt;Note: Search is limited to 10000 results and may not include recently updated data (depending on the project size).&lt;/i&gt;&lt;br&gt; The following qualifiers are supported in the query:&lt;br&gt; &lt;ul&gt;   &lt;li&gt;&lt;code&gt;id:translation_id,...&lt;/code&gt; for queries on a comma-separated list of ids&lt;/li&gt;   &lt;li&gt;&lt;code&gt;unverified:{true|false}&lt;/code&gt; for verification status&lt;/li&gt;   &lt;li&gt;&lt;code&gt;tags:XYZ&lt;/code&gt; for tags on the translation&lt;/li&gt;   &lt;li&gt;&lt;code&gt;excluded:{true|false}&lt;/code&gt; for exclusion status&lt;/li&gt;   &lt;li&gt;&lt;code&gt;updated_at:{&gt;&#x3D;|&lt;&#x3D;}2013-02-21T00:00:00Z&lt;/code&gt; for date range queries&lt;/li&gt; &lt;/ul&gt; Find more examples &lt;a href&#x3D;\&quot;#overview--usage-examples\&quot;&gt;here&lt;/a&gt;.  | [optional] 

### Return type

[**List[Translation]**](Translation.md)

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

# **translations_exclude_collection**
> AffectedCount translations_exclude_collection(project_id, translations_exclude_parameters, x_phrase_app_otp=x_phrase_app_otp)

Exclude translations by query

Exclude translations matching query from locale export.

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
    api_instance = phrase_api.TranslationsApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    translations_exclude_parameters = phrase_api.TranslationsExcludeParameters() # TranslationsExcludeParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Exclude translations by query
        api_response = api_instance.translations_exclude_collection(project_id, translations_exclude_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TranslationsApi->translations_exclude_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **translations_exclude_parameters** | [**TranslationsExcludeParameters**](TranslationsExcludeParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**AffectedCount**](AffectedCount.md)

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

# **translations_include_collection**
> AffectedCount translations_include_collection(project_id, translations_include_parameters, x_phrase_app_otp=x_phrase_app_otp)

Include translations by query

Include translations matching query in locale export.

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
    api_instance = phrase_api.TranslationsApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    translations_include_parameters = phrase_api.TranslationsIncludeParameters() # TranslationsIncludeParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Include translations by query
        api_response = api_instance.translations_include_collection(project_id, translations_include_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TranslationsApi->translations_include_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **translations_include_parameters** | [**TranslationsIncludeParameters**](TranslationsIncludeParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**AffectedCount**](AffectedCount.md)

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

# **translations_list**
> List[Translation] translations_list(project_id, x_phrase_app_otp=x_phrase_app_otp, if_modified_since=if_modified_since, if_none_match=if_none_match, page=page, per_page=per_page, branch=branch, sort=sort, order=order, q=q)

List all translations

List translations for the given project. If you want to download all translations for one locale we recommend to use the <code>locales#download</code> endpoint.

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
    api_instance = phrase_api.TranslationsApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    if_modified_since = 'if_modified_since_example' # str | Last modified condition, see <a href=\"#overview--conditional-get-requests--http-caching\">Conditional GET requests / HTTP Caching</a> (optional)
    if_none_match = 'if_none_match_example' # str | ETag condition, see <a href=\"#overview--conditional-get-requests--http-caching\">Conditional GET requests / HTTP Caching</a> (optional)
    page = 1 # int | Page number
    per_page = 25 # int | Limit on the number of objects to be returned, between 1 and 100. 25 by default
    branch = 'my-feature-branch' # str | specify the branch to use
    sort = 'updated_at' # str | Sort criteria. Can be one of: key_name, created_at, updated_at.
    order = 'desc' # str | Order direction. Can be one of: asc, desc.
    q = 'PhraseApp*%20unverified:true%20excluded:true%20tags:feature,center' # str | Specify a query to find translations by content (including wildcards).<br><br> <i>Note: Search is limited to 10000 results and may not include recently updated data (depending on the project size).</i><br> The following qualifiers are supported in the query:<br> <ul>   <li><code>id:translation_id,...</code> for queries on a comma-separated list of ids</li>   <li><code>tags:XYZ</code> for tags on the translation</li>   <li><code>unverified:{true|false}</code> for verification status</li>   <li><code>excluded:{true|false}</code> for exclusion status</li>   <li><code>updated_at:{>=|<=}2013-02-21T00:00:00Z</code> for date range queries</li>   <li><code>reviewed_after:2013-02-21T00:00:00Z</code> for fetching translations that were reviewed after the given timestamp</li> </ul> Find more examples <a href=\"#overview--usage-examples\">here</a>. 

    try:
        # List all translations
        api_response = api_instance.translations_list(project_id, x_phrase_app_otp=x_phrase_app_otp, if_modified_since=if_modified_since, if_none_match=if_none_match, page=page, per_page=per_page, branch=branch, sort=sort, order=order, q=q)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TranslationsApi->translations_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **if_modified_since** | **str**| Last modified condition, see &lt;a href&#x3D;\&quot;#overview--conditional-get-requests--http-caching\&quot;&gt;Conditional GET requests / HTTP Caching&lt;/a&gt; (optional) | [optional] 
 **if_none_match** | **str**| ETag condition, see &lt;a href&#x3D;\&quot;#overview--conditional-get-requests--http-caching\&quot;&gt;Conditional GET requests / HTTP Caching&lt;/a&gt; (optional) | [optional] 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Limit on the number of objects to be returned, between 1 and 100. 25 by default | [optional] 
 **branch** | **str**| specify the branch to use | [optional] 
 **sort** | **str**| Sort criteria. Can be one of: key_name, created_at, updated_at. | [optional] 
 **order** | **str**| Order direction. Can be one of: asc, desc. | [optional] 
 **q** | **str**| Specify a query to find translations by content (including wildcards).&lt;br&gt;&lt;br&gt; &lt;i&gt;Note: Search is limited to 10000 results and may not include recently updated data (depending on the project size).&lt;/i&gt;&lt;br&gt; The following qualifiers are supported in the query:&lt;br&gt; &lt;ul&gt;   &lt;li&gt;&lt;code&gt;id:translation_id,...&lt;/code&gt; for queries on a comma-separated list of ids&lt;/li&gt;   &lt;li&gt;&lt;code&gt;tags:XYZ&lt;/code&gt; for tags on the translation&lt;/li&gt;   &lt;li&gt;&lt;code&gt;unverified:{true|false}&lt;/code&gt; for verification status&lt;/li&gt;   &lt;li&gt;&lt;code&gt;excluded:{true|false}&lt;/code&gt; for exclusion status&lt;/li&gt;   &lt;li&gt;&lt;code&gt;updated_at:{&gt;&#x3D;|&lt;&#x3D;}2013-02-21T00:00:00Z&lt;/code&gt; for date range queries&lt;/li&gt;   &lt;li&gt;&lt;code&gt;reviewed_after:2013-02-21T00:00:00Z&lt;/code&gt; for fetching translations that were reviewed after the given timestamp&lt;/li&gt; &lt;/ul&gt; Find more examples &lt;a href&#x3D;\&quot;#overview--usage-examples\&quot;&gt;here&lt;/a&gt;.  | [optional] 

### Return type

[**List[Translation]**](Translation.md)

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

# **translations_review_collection**
> AffectedCount translations_review_collection(project_id, translations_review_parameters, x_phrase_app_otp=x_phrase_app_otp)

Review translations selected by query

Review translations matching query.

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
    api_instance = phrase_api.TranslationsApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    translations_review_parameters = phrase_api.TranslationsReviewParameters() # TranslationsReviewParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Review translations selected by query
        api_response = api_instance.translations_review_collection(project_id, translations_review_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TranslationsApi->translations_review_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **translations_review_parameters** | [**TranslationsReviewParameters**](TranslationsReviewParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**AffectedCount**](AffectedCount.md)

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

# **translations_search**
> List[Translation] translations_search(project_id, translations_search_parameters, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page)

Search translations

Search translations for the given project. Provides the same search interface as <code>translations#index</code> but allows POST requests to avoid limitations imposed by GET requests. If you want to download all translations for one locale we recommend to use the <code>locales#download</code> endpoint.

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
    api_instance = phrase_api.TranslationsApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    translations_search_parameters = phrase_api.TranslationsSearchParameters() # TranslationsSearchParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)
    page = 1 # int | Page number
    per_page = 25 # int | Limit on the number of objects to be returned, between 1 and 100. 25 by default

    try:
        # Search translations
        api_response = api_instance.translations_search(project_id, translations_search_parameters, x_phrase_app_otp=x_phrase_app_otp, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TranslationsApi->translations_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **translations_search_parameters** | [**TranslationsSearchParameters**](TranslationsSearchParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Limit on the number of objects to be returned, between 1 and 100. 25 by default | [optional] 

### Return type

[**List[Translation]**](Translation.md)

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

# **translations_unverify_collection**
> AffectedCount translations_unverify_collection(project_id, translations_unverify_parameters, x_phrase_app_otp=x_phrase_app_otp)

Unverify translations by query

Mark translations matching query as unverified.

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
    api_instance = phrase_api.TranslationsApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    translations_unverify_parameters = phrase_api.TranslationsUnverifyParameters() # TranslationsUnverifyParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Unverify translations by query
        api_response = api_instance.translations_unverify_collection(project_id, translations_unverify_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TranslationsApi->translations_unverify_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **translations_unverify_parameters** | [**TranslationsUnverifyParameters**](TranslationsUnverifyParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**AffectedCount**](AffectedCount.md)

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

# **translations_verify_collection**
> AffectedCount translations_verify_collection(project_id, translations_verify_parameters, x_phrase_app_otp=x_phrase_app_otp)

Verify translations by query

Verify translations matching query.

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
    api_instance = phrase_api.TranslationsApi(api_client)
    project_id = 'project_id_example' # str | Project ID (required)
    translations_verify_parameters = phrase_api.TranslationsVerifyParameters() # TranslationsVerifyParameters |  (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Verify translations by query
        api_response = api_instance.translations_verify_collection(project_id, translations_verify_parameters, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TranslationsApi->translations_verify_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **translations_verify_parameters** | [**TranslationsVerifyParameters**](TranslationsVerifyParameters.md)|  | 
 **x_phrase_app_otp** | **str**| Two-Factor-Authentication token (optional) | [optional] 

### Return type

[**AffectedCount**](AffectedCount.md)

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


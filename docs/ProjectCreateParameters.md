# ProjectCreateParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the project | 
**main_format** | **str** | Main file format specified by its API Extension name. Used for locale downloads if no format is specified. For API Extension names of available file formats see [Format Guide](https://support.phrase.com/hc/en-us/sections/6111343326364) or our [Formats API Endpoint](/en/api/strings/formats/list-formats). | [optional] 
**media** | **str** | (Optional) Main technology stack used in the project. It affects for example the suggested placeholder style. Predefined values include: &#x60;Ruby&#x60;, &#x60;JavaScript&#x60;, &#x60;AngularJS&#x60;, &#x60;React&#x60;, &#x60;iOS&#x60;, &#x60;Android&#x60;, &#x60;Python&#x60;, &#x60;PHP&#x60;, &#x60;Java&#x60;, &#x60;Go&#x60;, &#x60;Windows Phone&#x60;, &#x60;Rails&#x60;, &#x60;Node.js&#x60;, &#x60;.NET&#x60;, &#x60;Django&#x60;, &#x60;Symfony&#x60;, &#x60;Yii Framework&#x60;, &#x60;Zend Framework&#x60;, &#x60;Apple App Store Description&#x60;, &#x60;Google Play Description&#x60;, but it can also take any other value. | [optional] 
**shares_translation_memory** | **bool** | Indicates whether the project should share the account&#39;s translation memory | [optional] 
**project_image** | **bytearray** | Image to identify the project | [optional] 
**remove_project_image** | **bool** | Indicates whether the project image should be deleted. | [optional] 
**account_id** | **str** | Account ID to specify the actual account the project should be created in. Required if the requesting user is a member of multiple accounts. | [optional] 
**point_of_contact** | **str** | (Optional) User ID of the point of contact for the project. | [optional] 
**source_project_id** | **str** | When a source project ID is given, a clone of that project will be created, including all locales, keys and translations as well as the main project settings if they are not defined otherwise through the params. | [optional] 
**workflow** | **str** | (Optional) Review Workflow. \&quot;simple\&quot; / \&quot;review\&quot;. [Read more](https://support.phrase.com/hc/en-us/articles/5784094755484) | [optional] 
**machine_translation_enabled** | **bool** | (Optional) Enable machine translation support in the project. Required for Pre-Translation | [optional] 
**enable_branching** | **bool** | (Optional) Enable branching in the project | [optional] 
**protect_master_branch** | **bool** | (Optional) Protect the master branch in project where branching is enabled | [optional] 
**enable_all_data_type_translation_keys_for_translators** | **bool** | (Optional) Otherwise, translators are not allowed to edit translations other than strings | [optional] 
**enable_icu_message_format** | **bool** | (Optional) We can validate and highlight your ICU messages. [Read more](https://support.phrase.com/hc/en-us/articles/5822319545116) | [optional] 
**zero_plural_form_enabled** | **bool** | (Optional) Displays the input fields for the &#39;ZERO&#39; plural form for every key as well although only some languages require the &#39;ZERO&#39; explicitly. | [optional] 
**autotranslate_enabled** | **bool** | (Optional) Autopilot, requires machine_translation_enabled. [Read more](https://support.phrase.com/hc/en-us/articles/5822187934364) | [optional] 
**autotranslate_check_new_translation_keys** | **bool** | (Optional) Requires autotranslate_enabled to be true | [optional] 
**autotranslate_check_new_uploads** | **bool** | (Optional) Requires autotranslate_enabled to be true | [optional] 
**autotranslate_check_new_locales** | **bool** | (Optional) Requires autotranslate_enabled to be true | [optional] 
**autotranslate_mark_as_unverified** | **bool** | (Optional) Requires autotranslate_enabled to be true | [optional] 
**autotranslate_use_machine_translation** | **bool** | (Optional) Requires autotranslate_enabled to be true | [optional] 
**autotranslate_use_translation_memory** | **bool** | (Optional) Requires autotranslate_enabled to be true | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



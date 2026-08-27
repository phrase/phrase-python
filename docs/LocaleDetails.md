# LocaleDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**default** | **bool** |  | [optional] 
**main** | **bool** |  | [optional] 
**rtl** | **bool** |  | [optional] 
**plural_forms** | **List[str]** |  | [optional] 
**ordinal_plural_forms** | **List[str]** |  | [optional] 
**source_locale** | [**LocalePreview**](LocalePreview.md) |  | [optional] 
**fallback_locale** | [**LocalePreview**](LocalePreview.md) |  | [optional] 
**language_ai_profile** | **str** |  | [optional] 
**unverify_new_translations** | **bool** | Indicates that new translations for this locale are marked as unverified. Only applies to locales using the basic verification workflow. Part of the [Advanced Workflows](https://support.phrase.com/hc/en-us/articles/5784094755484) feature. | [optional] 
**unverify_updated_translations** | **bool** | Indicates that updated translations for this locale are marked as unverified. Only applies to locales using the basic verification workflow. Part of the [Advanced Workflows](https://support.phrase.com/hc/en-us/articles/5784094755484) feature. | [optional] 
**unverify_on_source_changes** | **bool** | Indicates that translations for this locale are marked as unverified when the source language has been changed. | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**statistics** | [**LocaleStatistics**](LocaleStatistics.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



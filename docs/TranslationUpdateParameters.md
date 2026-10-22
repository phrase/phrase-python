# TranslationUpdateParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **str** | specify the branch to use | [optional] 
**content** | **str** | Translation content. Send an empty string or &#x60;null&#x60; to clear the translation&#39;s content; omit the field to leave it unchanged. The Phrase CLI drops &#x60;null&#x60; values before sending, so use an empty string there. | [optional] 
**plural_suffix** | **str** | Plural suffix. Can be one of: zero, one, two, few, many, other. Must be specified if the key associated to the translation is pluralized. | [optional] 
**unverified** | **bool** | Indicates whether translation is unverified. Part of the [Advanced Workflows](https://support.phrase.com/hc/en-us/articles/5784094755484) feature. | [optional] 
**excluded** | **bool** | Indicates whether translation is excluded. | [optional] 
**autotranslate** | **bool** | Indicates whether the translation should be auto-translated. Responses with status 422 if provided for translation within a non-default locale or the project does not have the Autopilot feature enabled. | [optional] 
**reviewed** | **bool** | When set to &#x60;true&#x60;, the translation will be marked as reviewed. | [optional] 
**minor_change** | **bool** | When &#x60;true&#x60;, the update is treated as a minor edit and does not trigger downstream re-verification on the linked locales&#39; translations.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



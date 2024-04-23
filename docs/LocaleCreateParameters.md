# LocaleCreateParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **str** | specify the branch to use | [optional] 
**name** | **str** | Locale name | 
**code** | **str** | Locale ISO code | 
**default** | **bool** | Indicates whether locale is the default locale. If set to true, the previous default locale the project is no longer the default locale. | [optional] 
**main** | **bool** | Indicates whether locale is a main locale. Main locales are part of the &lt;a href&#x3D;\&quot;https://support.phrase.com/hc/en-us/articles/5784094755484\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Verification System&lt;/a&gt; feature. | [optional] 
**rtl** | **bool** | Indicates whether locale is a RTL (Right-to-Left) locale. | [optional] 
**source_locale_id** | **str** | Source locale. Can be the name or id of the locale. Preferred is id. | [optional] 
**fallback_locale_id** | **str** | Fallback locale for empty translations. Can be a locale name or id. | [optional] 
**unverify_new_translations** | **bool** | Indicates that new translations for this locale should be marked as unverified. Part of the &lt;a href&#x3D;\&quot;https://support.phrase.com/hc/en-us/articles/5784094755484\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Advanced Workflows&lt;/a&gt; feature. | [optional] 
**unverify_updated_translations** | **bool** | Indicates that updated translations for this locale should be marked as unverified. Part of the &lt;a href&#x3D;\&quot;https://support.phrase.com/hc/en-us/articles/5784094755484\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Advanced Workflows&lt;/a&gt; feature. | [optional] 
**autotranslate** | **bool** | If set, translations for this locale will be fetched automatically, right after creation. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



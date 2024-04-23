# OrderCreateParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **str** | specify the branch to use | [optional] 
**name** | **str** | the name of the order, default name is: Translation order from &#39;current datetime&#39; | 
**lsp** | **str** | Name of the LSP that should process this order. Can be one of gengo, textmaster. | 
**source_locale_id** | **str** | Source locale for the order. Can be the name or id of the source locale. Preferred is id. | [optional] 
**target_locale_ids** | **List[str]** | List of target locales you want the source content translate to. Can be the name or id of the target locales. Preferred is id. | [optional] 
**translation_type** | **str** | Name of the quality level, availability depends on the LSP. Can be one of:  standard, pro (for orders processed by Gengo) and one of regular, premium, enterprise (for orders processed by TextMaster) | [optional] 
**tag** | **str** | Tag you want to order translations for. | [optional] 
**message** | **str** | Message that is displayed to the translators for description. | [optional] 
**styleguide_id** | **str** | Style guide for translators to be sent with the order. | [optional] 
**unverify_translations_upon_delivery** | **bool** | Unverify translations upon delivery. | [optional] 
**include_untranslated_keys** | **bool** | Order translations for keys with untranslated content in the selected target locales. | [optional] 
**include_unverified_translations** | **bool** | Order translations for keys with unverified content in the selected target locales. | [optional] 
**category** | **str** | Category to use (required for orders processed by TextMaster). | [optional] 
**quality** | **bool** | Extra proofreading option to ensure consistency in vocabulary and style. Only available for orders processed by TextMaster. | [optional] 
**priority** | **bool** | Indicates whether the priority option should be ordered which decreases turnaround time by 30%. Available only for orders processed by TextMaster. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



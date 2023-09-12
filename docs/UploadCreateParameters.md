# UploadCreateParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **str** | specify the branch to use | [optional] 
**file** | **file** | File to be imported | [optional] 
**file_format** | **str** | File format. Auto-detected when possible and not specified. | [optional] 
**locale_id** | **str** | Locale of the file&#39;s content. Can be the name or public id of the locale. Preferred is the public id. | [optional] 
**tags** | **str** | List of tags separated by comma to be associated with the new keys contained in the upload. | [optional] 
**update_translations** | **bool** | Indicates whether existing translations should be updated with the file content. | [optional] 
**update_descriptions** | **bool** | Existing key descriptions will be updated with the file content. Empty descriptions overwrite existing descriptions. | [optional] 
**convert_emoji** | **bool** | This option is obsolete. Providing the option will cause a bad request error. | [optional] 
**skip_upload_tags** | **bool** | Indicates whether the upload should not create upload tags. | [optional] 
**skip_unverification** | **bool** | Indicates whether the upload should unverify updated translations. | [optional] 
**file_encoding** | **str** | Enforces a specific encoding on the file contents. Valid options are \&quot;UTF-8\&quot;, \&quot;UTF-16\&quot; and \&quot;ISO-8859-1\&quot;. | [optional] 
**locale_mapping** | [**object**](.md) | Optional, format specific mapping between locale names and the columns the translations to those locales are contained in. | [optional] 
**format_options** | [**object**](.md) | Additional options available for specific formats. See our format guide for complete list. | [optional] 
**autotranslate** | **bool** | If set, translations for the uploaded language will be fetched automatically. | [optional] 
**mark_reviewed** | **bool** | Indicated whether the imported translations should be marked as reviewed. This setting is available if the review workflow is enabled for the project. | [optional] 
**tag_only_affected_keys** | **bool** | Indicates whether only keys affected (created or updated) by the upload should be tagged. The default is &#x60;false&#x60; | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



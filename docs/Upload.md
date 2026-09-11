# Upload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**filename** | **str** |  | [optional] 
**format** | **str** |  | [optional] 
**state** | **str** | Processing state of the upload: &#x60;initialized&#x60;, &#x60;processing&#x60;, &#x60;success&#x60;, or &#x60;error&#x60;. &#x60;error&#x60; means processing failed — for example the file could not be parsed, or a provided &#x60;file_format&#x60; didn&#39;t match the file&#39;s actual content. Poll this field until it leaves &#x60;initialized&#x60;/&#x60;processing&#x60; to get the final outcome.  | [optional] 
**error_message** | **str** | A user-facing message explaining why the upload failed, or &#x60;null&#x60; if the upload did not fail.  This message is intended for display only. Its wording may change at any time and it should not be parsed or relied upon programmatically.  | [optional] 
**tag** | **str** | Unique tag of the upload  | [optional] 
**tags** | **List[str]** | List of tags that were assigned to the uploaded keys  | [optional] 
**url** | **str** | The URL to the upload in Phrase Strings app.  | [optional] 
**user** | [**UserPreview**](.md) |  | [optional] 
**summary** | [**UploadSummary**](UploadSummary.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



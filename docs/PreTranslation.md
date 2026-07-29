# PreTranslation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**status** | **str** | Current execution state of the pre-translation job. Jobs start as &#x60;pending&#x60; while queued, transition to &#x60;running&#x60; while executing, and settle to &#x60;success&#x60; or &#x60;error&#x60;.  | [optional] 
**translatable_type** | **str** | Resource type that was pre-translated. | [optional] 
**translatable_id** | **str** | ID of the targeted resource (locale ID, job ID, key ID, or upload ID). | [optional] 
**error** | **str** | Error message. &#x60;null&#x60; unless the job&#39;s status is &#x60;error&#x60;. | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# JobDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**briefing** | **str** |  | [optional] 
**due_date** | **datetime** |  | [optional] 
**state** | **str** |  | [optional] 
**ticket_url** | **str** |  | [optional] 
**project** | [**ProjectShort**](ProjectShort.md) |  | [optional] 
**branch** | [**BranchName**](BranchName.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**automation_id** | **str** | The ID of the automation that created this job, or null if the job was created manually. | [optional] 
**job_template_id** | **str** | The ID of the job template this job was created from, or null if no template was used. | [optional] 
**owner** | [**UserPreview**](UserPreview.md) |  | [optional] 
**job_tag_name** | **str** |  | [optional] 
**source_translations_updated_at** | **datetime** |  | [optional] 
**source_locale** | [**LocalePreview**](LocalePreview.md) |  | [optional] 
**locales** | [**List[LocalePreview]**](LocalePreview.md) |  | [optional] 
**keys** | [**List[KeyPreview]**](KeyPreview.md) |  | [optional] 
**annotations** | [**List[JobAnnotationShort]**](JobAnnotationShort.md) | Returned only when &#x60;include_annotations&#x3D;true&#x60; is supplied on the request. | [optional] 
**locked** | **bool** | &#x60;true&#x60; if the job has been locked by the project&#39;s job-locking workflow (translations attached to the job are read-only until the job advances).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



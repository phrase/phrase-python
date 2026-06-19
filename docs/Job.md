# Job

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
**review_due_date** | **datetime** | The review due date for this job. Returns &#x60;null&#x60; when the project does not have review workflow enabled. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



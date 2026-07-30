# AutomationEvent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the automation event. | [optional] 
**automation_id** | **str** | Identifier of the automation that produced this event. | [optional] 
**state** | **str** | Outcome of the automation run. | [optional] 
**triggered_by** | **str** | What caused the automation to run. | [optional] 
**created_at** | **datetime** | Timestamp when the event was created. | [optional] 
**jobs_created** | **int** | Number of jobs created during this automation run. | [optional] 
**job_ids** | **List[str]** | Identifiers of the jobs created during this automation run. | [optional] 
**project** | [**AutomationEventProject**](AutomationEventProject.md) |  | [optional] 
**details** | **str** | Error message describing the failure when state is &#x60;failure&#x60;; null otherwise. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



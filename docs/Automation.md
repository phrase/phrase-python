# Automation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**trigger** | **str** |  | [optional] 
**status_filters** | **List[str]** | translation key statuses used to filter keys that are added to jobs | [optional] 
**project_id** | **str** |  | [optional] 
**project_ids** | **List[str]** | All project IDs the automation applies to. Returned alongside the singular &#x60;project_id&#x60; for backwards compatibility. | [optional] 
**job_template_id** | **str** |  | [optional] 
**job_owner_id** | **str** | User ID of the job owner that newly created jobs are assigned to. | [optional] 
**include_only_updated_locales** | **bool** | When &#x60;true&#x60;, the automation only acts on locales that changed since its last run. | [optional] 
**tags** | **List[str]** |  | [optional] 
**cron_schedule** | **str** |  | [optional] 
**time_zone** | **str** |  | [optional] 
**account** | [**Account**](Account.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ReleaseTrigger

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**branch** | **str** |  | [optional] 
**cron_schedule** | **str** | Cron schedule for the scheduler. Read more about the format of this field at https://en.wikipedia.org/wiki/Cron | [optional] 
**time_zone** | **str** | Time zone for the scheduler | [optional] 
**next_run_at** | **datetime** | The next time a release will be created for this trigger | [optional] 
**app_min_version** | **str** |  | [optional] 
**app_max_version** | **str** |  | [optional] 
**locales** | [**List[LocalePreview]**](LocalePreview.md) |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



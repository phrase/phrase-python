# ReleaseCreateParameters1

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cron_schedule** | **str** | Cron schedule for the scheduler. Read more about the format of this field at https://en.wikipedia.org/wiki/Cron | [optional] 
**time_zone** | **str** | Time zone for the scheduler | [optional] 
**locale_ids** | **List[str]** | List of locale ids that will be included in the release. | [optional] 
**tags** | **List[str]** | Only include tagged keys in the release. For a key to be included it must be tagged with all tags provided | [optional] 
**branch** | **str** | Branch used for release | [optional] 
**app_min_version** | **str** | The created releases will be available only for apps with version greater or equal to this value | [optional] 
**app_max_version** | **str** | The created releases will be available only for apps with version less or equal to this value | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# RepoSyncExportSchedule

Schedule configuration for automatic exports. Only present when the automatic export feature is enabled for the account. `null` when the `schedule` trigger is not active. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency** | **str** | How often the export runs. &#x60;cron&#x60; means a fully custom cron expression is used (&#x60;cron_schedule&#x60; holds the raw expression).  | [optional] 
**cron_schedule** | **str** | The underlying cron expression. Derived automatically from &#x60;frequency&#x60;, &#x60;time&#x60;, and day fields when using a named frequency; provided verbatim when &#x60;frequency&#x60; is &#x60;cron&#x60;.  | [optional] 
**time_zone** | **str** | IANA time zone name used to interpret the schedule. | [optional] 
**next_run_at** | **datetime** | When the next scheduled export will run, in UTC. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# RepoSyncCreateParametersExportSchedule

Schedule settings for automatic exports. Required when `export_triggers` includes `schedule`. Requires the automatic export feature to be enabled. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency** | **str** |  | [optional] 
**time** | **str** | Time of day for the export (HH:MM format). Used with &#x60;day&#x60;, &#x60;week&#x60;, and &#x60;month&#x60; frequencies. | [optional] 
**time_zone** | **str** | IANA time zone name. | [optional] 
**days_of_week** | **str** | Comma-separated day numbers (0&#x3D;Sunday … 6&#x3D;Saturday). Used with &#x60;week&#x60; frequency. | [optional] 
**day_of_month** | **int** | Day of the month (1–31). Used with &#x60;month&#x60; frequency. | [optional] 
**cron_schedule** | **str** | Raw cron expression. Used when &#x60;frequency&#x60; is &#x60;cron&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



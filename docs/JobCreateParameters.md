# JobCreateParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **str** | specify the branch to use | [optional] 
**name** | **str** | Job name | 
**source_locale_id** | **str** | The API id of the source language | [optional] 
**briefing** | **str** | Briefing for the translators | [optional] 
**due_date** | **datetime** | Date the job should be finished | [optional] 
**ticket_url** | **str** | URL to a ticket for this job (e.g. Jira, Trello) | [optional] 
**tags** | **List[str]** | tags of keys that should be included within the job | [optional] 
**translation_key_ids** | **List[str]** | ids of keys that should be included within the job | [optional] 
**job_template_id** | **str** | id of a job template you would like to model the created job after. Any manually added parameters will take preference over template attributes. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



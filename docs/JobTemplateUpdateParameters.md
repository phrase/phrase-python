# JobTemplateUpdateParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **str** | specify the branch to use | [optional] 
**name** | **str** | Job template name | 
**briefing** | **str** | Briefing for the translators | [optional] 
**autotranslate** | **bool** | Automatically translate the job using machine translation. | [optional] 
**source_locale_id** | **str** | The API id of the source language. This locale will be set as source locale for the job template. If not provided, the project default locale will be used. | [optional] 
**owner_id** | **str** | Code of the account member to set as the job template owner. The referenced user must also be a member of the project; passing the code of an account member who is not a project member returns a 404. Pass an empty string to clear a previously set owner; when blank, jobs created from this template will default to assigning the job creator as owner.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



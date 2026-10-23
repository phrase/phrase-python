# OrganizationJobTemplateUpdateParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Job template name | 
**briefing** | **str** | Briefing for the translators. Send an empty string or &#x60;null&#x60; to clear the value; omit the field to leave it unchanged. The Phrase CLI drops &#x60;null&#x60; values before sending, so use an empty string there. | [optional] 
**autotranslate** | **bool** | Automatically translate the job using machine translation. | [optional] 
**owner_id** | **str** | Code of the account member to set as the job template owner. Pass an empty string to clear a previously set owner; when blank, the owner is set to null and jobs created from this template will default to assigning the job creator as owner.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



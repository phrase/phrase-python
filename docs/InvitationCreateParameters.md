# InvitationCreateParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The email of the invited user. The &#x60;email&#x60; can not be updated once created. Create a new invitation for each unique email. | 
**role** | **str** | Invitiation role, can be any of Manager, Developer, Translator. | 
**project_ids** | **str** | List of project ids the invited user has access to. | [optional] 
**locale_ids** | **str** | List of locale ids the invited user has access to. | [optional] 
**space_ids** | **List[str]** | List of spaces the user is assigned to. | [optional] 
**team_ids** | **List[str]** | List of teams the user is assigned to. | [optional] 
**default_locale_codes** | **List[str]** | List of default locales for the user. | [optional] 
**permissions** | **Dict[str, str]** | Additional permissions depending on invitation role. Available permissions are &#x60;create_upload&#x60; and &#x60;review_translations&#x60; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



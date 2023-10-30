# InvitationUpdateParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | Invitiation role, can be any of Manager, Developer, Translator | [optional] 
**project_ids** | **str** | List of project ids the invited user has access to | [optional] 
**locale_ids** | **str** | List of locale ids the invited user has access to | [optional] 
**space_ids** | **List[str]** | List of spaces the user is assigned to. | [optional] 
**team_ids** | **List[str]** | List of teams the user is assigned to. | [optional] 
**default_locale_codes** | **List[str]** | List of default locales for the user. | [optional] 
**permissions** | **Dict[str, str]** | Additional permissions depending on invitation role. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



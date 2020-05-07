# InvitationCreateParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The email of the invited user. The &lt;code&gt;email&lt;/code&gt; can not be updated once created. Create a new invitation for each unique email. | [optional] 
**role** | **str** | Invitiation role, can be any of Manager, Developer, Translator. | [optional] 
**project_ids** | **str** | List of project ids the invited user has access to. | [optional] 
**locale_ids** | **str** | List of locale ids the invited user has access to. | [optional] 
**permissions** | **dict(str, str)** | Additional permissions depending on invitation role. Available permissions are &lt;code&gt;create_upload&lt;/code&gt; and &lt;code&gt;review_translations&lt;/code&gt; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



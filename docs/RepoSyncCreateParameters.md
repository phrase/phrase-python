# RepoSyncCreateParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | ID of the project to connect the Repo Sync to. | 
**name** | **str** | Optional custom display name for this repo sync. Defaults to null; when null the project name is used as the display name.  | [optional] 
**git_provider** | **str** | The Git provider to use. | [optional] [default to 'github']
**connection_type** | **str** | The authentication method used to connect to the Git provider. Defaults to &#x60;token&#x60; if not specified.  Valid values: - &#x60;token&#x60; — Personal access token stored on the Repo Sync. Supported by all providers. - &#x60;github_app&#x60; — Authenticate via the Phrase GitHub App installation on your account. GitHub only. The account must already have the GitHub App installed; if not, the response will include a &#x60;github_app_installation_url&#x60;. - &#x60;self_hosted&#x60; — Token-based auth for self-hosted Git instances. Requires &#x60;custom_api_endpoint&#x60;. | 
**repo_name** | **str** | Full repository name including the owner, e.g. &#x60;my-org/my-repo&#x60;. | 
**base_branch** | **str** | The default branch to use for imports and exports. | [optional] 
**pr_branch** | **str** | Branch that translations are exported to before opening a pull request. If omitted, exports go directly to &#x60;base_branch&#x60;. | [optional] 
**auto_import** | **bool** | Enable automatic import of translations triggered by pushes to the repository. | [optional] 
**access_token** | **str** | Personal access token for the Git provider. Required when &#x60;connection_type&#x60; is &#x60;token&#x60; or &#x60;self_hosted&#x60;. Not used for &#x60;github_app&#x60;. | [optional] 
**custom_api_endpoint** | **str** | Custom API endpoint URL for self-hosted Git instances. Required when &#x60;connection_type&#x60; is &#x60;self_hosted&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



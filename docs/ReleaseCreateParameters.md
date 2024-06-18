# ReleaseCreateParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the release | [optional] 
**platforms** | **List[str]** | List of platforms the release should support. | [optional] 
**locale_ids** | **List[str]** | List of locale ids that will be included in the release. If empty, distribution locales will be used | [optional] 
**tags** | **List[str]** | Only include tagged keys in the release. For a key to be included it must be tagged with all tags provided | [optional] 
**app_min_version** | **str** | Minimum version of the app that the release supports in semver format | [optional] 
**app_max_version** | **str** | Maximum version of the app that the release supports in semver format | [optional] 
**branch** | **str** | Branch used for release | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



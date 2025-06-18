# TranslationsUnverifyParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **str** | specify the branch to use | [optional] 
**q** | **str** | Specify a query to find translations by content (including wildcards).  *Note: Search is limited to 10000 results and may not include recently updated data (depending on the project size).*  The following qualifiers are supported in the query: * &#x60;id:translation_id,...&#x60; for queries on a comma-separated list of ids * &#x60;tags:XYZ&#x60; for tags on the translation * &#x60;unverified:{true|false}&#x60; for verification status * &#x60;excluded:{true|false}&#x60; for exclusion status * &#x60;updated_at:{&gt;&#x3D;|&lt;&#x3D;}2013-02-21T00:00:00Z&#x60; for date range queries  Find more examples [here](/en/api/strings/usage-examples).  | [optional] 
**sort** | **str** | Sort criteria. Can be one of: key_name, created_at, updated_at. | [optional] 
**order** | **str** | Order direction. Can be one of: asc, desc. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



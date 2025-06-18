# KeysSearchParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **str** | specify the branch to use | [optional] 
**sort** | **str** | Sort by field. Can be one of: name, created_at, updated_at. | [optional] 
**order** | **str** | Order direction. Can be one of: asc, desc. | [optional] 
**q** | **str** | Specify a query to do broad search for keys by name (including wildcards).  The following qualifiers are also supported in the search term:  * &#x60;ids:key_id,...&#x60; for queries on a comma-separated list of ids * &#x60;name:key_name,...&#x60; for text queries on a comma-seperated list of exact key names - spaces, commas, and colons need to be escaped with double backslashes * &#x60;tags:tag_name,...&#x60; to filter for keys with certain comma-seperated list of tags * &#x60;uploads:upload_id,...&#x60; to filter for keys with certain comma-seperated list of uploads * &#x60;job:{true|false}&#x60; to filter for keys mentioned in an active job * &#x60;translated:{true|false}&#x60; for translation status (also requires &#x60;locale_id&#x60; to be specified) * &#x60;updated_at:{&gt;&#x3D;|&lt;&#x3D;}2013-02-21T00:00:00Z&#x60; for date range queries * &#x60;unmentioned_in_upload:upload_id,...&#x60; to filter keys unmentioned within upload. When multiple upload IDs provided, matches only keys not mentioned in **all** uploads  Find more examples [here](/en/api/strings/usage-examples). Please note: If &#x60;tags&#x60; are added to filter the search, the search will be limited to a maximum of 65,536 tagged keys.  | [optional] 
**locale_id** | **str** | Locale used to determine the translation state of a key when filtering for untranslated or translated keys. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



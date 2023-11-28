# KeysSearchParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **str** | specify the branch to use | [optional] 
**sort** | **str** | Sort by field. Can be one of: name, created_at, updated_at. | [optional] 
**order** | **str** | Order direction. Can be one of: asc, desc. | [optional] 
**q** | **str** | Specify a query to do broad search for keys by name (including wildcards).&lt;br&gt;&lt;br&gt; The following qualifiers are also supported in the search term:&lt;br&gt; &lt;ul&gt;   &lt;li&gt;&lt;code&gt;ids:key_id,...&lt;/code&gt; for queries on a comma-separated list of ids&lt;/li&gt;   &lt;li&gt;&lt;code&gt;name:key_name,...&lt;/code&gt; for text queries on a comma-seperated list of exact key names - spaces, commas, and colons need to be escaped with double backslashes&lt;/li&gt;   &lt;li&gt;&lt;code&gt;tags:tag_name,...&lt;/code&gt; to filter for keys with certain comma-seperated list of tags&lt;/li&gt;   &lt;li&gt;&lt;code&gt;uploads:upload_id,...&lt;/code&gt; to filter for keys with certain comma-seperated list of uploads&lt;/li&gt;   &lt;li&gt;&lt;code&gt;job:{true|false}&lt;/code&gt; to filter for keys mentioned in an active job&lt;/li&gt;   &lt;li&gt;&lt;code&gt;translated:{true|false}&lt;/code&gt; for translation status (also requires &lt;code&gt;locale_id&lt;/code&gt; to be specified)&lt;/li&gt;   &lt;li&gt;&lt;code&gt;updated_at:{&amp;gt;&#x3D;|&amp;lt;&#x3D;}2013-02-21T00:00:00Z&lt;/code&gt; for date range queries&lt;/li&gt;   &lt;li&gt;&lt;code&gt;unmentioned_in_upload:upload_id&lt;/code&gt; to filter keys unmentioned within upload&lt;/li&gt; &lt;/ul&gt; Find more examples &lt;a href&#x3D;\&quot;#overview--usage-examples\&quot;&gt;here&lt;/a&gt;. Please note: If &lt;code&gt;tags&lt;/code&gt; are added to filter the search, the search will be limited to a maximum of 65,536 tagged keys.  | [optional] 
**locale_id** | **str** | Locale used to determine the translation state of a key when filtering for untranslated or translated keys. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



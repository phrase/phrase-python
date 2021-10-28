# DistributionCreateParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the distribution | [optional] 
**project_id** | **str** | Project id the distribution should be assigned to. | [optional] 
**platforms** | **list[str]** | List of platforms the distribution should support. | [optional] 
**locale_ids** | **list[str]** | List of locale ids that will be part of distribution releases | [optional] 
**format_options** | **dict(str, str)** | Additional formatting and render options. Only &lt;code&gt;enclose_in_cdata&lt;/code&gt; is available for platform &lt;code&gt;android&lt;/code&gt;. | [optional] 
**fallback_to_non_regional_locale** | **bool** | Indicates whether to fallback to non regional locale when locale can not be found | [optional] 
**fallback_to_default_locale** | **bool** | Indicates whether to fallback to projects default locale when locale can not be found | [optional] 
**use_last_reviewed_version** | **bool** | Use last reviewed instead of latest translation in a project | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



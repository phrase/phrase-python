# DistributionCreateParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the distribution | 
**project_id** | **str** | Project id the distribution should be assigned to. | 
**platforms** | **List[str]** | List of platforms the distribution should support. Valid values are: * &#x60;android&#x60; * &#x60;ios&#x60; * &#x60;flutter&#x60; * &#x60;i18next&#x60; * &#x60;rails&#x60; | [optional] 
**locale_ids** | **List[str]** | List of locale ids that will be part of distribution releases | [optional] 
**format_options** | **Dict[str, str]** | Additional formatting and render options. Only &lt;code&gt;enclose_in_cdata&lt;/code&gt; is available for platform &lt;code&gt;android&lt;/code&gt;. | [optional] 
**fallback_locales_enabled** | **bool** | Use fallback locale if there is no translation in the current locale. | [optional] 
**fallback_to_non_regional_locale** | **bool** | Indicates whether to fallback to non regional locale when locale can not be found | [optional] 
**fallback_to_default_locale** | **bool** | Indicates whether to fallback to projects default locale when locale can not be found | [optional] 
**use_last_reviewed_version** | **bool** | Use last reviewed instead of latest translation in a project | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



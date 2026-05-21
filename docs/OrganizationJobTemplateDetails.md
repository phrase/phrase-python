# OrganizationJobTemplateDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**briefing** | **str** |  | [optional] 
**autotranslate_enabled** | **bool** | When &#x60;true&#x60;, jobs created from this template are auto-translated on creation. Maps to the &#x60;autotranslate&#x60; field on the request body.  | [optional] 
**source_locale_id** | **str** | Optional. ID of the source locale used by jobs created from this template. When omitted, the project&#39;s default source locale is used.  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**owner** | [**UserPreview**](UserPreview.md) |  | [optional] 
**creator** | [**UserPreview**](UserPreview.md) |  | [optional] 
**locales** | [**List[LocalePreview]**](LocalePreview.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



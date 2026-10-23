# WebhookUpdateParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_url** | **str** | Callback URL to send requests to | [optional] 
**secret** | **str** | Webhook secret used to calculate signature. If empty, the default project secret will be used. | [optional] 
**description** | **str** | Webhook description. Send an empty string or &#x60;null&#x60; to clear the value; omit the field to leave it unchanged. The Phrase CLI drops &#x60;null&#x60; values before sending, so use an empty string there. | [optional] 
**events** | **str** | List of event names to trigger the webhook (separated by comma) | [optional] 
**active** | **bool** | Whether webhook is active or inactive | [optional] 
**include_branches** | **bool** | If enabled, webhook will also be triggered for events from branches of the project specified. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



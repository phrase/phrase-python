# Format

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human-readable display name of the format. | 
**api_name** | **str** | Identifier used to reference this format in API requests, such as the file_format parameter on the uploads and downloads endpoints. | 
**description** | **str** | Human-readable summary of the format and its typical use case. | 
**extension** | **str** | Default file extension associated with this format. | 
**default_encoding** | **str** | Default character encoding used when reading or writing files in this format. | 
**importable** | **bool** | Whether locale files can be imported using this format. | 
**exportable** | **bool** | Whether locale files can be exported using this format. | 
**default_file** | **str** | Conventional file path pattern for this format. Contains locale_name as a placeholder for the locale identifier. | 
**renders_default_locale** | **bool** | When true, exported files contain the default locale&#39;s content for any key that has no translation in the target locale. | 
**includes_locale_information** | **bool** | When true, files in this format embed locale information so Phrase can detect the locale automatically on import. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



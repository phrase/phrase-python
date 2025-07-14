# KeyUpdateParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **str** | specify the branch to use | [optional] 
**name** | **str** | Key name | [optional] 
**description** | **str** | Key description (usually includes contextual information for translators) | [optional] 
**plural** | **bool** | Indicates whether key supports pluralization | [optional] 
**use_ordinal_rules** | **bool** | Indicates whether key uses ordinal rules for pluralization | [optional] 
**name_plural** | **str** | Plural name for the key (used in some file formats, e.g. Gettext) | [optional] 
**data_type** | **str** | Type of the key. Can be one of the following: string, number, boolean, array, markdown. | [optional] 
**tags** | **str** | List of tags separated by comma to be associated with the key. | [optional] 
**max_characters_allowed** | **int** | Max. number of characters translations for this key can have. | [optional] 
**screenshot** | **bytearray** | Screenshot/image for the key. This parameter is deprecated. Please use the Screenshots endpoint instead. | [optional] 
**remove_screenshot** | **bool** | Indicates whether the screenshot will be deleted. This parameter is deprecated. Please use the Screenshots endpoint instead. | [optional] 
**unformatted** | **bool** | Indicates whether the key should be exported as \&quot;unformatted\&quot;. Supported by Android XML and other formats. | [optional] 
**xml_space_preserve** | **bool** | Indicates whether the key should be exported with \&quot;xml:space&#x3D;preserve\&quot;. Supported by several XML-based formats. | [optional] 
**original_file** | **str** | Original file attribute. Used in some formats, e.g. XLIFF. | [optional] 
**localized_format_string** | **str** | NSStringLocalizedFormatKey attribute. Used in .stringsdict format. | [optional] 
**localized_format_key** | **str** | NSStringLocalizedFormatKey attribute. Used in .stringsdict format. | [optional] 
**custom_metadata** | **object** | Updates/Creates custom metadata property name and value pairs to be associated with key. If you want to delete a custom metadata property, you can set its value to null. If you want to update a custom metadata property, you can set its value to the new value. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



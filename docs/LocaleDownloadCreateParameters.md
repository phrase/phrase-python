# LocaleDownloadCreateParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_format** | **str** | File format name. See the [format guide](https://support.phrase.com/hc/en-us/sections/6111343326364) for all supported file formats. | 
**branch** | **str** | specify the branch to use | [optional] 
**tags** | **str** | Limit results to keys tagged with a list of comma separated tag names. | [optional] 
**include_empty_translations** | **bool** | Indicates whether keys without translations should be included in the output as well. | [optional] 
**exclude_empty_zero_forms** | **bool** | Indicates whether zero forms should be included when empty in pluralized keys. | [optional] 
**include_translated_keys** | **bool** | Include translated keys in the locale file. Use in combination with include_empty_translations to obtain only untranslated keys. | [optional] 
**keep_notranslate_tags** | **bool** | Indicates whether [NOTRANSLATE] tags should be kept. | [optional] 
**format_options** | **object** | Additional formatting and render options. See the [format guide](https://support.phrase.com/hc/en-us/sections/6111343326364) for a list of options available for each format. Pass format options as a JSON object with key-value pairs corresponding to the option name and value. For example, to include comments in a Gettext file, pass &#x60;{\&quot;include_comments\&quot;: true}&#x60;.  | [optional] 
**encoding** | **str** | Enforces a specific encoding on the file contents. Valid options are \&quot;UTF-8\&quot;, \&quot;UTF-16\&quot; and \&quot;ISO-8859-1\&quot;. | [optional] 
**include_unverified_translations** | **bool** | if set to false unverified translations are excluded | [optional] 
**use_last_reviewed_version** | **bool** | If set to true the last reviewed version of a translation is used. This is only available if the review workflow is enabled for the project. | [optional] 
**locale_ids** | **List[str]** | Locale IDs or locale names | [optional] 
**fallback_locale_id** | **str** | If a key has no translation in the locale being downloaded, the translation in the fallback locale will be used. Provide the ID of the locale that should be used as the fallback. Requires &#x60;include_empty_translations&#x60; to be set to &#x60;true&#x60; unless &#x60;fallback_for_unverified_translations&#x60; is also set to &#x60;true&#x60;. Mutually exclusive with &#x60;use_locale_fallback&#x60;.  | [optional] 
**use_locale_fallback** | **bool** | If a key has no translation in the locale being downloaded, the translation in the fallback locale will be used. Fallback locale is defined in [locale&#39;s settings](/en/api/strings/locales/update-a-locale#body-fallback-locale-id). Requires &#x60;include_empty_translations&#x60; to be set to &#x60;true&#x60; unless &#x60;fallback_for_unverified_translations&#x60; is also set to &#x60;true&#x60;. Mutually exclusive with &#x60;fallback_locale_id&#x60;.  | [optional] 
**fallback_for_unverified_translations** | **bool** | If set to &#x60;true&#x60;, translations in a non-final state are replaced by the fallback locale&#39;s translation at export time. In the simple workflow, \&quot;non-final\&quot; means &#x60;unverified&#x60;. In the review workflow, it additionally includes &#x60;translated&#x60; (awaiting review). No stored translations are modified. Requires &#x60;fallback_locale_id&#x60; or &#x60;use_locale_fallback&#x60; to be set; a &#x60;422&#x60; validation error is returned otherwise.  | [optional] 
**source_locale_id** | **str** | Provides the source language of a corresponding job as the source language of the generated locale file. This parameter will be ignored unless used in combination with a &#x60;tag&#x60; parameter indicating a specific job. | [optional] 
**custom_metadata_filters** | **object** | Custom metadata filters. Provide the name of the metadata field and the value to filter by. Only keys with matching metadata will be included in the download.  | [optional] 
**translation_key_prefix** | **str** | Download all translation keys, and remove the specified prefix where possible. Warning: this may create duplicate key names if other keys share the same name after the prefix is removed. | [optional] 
**filter_by_prefix** | **bool** | Only download translation keys containing the prefix specified by &#x60;translation_key_prefix&#x60;, and remove that prefix from the generated file. Requires &#x60;translation_key_prefix&#x60; to be set. | [optional] 
**updated_since** | **str** | Only include translations and keys that have been updated since the given date. The date must be in ISO 8601 format (e.g., &#x60;2023-01-01T00:00:00Z&#x60;).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



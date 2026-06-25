# KeyLinksBatchDestroyParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**child_key_ids** | **List[str]** | Codes of the child keys to unlink. Required when unlink_parent is false or omitted. Ignored when unlink_parent is true. | 
**unlink_parent** | **bool** | When true, dissolves the entire linked-key group by unlinking all children and removing the group. The child_key_ids field is ignored when this is set to true. | [optional] [default to False]
**strategy** | **str** | Controls what happens to child key translation content after unlinking. keep_content (default) copies the parent translation into each child; remove_content clears each child translation. | [optional] [default to 'keep_content']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



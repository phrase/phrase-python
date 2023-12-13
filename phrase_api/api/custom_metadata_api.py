# coding: utf-8

"""
    Phrase Strings API Reference

    The version of the OpenAPI document: 2.0.0
    Contact: support@phrase.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from phrase_api.api_client import ApiClient
from phrase_api.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class CustomMetadataApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def custom_metadata_properties_delete(self, account_id, id, **kwargs):  # noqa: E501
        """Destroy property  # noqa: E501

        Destroy a custom metadata property of an account.  This endpoint is only available to accounts with advanced plans or above.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.custom_metadata_properties_delete(account_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str account_id: Account ID (required)
        :param str id: ID (required)
        :param str x_phrase_app_otp: Two-Factor-Authentication token (optional)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.custom_metadata_properties_delete_with_http_info(account_id, id, **kwargs)  # noqa: E501

    def custom_metadata_properties_delete_with_http_info(self, account_id, id, **kwargs):  # noqa: E501
        """Destroy property  # noqa: E501

        Destroy a custom metadata property of an account.  This endpoint is only available to accounts with advanced plans or above.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.custom_metadata_properties_delete_with_http_info(account_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str account_id: Account ID (required)
        :param str id: ID (required)
        :param str x_phrase_app_otp: Two-Factor-Authentication token (optional)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'account_id',
            'id',
            'x_phrase_app_otp'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method custom_metadata_properties_delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'account_id' is set
        if self.api_client.client_side_validation and ('account_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['account_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `account_id` when calling `custom_metadata_properties_delete`")  # noqa: E501
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `custom_metadata_properties_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in local_var_params:
            path_params['account_id'] = local_var_params['account_id']  # noqa: E501
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_phrase_app_otp' in local_var_params:
            header_params['X-PhraseApp-OTP'] = local_var_params['x_phrase_app_otp']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Basic', 'Token']  # noqa: E501

        return self.api_client.call_api(
            '/accounts/{account_id}/custom_metadata/properties/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def custom_metadata_properties_list(self, account_id, **kwargs):  # noqa: E501
        """List properties  # noqa: E501

        List all custom metadata properties for an account.  This endpoint is only available to accounts with advanced plans or above.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.custom_metadata_properties_list(account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str account_id: Account ID (required)
        :param str x_phrase_app_otp: Two-Factor-Authentication token (optional)
        :param CustomMetadataDataType data_type: Data Type of Custom Metadata Property
        :param str project_id: id of project that the properties belong to
        :param int page: Page number
        :param int per_page: Limit on the number of objects to be returned, between 1 and 100. 25 by default
        :param str sort: Sort criteria. Can be one of: name, data_type, created_at.
        :param str order: Order direction. Can be one of: asc, desc.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: List[CustomMetadataProperty]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.custom_metadata_properties_list_with_http_info(account_id, **kwargs)  # noqa: E501

    def custom_metadata_properties_list_with_http_info(self, account_id, **kwargs):  # noqa: E501
        """List properties  # noqa: E501

        List all custom metadata properties for an account.  This endpoint is only available to accounts with advanced plans or above.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.custom_metadata_properties_list_with_http_info(account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str account_id: Account ID (required)
        :param str x_phrase_app_otp: Two-Factor-Authentication token (optional)
        :param CustomMetadataDataType data_type: Data Type of Custom Metadata Property
        :param str project_id: id of project that the properties belong to
        :param int page: Page number
        :param int per_page: Limit on the number of objects to be returned, between 1 and 100. 25 by default
        :param str sort: Sort criteria. Can be one of: name, data_type, created_at.
        :param str order: Order direction. Can be one of: asc, desc.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(List[CustomMetadataProperty], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'account_id',
            'x_phrase_app_otp',
            'data_type',
            'project_id',
            'page',
            'per_page',
            'sort',
            'order'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method custom_metadata_properties_list" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'account_id' is set
        if self.api_client.client_side_validation and ('account_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['account_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `account_id` when calling `custom_metadata_properties_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in local_var_params:
            path_params['account_id'] = local_var_params['account_id']  # noqa: E501

        query_params = []
        if 'data_type' in local_var_params and local_var_params['data_type'] is not None:  # noqa: E501
            query_params.append(('data_type', local_var_params['data_type']))  # noqa: E501
        if 'project_id' in local_var_params and local_var_params['project_id'] is not None:  # noqa: E501
            query_params.append(('project_id', local_var_params['project_id']))  # noqa: E501
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'per_page' in local_var_params and local_var_params['per_page'] is not None:  # noqa: E501
            query_params.append(('per_page', local_var_params['per_page']))  # noqa: E501
        if 'sort' in local_var_params and local_var_params['sort'] is not None:  # noqa: E501
            query_params.append(('sort', local_var_params['sort']))  # noqa: E501
        if 'order' in local_var_params and local_var_params['order'] is not None:  # noqa: E501
            query_params.append(('order', local_var_params['order']))  # noqa: E501

        header_params = {}
        if 'x_phrase_app_otp' in local_var_params:
            header_params['X-PhraseApp-OTP'] = local_var_params['x_phrase_app_otp']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic', 'Token']  # noqa: E501

        return self.api_client.call_api(
            '/accounts/{account_id}/custom_metadata/properties', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='List[CustomMetadataProperty]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def custom_metadata_property_create(self, account_id, name, data_type, **kwargs):  # noqa: E501
        """Create a property  # noqa: E501

        Create a new custom metadata property.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.custom_metadata_property_create(account_id, name, data_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str account_id: Account ID (required)
        :param str name: name of the property (required)
        :param CustomMetadataDataType data_type: Data Type of Custom Metadata Property (required)
        :param str x_phrase_app_otp: Two-Factor-Authentication token (optional)
        :param str description: description of property
        :param List[str] project_ids: ids of projects that the property belongs to
        :param List[str] value_options: value options of property (only applies to single or multi select properties)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CustomMetadataProperty
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.custom_metadata_property_create_with_http_info(account_id, name, data_type, **kwargs)  # noqa: E501

    def custom_metadata_property_create_with_http_info(self, account_id, name, data_type, **kwargs):  # noqa: E501
        """Create a property  # noqa: E501

        Create a new custom metadata property.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.custom_metadata_property_create_with_http_info(account_id, name, data_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str account_id: Account ID (required)
        :param str name: name of the property (required)
        :param CustomMetadataDataType data_type: Data Type of Custom Metadata Property (required)
        :param str x_phrase_app_otp: Two-Factor-Authentication token (optional)
        :param str description: description of property
        :param List[str] project_ids: ids of projects that the property belongs to
        :param List[str] value_options: value options of property (only applies to single or multi select properties)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(CustomMetadataProperty, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'account_id',
            'name',
            'data_type',
            'x_phrase_app_otp',
            'description',
            'project_ids',
            'value_options'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method custom_metadata_property_create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'account_id' is set
        if self.api_client.client_side_validation and ('account_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['account_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `account_id` when calling `custom_metadata_property_create`")  # noqa: E501
        # verify the required parameter 'name' is set
        if self.api_client.client_side_validation and ('name' not in local_var_params or  # noqa: E501
                                                        local_var_params['name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `name` when calling `custom_metadata_property_create`")  # noqa: E501
        # verify the required parameter 'data_type' is set
        if self.api_client.client_side_validation and ('data_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['data_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `data_type` when calling `custom_metadata_property_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in local_var_params:
            path_params['account_id'] = local_var_params['account_id']  # noqa: E501

        query_params = []
        if 'name' in local_var_params and local_var_params['name'] is not None:  # noqa: E501
            query_params.append(('name', local_var_params['name']))  # noqa: E501
        if 'data_type' in local_var_params and local_var_params['data_type'] is not None:  # noqa: E501
            query_params.append(('data_type', local_var_params['data_type']))  # noqa: E501
        if 'description' in local_var_params and local_var_params['description'] is not None:  # noqa: E501
            query_params.append(('description', local_var_params['description']))  # noqa: E501
        if 'project_ids' in local_var_params and local_var_params['project_ids'] is not None:  # noqa: E501
            query_params.append(('project_ids', local_var_params['project_ids']))  # noqa: E501
            collection_formats['project_ids'] = 'multi'  # noqa: E501
        if 'value_options' in local_var_params and local_var_params['value_options'] is not None:  # noqa: E501
            query_params.append(('value_options', local_var_params['value_options']))  # noqa: E501
            collection_formats['value_options'] = 'multi'  # noqa: E501

        header_params = {}
        if 'x_phrase_app_otp' in local_var_params:
            header_params['X-PhraseApp-OTP'] = local_var_params['x_phrase_app_otp']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic', 'Token']  # noqa: E501

        return self.api_client.call_api(
            '/accounts/{account_id}/custom_metadata/properties', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CustomMetadataProperty',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def custom_metadata_property_show(self, account_id, id, **kwargs):  # noqa: E501
        """Get a single property  # noqa: E501

        Get details of a single custom property.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.custom_metadata_property_show(account_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str account_id: Account ID (required)
        :param str id: ID (required)
        :param str x_phrase_app_otp: Two-Factor-Authentication token (optional)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CustomMetadataProperty
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.custom_metadata_property_show_with_http_info(account_id, id, **kwargs)  # noqa: E501

    def custom_metadata_property_show_with_http_info(self, account_id, id, **kwargs):  # noqa: E501
        """Get a single property  # noqa: E501

        Get details of a single custom property.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.custom_metadata_property_show_with_http_info(account_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str account_id: Account ID (required)
        :param str id: ID (required)
        :param str x_phrase_app_otp: Two-Factor-Authentication token (optional)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(CustomMetadataProperty, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'account_id',
            'id',
            'x_phrase_app_otp'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method custom_metadata_property_show" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'account_id' is set
        if self.api_client.client_side_validation and ('account_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['account_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `account_id` when calling `custom_metadata_property_show`")  # noqa: E501
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `custom_metadata_property_show`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in local_var_params:
            path_params['account_id'] = local_var_params['account_id']  # noqa: E501
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_phrase_app_otp' in local_var_params:
            header_params['X-PhraseApp-OTP'] = local_var_params['x_phrase_app_otp']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic', 'Token']  # noqa: E501

        return self.api_client.call_api(
            '/accounts/{account_id}/custom_metadata/properties/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CustomMetadataProperty',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def custom_metadata_property_update(self, account_id, id, **kwargs):  # noqa: E501
        """Update a property  # noqa: E501

        Update an existing custom metadata property.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.custom_metadata_property_update(account_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str account_id: Account ID (required)
        :param str id: ID (required)
        :param str x_phrase_app_otp: Two-Factor-Authentication token (optional)
        :param str name: name of the property
        :param str description: description of property
        :param List[str] project_ids: ids of projects that the property belongs to
        :param List[str] value_options: value options of property (only applies to single or multi select properties)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CustomMetadataProperty
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.custom_metadata_property_update_with_http_info(account_id, id, **kwargs)  # noqa: E501

    def custom_metadata_property_update_with_http_info(self, account_id, id, **kwargs):  # noqa: E501
        """Update a property  # noqa: E501

        Update an existing custom metadata property.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.custom_metadata_property_update_with_http_info(account_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str account_id: Account ID (required)
        :param str id: ID (required)
        :param str x_phrase_app_otp: Two-Factor-Authentication token (optional)
        :param str name: name of the property
        :param str description: description of property
        :param List[str] project_ids: ids of projects that the property belongs to
        :param List[str] value_options: value options of property (only applies to single or multi select properties)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(CustomMetadataProperty, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'account_id',
            'id',
            'x_phrase_app_otp',
            'name',
            'description',
            'project_ids',
            'value_options'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method custom_metadata_property_update" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'account_id' is set
        if self.api_client.client_side_validation and ('account_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['account_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `account_id` when calling `custom_metadata_property_update`")  # noqa: E501
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `custom_metadata_property_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in local_var_params:
            path_params['account_id'] = local_var_params['account_id']  # noqa: E501
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []
        if 'name' in local_var_params and local_var_params['name'] is not None:  # noqa: E501
            query_params.append(('name', local_var_params['name']))  # noqa: E501
        if 'description' in local_var_params and local_var_params['description'] is not None:  # noqa: E501
            query_params.append(('description', local_var_params['description']))  # noqa: E501
        if 'project_ids' in local_var_params and local_var_params['project_ids'] is not None:  # noqa: E501
            query_params.append(('project_ids', local_var_params['project_ids']))  # noqa: E501
            collection_formats['project_ids'] = 'multi'  # noqa: E501
        if 'value_options' in local_var_params and local_var_params['value_options'] is not None:  # noqa: E501
            query_params.append(('value_options', local_var_params['value_options']))  # noqa: E501
            collection_formats['value_options'] = 'multi'  # noqa: E501

        header_params = {}
        if 'x_phrase_app_otp' in local_var_params:
            header_params['X-PhraseApp-OTP'] = local_var_params['x_phrase_app_otp']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic', 'Token']  # noqa: E501

        return self.api_client.call_api(
            '/accounts/{account_id}/custom_metadata/properties/{id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CustomMetadataProperty',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

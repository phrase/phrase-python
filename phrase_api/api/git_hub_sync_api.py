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


class GitHubSyncApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def github_sync_export(self, github_sync_export_parameters, **kwargs):  # noqa: E501
        """Export from Phrase Strings to GitHub  # noqa: E501

        Export translations from Phrase Strings to GitHub according to the .phraseapp.yml file within the GitHub repository.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.github_sync_export(github_sync_export_parameters, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param GithubSyncExportParameters github_sync_export_parameters: (required)
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
        return self.github_sync_export_with_http_info(github_sync_export_parameters, **kwargs)  # noqa: E501

    def github_sync_export_with_http_info(self, github_sync_export_parameters, **kwargs):  # noqa: E501
        """Export from Phrase Strings to GitHub  # noqa: E501

        Export translations from Phrase Strings to GitHub according to the .phraseapp.yml file within the GitHub repository.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.github_sync_export_with_http_info(github_sync_export_parameters, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param GithubSyncExportParameters github_sync_export_parameters: (required)
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
            'github_sync_export_parameters',
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
                    " to method github_sync_export" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'github_sync_export_parameters' is set
        if self.api_client.client_side_validation and ('github_sync_export_parameters' not in local_var_params or  # noqa: E501
                                                        local_var_params['github_sync_export_parameters'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `github_sync_export_parameters` when calling `github_sync_export`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_phrase_app_otp' in local_var_params:
            header_params['X-PhraseApp-OTP'] = local_var_params['x_phrase_app_otp']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'github_sync_export_parameters' in local_var_params:
            body_params = local_var_params['github_sync_export_parameters']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic', 'Token']  # noqa: E501

        return self.api_client.call_api(
            '/github_syncs/export', 'POST',
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

    def github_sync_import(self, github_sync_import_parameters, **kwargs):  # noqa: E501
        """Import to Phrase Strings from GitHub  # noqa: E501

        Import files to Phrase Strings from your connected GitHub repository.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.github_sync_import(github_sync_import_parameters, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param GithubSyncImportParameters github_sync_import_parameters: (required)
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
        return self.github_sync_import_with_http_info(github_sync_import_parameters, **kwargs)  # noqa: E501

    def github_sync_import_with_http_info(self, github_sync_import_parameters, **kwargs):  # noqa: E501
        """Import to Phrase Strings from GitHub  # noqa: E501

        Import files to Phrase Strings from your connected GitHub repository.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.github_sync_import_with_http_info(github_sync_import_parameters, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param GithubSyncImportParameters github_sync_import_parameters: (required)
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
            'github_sync_import_parameters',
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
                    " to method github_sync_import" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'github_sync_import_parameters' is set
        if self.api_client.client_side_validation and ('github_sync_import_parameters' not in local_var_params or  # noqa: E501
                                                        local_var_params['github_sync_import_parameters'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `github_sync_import_parameters` when calling `github_sync_import`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_phrase_app_otp' in local_var_params:
            header_params['X-PhraseApp-OTP'] = local_var_params['x_phrase_app_otp']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'github_sync_import_parameters' in local_var_params:
            body_params = local_var_params['github_sync_import_parameters']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic', 'Token']  # noqa: E501

        return self.api_client.call_api(
            '/github_syncs/import', 'POST',
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

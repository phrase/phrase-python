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


class LocaleDownloadsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def locale_download_create(self, project_id, locale_id, locale_download_create_parameters, **kwargs):  # noqa: E501
        """Initiate async download of a locale  # noqa: E501

        Prepare a locale for download in a specific file format.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.locale_download_create(project_id, locale_id, locale_download_create_parameters, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_id: Project ID (required)
        :param str locale_id: Locale ID (required)
        :param LocaleDownloadCreateParameters locale_download_create_parameters: (required)
        :param str x_phrase_app_otp: Two-Factor-Authentication token (optional)
        :param str if_modified_since: Last modified condition, see <a href=\"#overview--conditional-get-requests--http-caching\">Conditional GET requests / HTTP Caching</a> (optional)
        :param str if_none_match: ETag condition, see <a href=\"#overview--conditional-get-requests--http-caching\">Conditional GET requests / HTTP Caching</a> (optional)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: LocaleDownload
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.locale_download_create_with_http_info(project_id, locale_id, locale_download_create_parameters, **kwargs)  # noqa: E501

    def locale_download_create_with_http_info(self, project_id, locale_id, locale_download_create_parameters, **kwargs):  # noqa: E501
        """Initiate async download of a locale  # noqa: E501

        Prepare a locale for download in a specific file format.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.locale_download_create_with_http_info(project_id, locale_id, locale_download_create_parameters, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_id: Project ID (required)
        :param str locale_id: Locale ID (required)
        :param LocaleDownloadCreateParameters locale_download_create_parameters: (required)
        :param str x_phrase_app_otp: Two-Factor-Authentication token (optional)
        :param str if_modified_since: Last modified condition, see <a href=\"#overview--conditional-get-requests--http-caching\">Conditional GET requests / HTTP Caching</a> (optional)
        :param str if_none_match: ETag condition, see <a href=\"#overview--conditional-get-requests--http-caching\">Conditional GET requests / HTTP Caching</a> (optional)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(LocaleDownload, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'project_id',
            'locale_id',
            'locale_download_create_parameters',
            'x_phrase_app_otp',
            'if_modified_since',
            'if_none_match'
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
                    " to method locale_download_create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'project_id' is set
        if self.api_client.client_side_validation and ('project_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['project_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `project_id` when calling `locale_download_create`")  # noqa: E501
        # verify the required parameter 'locale_id' is set
        if self.api_client.client_side_validation and ('locale_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['locale_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `locale_id` when calling `locale_download_create`")  # noqa: E501
        # verify the required parameter 'locale_download_create_parameters' is set
        if self.api_client.client_side_validation and ('locale_download_create_parameters' not in local_var_params or  # noqa: E501
                                                        local_var_params['locale_download_create_parameters'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `locale_download_create_parameters` when calling `locale_download_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']  # noqa: E501
        if 'locale_id' in local_var_params:
            path_params['locale_id'] = local_var_params['locale_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_phrase_app_otp' in local_var_params:
            header_params['X-PhraseApp-OTP'] = local_var_params['x_phrase_app_otp']  # noqa: E501
        if 'if_modified_since' in local_var_params:
            header_params['If-Modified-Since'] = local_var_params['if_modified_since']  # noqa: E501
        if 'if_none_match' in local_var_params:
            header_params['If-None-Match'] = local_var_params['if_none_match']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'locale_download_create_parameters' in local_var_params:
            body_params = local_var_params['locale_download_create_parameters']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic', 'Token']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{project_id}/locales/{locale_id}/downloads', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LocaleDownload',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def locale_download_show(self, project_id, locale_id, id, **kwargs):  # noqa: E501
        """Show status of an async locale download  # noqa: E501

        Show status of already started async locale download. If the download is finished, the download link will be returned.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.locale_download_show(project_id, locale_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_id: Project ID (required)
        :param str locale_id: Locale ID (required)
        :param str id: ID (required)
        :param str x_phrase_app_otp: Two-Factor-Authentication token (optional)
        :param str if_modified_since: Last modified condition, see <a href=\"#overview--conditional-get-requests--http-caching\">Conditional GET requests / HTTP Caching</a> (optional)
        :param str if_none_match: ETag condition, see <a href=\"#overview--conditional-get-requests--http-caching\">Conditional GET requests / HTTP Caching</a> (optional)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: LocaleDownload
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.locale_download_show_with_http_info(project_id, locale_id, id, **kwargs)  # noqa: E501

    def locale_download_show_with_http_info(self, project_id, locale_id, id, **kwargs):  # noqa: E501
        """Show status of an async locale download  # noqa: E501

        Show status of already started async locale download. If the download is finished, the download link will be returned.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.locale_download_show_with_http_info(project_id, locale_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_id: Project ID (required)
        :param str locale_id: Locale ID (required)
        :param str id: ID (required)
        :param str x_phrase_app_otp: Two-Factor-Authentication token (optional)
        :param str if_modified_since: Last modified condition, see <a href=\"#overview--conditional-get-requests--http-caching\">Conditional GET requests / HTTP Caching</a> (optional)
        :param str if_none_match: ETag condition, see <a href=\"#overview--conditional-get-requests--http-caching\">Conditional GET requests / HTTP Caching</a> (optional)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(LocaleDownload, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'project_id',
            'locale_id',
            'id',
            'x_phrase_app_otp',
            'if_modified_since',
            'if_none_match'
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
                    " to method locale_download_show" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'project_id' is set
        if self.api_client.client_side_validation and ('project_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['project_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `project_id` when calling `locale_download_show`")  # noqa: E501
        # verify the required parameter 'locale_id' is set
        if self.api_client.client_side_validation and ('locale_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['locale_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `locale_id` when calling `locale_download_show`")  # noqa: E501
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `locale_download_show`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']  # noqa: E501
        if 'locale_id' in local_var_params:
            path_params['locale_id'] = local_var_params['locale_id']  # noqa: E501
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_phrase_app_otp' in local_var_params:
            header_params['X-PhraseApp-OTP'] = local_var_params['x_phrase_app_otp']  # noqa: E501
        if 'if_modified_since' in local_var_params:
            header_params['If-Modified-Since'] = local_var_params['if_modified_since']  # noqa: E501
        if 'if_none_match' in local_var_params:
            header_params['If-None-Match'] = local_var_params['if_none_match']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic', 'Token']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{project_id}/locales/{locale_id}/downloads/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LocaleDownload',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

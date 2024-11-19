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


class UploadsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def upload_create(self, project_id, file, file_format, locale_id, **kwargs):  # noqa: E501
        """Upload a new file  # noqa: E501

        Upload a new language file. Creates necessary resources in your project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upload_create(project_id, file, file_format, locale_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_id: Project ID (required)
        :param bytearray file: File to be imported (required)
        :param str file_format: File format. Auto-detected when possible and not specified. (required)
        :param str locale_id: Locale of the file's content. Can be the name or id of the locale. Preferred is id. (required)
        :param str x_phrase_app_otp: Two-Factor-Authentication token (optional)
        :param str branch: specify the branch to use
        :param str tags: List of tags separated by comma to be associated with the new keys contained in the upload.
        :param bool update_translations: Indicates whether existing translations should be updated with the file content.
        :param bool update_translation_keys: Pass `false` here to prevent new keys from being created and existing keys updated.
        :param bool update_translations_on_source_match: Update target translations only if the source translations of the uploaded multilingual file match the stored translations.
        :param bool update_descriptions: Existing key descriptions will be updated with the file content. Empty descriptions overwrite existing descriptions.
        :param bool convert_emoji: This option is obsolete. Providing the option will cause a bad request error.
        :param bool skip_upload_tags: Indicates whether the upload should not create upload tags.
        :param bool skip_unverification: Indicates whether the upload should unverify updated translations.
        :param str file_encoding: Enforces a specific encoding on the file contents. Valid options are \\\"UTF-8\\\", \\\"UTF-16\\\" and \\\"ISO-8859-1\\\".
        :param object locale_mapping: Mapping between locale names and translation columns. Required in some formats like CSV or XLSX.
        :param object format_options: Additional options available for specific formats. See our format guide for the [complete list](https://support.phrase.com/hc/en-us/articles/9652464547740-List-of-Supported-File-Types-Strings).
        :param bool autotranslate: If set, translations for the uploaded language will be fetched automatically.
        :param bool mark_reviewed: Indicated whether the imported translations should be marked as reviewed. This setting is available if the review workflow is enabled for the project.
        :param bool tag_only_affected_keys: Indicates whether only keys affected (created or updated) by the upload should be tagged. The default is `false`
        :param str translation_key_prefix: This prefix will be added to all uploaded translation key names to prevent collisions. Use a meaningful prefix related to your project or file to keep key names organized.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Upload
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.upload_create_with_http_info(project_id, file, file_format, locale_id, **kwargs)  # noqa: E501

    def upload_create_with_http_info(self, project_id, file, file_format, locale_id, **kwargs):  # noqa: E501
        """Upload a new file  # noqa: E501

        Upload a new language file. Creates necessary resources in your project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upload_create_with_http_info(project_id, file, file_format, locale_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_id: Project ID (required)
        :param bytearray file: File to be imported (required)
        :param str file_format: File format. Auto-detected when possible and not specified. (required)
        :param str locale_id: Locale of the file's content. Can be the name or id of the locale. Preferred is id. (required)
        :param str x_phrase_app_otp: Two-Factor-Authentication token (optional)
        :param str branch: specify the branch to use
        :param str tags: List of tags separated by comma to be associated with the new keys contained in the upload.
        :param bool update_translations: Indicates whether existing translations should be updated with the file content.
        :param bool update_translation_keys: Pass `false` here to prevent new keys from being created and existing keys updated.
        :param bool update_translations_on_source_match: Update target translations only if the source translations of the uploaded multilingual file match the stored translations.
        :param bool update_descriptions: Existing key descriptions will be updated with the file content. Empty descriptions overwrite existing descriptions.
        :param bool convert_emoji: This option is obsolete. Providing the option will cause a bad request error.
        :param bool skip_upload_tags: Indicates whether the upload should not create upload tags.
        :param bool skip_unverification: Indicates whether the upload should unverify updated translations.
        :param str file_encoding: Enforces a specific encoding on the file contents. Valid options are \\\"UTF-8\\\", \\\"UTF-16\\\" and \\\"ISO-8859-1\\\".
        :param object locale_mapping: Mapping between locale names and translation columns. Required in some formats like CSV or XLSX.
        :param object format_options: Additional options available for specific formats. See our format guide for the [complete list](https://support.phrase.com/hc/en-us/articles/9652464547740-List-of-Supported-File-Types-Strings).
        :param bool autotranslate: If set, translations for the uploaded language will be fetched automatically.
        :param bool mark_reviewed: Indicated whether the imported translations should be marked as reviewed. This setting is available if the review workflow is enabled for the project.
        :param bool tag_only_affected_keys: Indicates whether only keys affected (created or updated) by the upload should be tagged. The default is `false`
        :param str translation_key_prefix: This prefix will be added to all uploaded translation key names to prevent collisions. Use a meaningful prefix related to your project or file to keep key names organized.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Upload, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'project_id',
            'file',
            'file_format',
            'locale_id',
            'x_phrase_app_otp',
            'branch',
            'tags',
            'update_translations',
            'update_translation_keys',
            'update_translations_on_source_match',
            'update_descriptions',
            'convert_emoji',
            'skip_upload_tags',
            'skip_unverification',
            'file_encoding',
            'locale_mapping',
            'format_options',
            'autotranslate',
            'mark_reviewed',
            'tag_only_affected_keys',
            'translation_key_prefix'
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
                    " to method upload_create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'project_id' is set
        if self.api_client.client_side_validation and ('project_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['project_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `project_id` when calling `upload_create`")  # noqa: E501
        # verify the required parameter 'file' is set
        if self.api_client.client_side_validation and ('file' not in local_var_params or  # noqa: E501
                                                        local_var_params['file'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `file` when calling `upload_create`")  # noqa: E501
        # verify the required parameter 'file_format' is set
        if self.api_client.client_side_validation and ('file_format' not in local_var_params or  # noqa: E501
                                                        local_var_params['file_format'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `file_format` when calling `upload_create`")  # noqa: E501
        # verify the required parameter 'locale_id' is set
        if self.api_client.client_side_validation and ('locale_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['locale_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `locale_id` when calling `upload_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_phrase_app_otp' in local_var_params:
            header_params['X-PhraseApp-OTP'] = local_var_params['x_phrase_app_otp']  # noqa: E501

        form_params = []
        local_var_files = {}
        if 'branch' in local_var_params:
            form_params.append(('branch', local_var_params['branch']))  # noqa: E501
        if 'file' in local_var_params:
            local_var_files['file'] = local_var_params['file']  # noqa: E501
        if 'file_format' in local_var_params:
            form_params.append(('file_format', local_var_params['file_format']))  # noqa: E501
        if 'locale_id' in local_var_params:
            form_params.append(('locale_id', local_var_params['locale_id']))  # noqa: E501
        if 'tags' in local_var_params:
            form_params.append(('tags', local_var_params['tags']))  # noqa: E501
        if 'update_translations' in local_var_params:
            form_params.append(('update_translations', local_var_params['update_translations']))  # noqa: E501
        if 'update_translation_keys' in local_var_params:
            form_params.append(('update_translation_keys', local_var_params['update_translation_keys']))  # noqa: E501
        if 'update_translations_on_source_match' in local_var_params:
            form_params.append(('update_translations_on_source_match', local_var_params['update_translations_on_source_match']))  # noqa: E501
        if 'update_descriptions' in local_var_params:
            form_params.append(('update_descriptions', local_var_params['update_descriptions']))  # noqa: E501
        if 'convert_emoji' in local_var_params:
            form_params.append(('convert_emoji', local_var_params['convert_emoji']))  # noqa: E501
        if 'skip_upload_tags' in local_var_params:
            form_params.append(('skip_upload_tags', local_var_params['skip_upload_tags']))  # noqa: E501
        if 'skip_unverification' in local_var_params:
            form_params.append(('skip_unverification', local_var_params['skip_unverification']))  # noqa: E501
        if 'file_encoding' in local_var_params:
            form_params.append(('file_encoding', local_var_params['file_encoding']))  # noqa: E501
        if 'locale_mapping' in local_var_params:
            form_params.append(('locale_mapping', local_var_params['locale_mapping']))  # noqa: E501
        if 'format_options' in local_var_params:
            form_params.append(('format_options', local_var_params['format_options']))  # noqa: E501
        if 'autotranslate' in local_var_params:
            form_params.append(('autotranslate', local_var_params['autotranslate']))  # noqa: E501
        if 'mark_reviewed' in local_var_params:
            form_params.append(('mark_reviewed', local_var_params['mark_reviewed']))  # noqa: E501
        if 'tag_only_affected_keys' in local_var_params:
            form_params.append(('tag_only_affected_keys', local_var_params['tag_only_affected_keys']))  # noqa: E501
        if 'translation_key_prefix' in local_var_params:
            form_params.append(('translation_key_prefix', local_var_params['translation_key_prefix']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic', 'Token']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{project_id}/uploads', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Upload',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def upload_show(self, project_id, id, **kwargs):  # noqa: E501
        """Get a single upload  # noqa: E501

        View details and summary for a single upload.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upload_show(project_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_id: Project ID (required)
        :param str id: ID (required)
        :param str x_phrase_app_otp: Two-Factor-Authentication token (optional)
        :param str branch: specify the branch to use
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Upload
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.upload_show_with_http_info(project_id, id, **kwargs)  # noqa: E501

    def upload_show_with_http_info(self, project_id, id, **kwargs):  # noqa: E501
        """Get a single upload  # noqa: E501

        View details and summary for a single upload.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upload_show_with_http_info(project_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_id: Project ID (required)
        :param str id: ID (required)
        :param str x_phrase_app_otp: Two-Factor-Authentication token (optional)
        :param str branch: specify the branch to use
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Upload, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'project_id',
            'id',
            'x_phrase_app_otp',
            'branch'
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
                    " to method upload_show" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'project_id' is set
        if self.api_client.client_side_validation and ('project_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['project_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `project_id` when calling `upload_show`")  # noqa: E501
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `upload_show`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']  # noqa: E501
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []
        if 'branch' in local_var_params and local_var_params['branch'] is not None:  # noqa: E501
            query_params.append(('branch', local_var_params['branch']))  # noqa: E501

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
            '/projects/{project_id}/uploads/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Upload',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def uploads_list(self, project_id, **kwargs):  # noqa: E501
        """List uploads  # noqa: E501

        List all uploads for the given project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.uploads_list(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_id: Project ID (required)
        :param str x_phrase_app_otp: Two-Factor-Authentication token (optional)
        :param int page: Page number
        :param int per_page: Limit on the number of objects to be returned, between 1 and 100. 25 by default
        :param str branch: specify the branch to use
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: List[Upload]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.uploads_list_with_http_info(project_id, **kwargs)  # noqa: E501

    def uploads_list_with_http_info(self, project_id, **kwargs):  # noqa: E501
        """List uploads  # noqa: E501

        List all uploads for the given project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.uploads_list_with_http_info(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_id: Project ID (required)
        :param str x_phrase_app_otp: Two-Factor-Authentication token (optional)
        :param int page: Page number
        :param int per_page: Limit on the number of objects to be returned, between 1 and 100. 25 by default
        :param str branch: specify the branch to use
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(List[Upload], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'project_id',
            'x_phrase_app_otp',
            'page',
            'per_page',
            'branch'
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
                    " to method uploads_list" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'project_id' is set
        if self.api_client.client_side_validation and ('project_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['project_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `project_id` when calling `uploads_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']  # noqa: E501

        query_params = []
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'per_page' in local_var_params and local_var_params['per_page'] is not None:  # noqa: E501
            query_params.append(('per_page', local_var_params['per_page']))  # noqa: E501
        if 'branch' in local_var_params and local_var_params['branch'] is not None:  # noqa: E501
            query_params.append(('branch', local_var_params['branch']))  # noqa: E501

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
            '/projects/{project_id}/uploads', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='List[Upload]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

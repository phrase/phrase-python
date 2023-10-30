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


class JobTemplateLocalesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def job_template_locale_delete(self, project_id, job_template_id, job_template_locale_id, **kwargs):  # noqa: E501
        """Delete a job template locale  # noqa: E501

        Delete an existing job template locale.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.job_template_locale_delete(project_id, job_template_id, job_template_locale_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_id: Project ID (required)
        :param str job_template_id: Job Template ID (required)
        :param str job_template_locale_id: Job Template Locale ID (required)
        :param str x_phrase_app_otp: Two-Factor-Authentication token (optional)
        :param str branch: specify the branch to use
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
        return self.job_template_locale_delete_with_http_info(project_id, job_template_id, job_template_locale_id, **kwargs)  # noqa: E501

    def job_template_locale_delete_with_http_info(self, project_id, job_template_id, job_template_locale_id, **kwargs):  # noqa: E501
        """Delete a job template locale  # noqa: E501

        Delete an existing job template locale.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.job_template_locale_delete_with_http_info(project_id, job_template_id, job_template_locale_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_id: Project ID (required)
        :param str job_template_id: Job Template ID (required)
        :param str job_template_locale_id: Job Template Locale ID (required)
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
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'project_id',
            'job_template_id',
            'job_template_locale_id',
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
                    " to method job_template_locale_delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'project_id' is set
        if self.api_client.client_side_validation and ('project_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['project_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `project_id` when calling `job_template_locale_delete`")  # noqa: E501
        # verify the required parameter 'job_template_id' is set
        if self.api_client.client_side_validation and ('job_template_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['job_template_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `job_template_id` when calling `job_template_locale_delete`")  # noqa: E501
        # verify the required parameter 'job_template_locale_id' is set
        if self.api_client.client_side_validation and ('job_template_locale_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['job_template_locale_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `job_template_locale_id` when calling `job_template_locale_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']  # noqa: E501
        if 'job_template_id' in local_var_params:
            path_params['job_template_id'] = local_var_params['job_template_id']  # noqa: E501
        if 'job_template_locale_id' in local_var_params:
            path_params['job_template_locale_id'] = local_var_params['job_template_locale_id']  # noqa: E501

        query_params = []
        if 'branch' in local_var_params and local_var_params['branch'] is not None:  # noqa: E501
            query_params.append(('branch', local_var_params['branch']))  # noqa: E501

        header_params = {}
        if 'x_phrase_app_otp' in local_var_params:
            header_params['X-PhraseApp-OTP'] = local_var_params['x_phrase_app_otp']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Basic', 'Token']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{project_id}/job_templates/{job_template_id}/locales/{job_template_locale_id}', 'DELETE',
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

    def job_template_locale_show(self, project_id, job_template_id, job_template_locale_id, **kwargs):  # noqa: E501
        """Get a single job template locale  # noqa: E501

        Get a single job template locale for a given job template.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.job_template_locale_show(project_id, job_template_id, job_template_locale_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_id: Project ID (required)
        :param str job_template_id: Job Template ID (required)
        :param str job_template_locale_id: Job Template Locale ID (required)
        :param str x_phrase_app_otp: Two-Factor-Authentication token (optional)
        :param str branch: specify the branch to use
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: JobTemplateLocales
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.job_template_locale_show_with_http_info(project_id, job_template_id, job_template_locale_id, **kwargs)  # noqa: E501

    def job_template_locale_show_with_http_info(self, project_id, job_template_id, job_template_locale_id, **kwargs):  # noqa: E501
        """Get a single job template locale  # noqa: E501

        Get a single job template locale for a given job template.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.job_template_locale_show_with_http_info(project_id, job_template_id, job_template_locale_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_id: Project ID (required)
        :param str job_template_id: Job Template ID (required)
        :param str job_template_locale_id: Job Template Locale ID (required)
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
        :return: tuple(JobTemplateLocales, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'project_id',
            'job_template_id',
            'job_template_locale_id',
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
                    " to method job_template_locale_show" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'project_id' is set
        if self.api_client.client_side_validation and ('project_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['project_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `project_id` when calling `job_template_locale_show`")  # noqa: E501
        # verify the required parameter 'job_template_id' is set
        if self.api_client.client_side_validation and ('job_template_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['job_template_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `job_template_id` when calling `job_template_locale_show`")  # noqa: E501
        # verify the required parameter 'job_template_locale_id' is set
        if self.api_client.client_side_validation and ('job_template_locale_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['job_template_locale_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `job_template_locale_id` when calling `job_template_locale_show`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']  # noqa: E501
        if 'job_template_id' in local_var_params:
            path_params['job_template_id'] = local_var_params['job_template_id']  # noqa: E501
        if 'job_template_locale_id' in local_var_params:
            path_params['job_template_locale_id'] = local_var_params['job_template_locale_id']  # noqa: E501

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
            '/projects/{project_id}/job_templates/{job_template_id}/locales/{job_template_locale_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JobTemplateLocales',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def job_template_locale_update(self, project_id, job_template_id, job_template_locale_id, job_template_locale_update_parameters, **kwargs):  # noqa: E501
        """Update a job template locale  # noqa: E501

        Update an existing job template locale.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.job_template_locale_update(project_id, job_template_id, job_template_locale_id, job_template_locale_update_parameters, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_id: Project ID (required)
        :param str job_template_id: Job Template ID (required)
        :param str job_template_locale_id: Job Template Locale ID (required)
        :param JobTemplateLocaleUpdateParameters job_template_locale_update_parameters: (required)
        :param str x_phrase_app_otp: Two-Factor-Authentication token (optional)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: JobTemplateLocales
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.job_template_locale_update_with_http_info(project_id, job_template_id, job_template_locale_id, job_template_locale_update_parameters, **kwargs)  # noqa: E501

    def job_template_locale_update_with_http_info(self, project_id, job_template_id, job_template_locale_id, job_template_locale_update_parameters, **kwargs):  # noqa: E501
        """Update a job template locale  # noqa: E501

        Update an existing job template locale.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.job_template_locale_update_with_http_info(project_id, job_template_id, job_template_locale_id, job_template_locale_update_parameters, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_id: Project ID (required)
        :param str job_template_id: Job Template ID (required)
        :param str job_template_locale_id: Job Template Locale ID (required)
        :param JobTemplateLocaleUpdateParameters job_template_locale_update_parameters: (required)
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
        :return: tuple(JobTemplateLocales, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'project_id',
            'job_template_id',
            'job_template_locale_id',
            'job_template_locale_update_parameters',
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
                    " to method job_template_locale_update" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'project_id' is set
        if self.api_client.client_side_validation and ('project_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['project_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `project_id` when calling `job_template_locale_update`")  # noqa: E501
        # verify the required parameter 'job_template_id' is set
        if self.api_client.client_side_validation and ('job_template_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['job_template_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `job_template_id` when calling `job_template_locale_update`")  # noqa: E501
        # verify the required parameter 'job_template_locale_id' is set
        if self.api_client.client_side_validation and ('job_template_locale_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['job_template_locale_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `job_template_locale_id` when calling `job_template_locale_update`")  # noqa: E501
        # verify the required parameter 'job_template_locale_update_parameters' is set
        if self.api_client.client_side_validation and ('job_template_locale_update_parameters' not in local_var_params or  # noqa: E501
                                                        local_var_params['job_template_locale_update_parameters'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `job_template_locale_update_parameters` when calling `job_template_locale_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']  # noqa: E501
        if 'job_template_id' in local_var_params:
            path_params['job_template_id'] = local_var_params['job_template_id']  # noqa: E501
        if 'job_template_locale_id' in local_var_params:
            path_params['job_template_locale_id'] = local_var_params['job_template_locale_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_phrase_app_otp' in local_var_params:
            header_params['X-PhraseApp-OTP'] = local_var_params['x_phrase_app_otp']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'job_template_locale_update_parameters' in local_var_params:
            body_params = local_var_params['job_template_locale_update_parameters']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic', 'Token']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{project_id}/job_templates/{job_template_id}/locales/{job_template_locale_id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JobTemplateLocales',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def job_template_locales_create(self, project_id, job_template_id, job_template_locales_create_parameters, **kwargs):  # noqa: E501
        """Create a job template locale  # noqa: E501

        Create a new job template locale.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.job_template_locales_create(project_id, job_template_id, job_template_locales_create_parameters, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_id: Project ID (required)
        :param str job_template_id: Job Template ID (required)
        :param JobTemplateLocalesCreateParameters job_template_locales_create_parameters: (required)
        :param str x_phrase_app_otp: Two-Factor-Authentication token (optional)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: JobTemplateLocales
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.job_template_locales_create_with_http_info(project_id, job_template_id, job_template_locales_create_parameters, **kwargs)  # noqa: E501

    def job_template_locales_create_with_http_info(self, project_id, job_template_id, job_template_locales_create_parameters, **kwargs):  # noqa: E501
        """Create a job template locale  # noqa: E501

        Create a new job template locale.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.job_template_locales_create_with_http_info(project_id, job_template_id, job_template_locales_create_parameters, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_id: Project ID (required)
        :param str job_template_id: Job Template ID (required)
        :param JobTemplateLocalesCreateParameters job_template_locales_create_parameters: (required)
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
        :return: tuple(JobTemplateLocales, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'project_id',
            'job_template_id',
            'job_template_locales_create_parameters',
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
                    " to method job_template_locales_create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'project_id' is set
        if self.api_client.client_side_validation and ('project_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['project_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `project_id` when calling `job_template_locales_create`")  # noqa: E501
        # verify the required parameter 'job_template_id' is set
        if self.api_client.client_side_validation and ('job_template_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['job_template_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `job_template_id` when calling `job_template_locales_create`")  # noqa: E501
        # verify the required parameter 'job_template_locales_create_parameters' is set
        if self.api_client.client_side_validation and ('job_template_locales_create_parameters' not in local_var_params or  # noqa: E501
                                                        local_var_params['job_template_locales_create_parameters'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `job_template_locales_create_parameters` when calling `job_template_locales_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']  # noqa: E501
        if 'job_template_id' in local_var_params:
            path_params['job_template_id'] = local_var_params['job_template_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_phrase_app_otp' in local_var_params:
            header_params['X-PhraseApp-OTP'] = local_var_params['x_phrase_app_otp']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'job_template_locales_create_parameters' in local_var_params:
            body_params = local_var_params['job_template_locales_create_parameters']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic', 'Token']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{project_id}/job_templates/{job_template_id}/locales', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JobTemplateLocales',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def job_template_locales_list(self, project_id, job_template_id, **kwargs):  # noqa: E501
        """List job template locales  # noqa: E501

        List all job template locales for a given job template.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.job_template_locales_list(project_id, job_template_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_id: Project ID (required)
        :param str job_template_id: Job Template ID (required)
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
        :return: List[JobTemplateLocales]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.job_template_locales_list_with_http_info(project_id, job_template_id, **kwargs)  # noqa: E501

    def job_template_locales_list_with_http_info(self, project_id, job_template_id, **kwargs):  # noqa: E501
        """List job template locales  # noqa: E501

        List all job template locales for a given job template.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.job_template_locales_list_with_http_info(project_id, job_template_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_id: Project ID (required)
        :param str job_template_id: Job Template ID (required)
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
        :return: tuple(List[JobTemplateLocales], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'project_id',
            'job_template_id',
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
                    " to method job_template_locales_list" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'project_id' is set
        if self.api_client.client_side_validation and ('project_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['project_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `project_id` when calling `job_template_locales_list`")  # noqa: E501
        # verify the required parameter 'job_template_id' is set
        if self.api_client.client_side_validation and ('job_template_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['job_template_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `job_template_id` when calling `job_template_locales_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']  # noqa: E501
        if 'job_template_id' in local_var_params:
            path_params['job_template_id'] = local_var_params['job_template_id']  # noqa: E501

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
            '/projects/{project_id}/job_templates/{job_template_id}/locales', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='List[JobTemplateLocales]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

# coding: utf-8

"""
    Phrase Strings API Reference

    The version of the OpenAPI document: 2.0.0
    Contact: support@phrase.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from phrase_api.configuration import Configuration


class SearchInAccountParameters(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'query': 'str',
        'locale_code': 'str',
        'page': 'int',
        'per_page': 'int'
    }

    attribute_map = {
        'query': 'query',
        'locale_code': 'locale_code',
        'page': 'page',
        'per_page': 'per_page'
    }

    def __init__(self, query=None, locale_code=None, page=None, per_page=None, local_vars_configuration=None):  # noqa: E501
        """SearchInAccountParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._query = None
        self._locale_code = None
        self._page = None
        self._per_page = None
        self.discriminator = None

        if query is not None:
            self.query = query
        if locale_code is not None:
            self.locale_code = locale_code
        if page is not None:
            self.page = page
        if per_page is not None:
            self.per_page = per_page

    @property
    def query(self):
        """Gets the query of this SearchInAccountParameters.  # noqa: E501

        Search query  # noqa: E501

        :return: The query of this SearchInAccountParameters.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this SearchInAccountParameters.

        Search query  # noqa: E501

        :param query: The query of this SearchInAccountParameters.  # noqa: E501
        :type: str
        """

        self._query = query

    @property
    def locale_code(self):
        """Gets the locale_code of this SearchInAccountParameters.  # noqa: E501

        Locale code  # noqa: E501

        :return: The locale_code of this SearchInAccountParameters.  # noqa: E501
        :rtype: str
        """
        return self._locale_code

    @locale_code.setter
    def locale_code(self, locale_code):
        """Sets the locale_code of this SearchInAccountParameters.

        Locale code  # noqa: E501

        :param locale_code: The locale_code of this SearchInAccountParameters.  # noqa: E501
        :type: str
        """

        self._locale_code = locale_code

    @property
    def page(self):
        """Gets the page of this SearchInAccountParameters.  # noqa: E501

        Page  # noqa: E501

        :return: The page of this SearchInAccountParameters.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this SearchInAccountParameters.

        Page  # noqa: E501

        :param page: The page of this SearchInAccountParameters.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def per_page(self):
        """Gets the per_page of this SearchInAccountParameters.  # noqa: E501

        Number of results per page  # noqa: E501

        :return: The per_page of this SearchInAccountParameters.  # noqa: E501
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        """Sets the per_page of this SearchInAccountParameters.

        Number of results per page  # noqa: E501

        :param per_page: The per_page of this SearchInAccountParameters.  # noqa: E501
        :type: int
        """

        self._per_page = per_page

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SearchInAccountParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SearchInAccountParameters):
            return True

        return self.to_dict() != other.to_dict()

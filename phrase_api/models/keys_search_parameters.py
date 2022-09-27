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


class KeysSearchParameters(object):
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
        'branch': 'str',
        'sort': 'str',
        'order': 'str',
        'q': 'str',
        'locale_id': 'str'
    }

    attribute_map = {
        'branch': 'branch',
        'sort': 'sort',
        'order': 'order',
        'q': 'q',
        'locale_id': 'locale_id'
    }

    def __init__(self, branch=None, sort=None, order=None, q=None, locale_id=None, local_vars_configuration=None):  # noqa: E501
        """KeysSearchParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._branch = None
        self._sort = None
        self._order = None
        self._q = None
        self._locale_id = None
        self.discriminator = None

        if branch is not None:
            self.branch = branch
        if sort is not None:
            self.sort = sort
        if order is not None:
            self.order = order
        if q is not None:
            self.q = q
        if locale_id is not None:
            self.locale_id = locale_id

    @property
    def branch(self):
        """Gets the branch of this KeysSearchParameters.  # noqa: E501

        specify the branch to use  # noqa: E501

        :return: The branch of this KeysSearchParameters.  # noqa: E501
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this KeysSearchParameters.

        specify the branch to use  # noqa: E501

        :param branch: The branch of this KeysSearchParameters.  # noqa: E501
        :type: str
        """

        self._branch = branch

    @property
    def sort(self):
        """Gets the sort of this KeysSearchParameters.  # noqa: E501

        Sort by field. Can be one of: name, created_at, updated_at.  # noqa: E501

        :return: The sort of this KeysSearchParameters.  # noqa: E501
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this KeysSearchParameters.

        Sort by field. Can be one of: name, created_at, updated_at.  # noqa: E501

        :param sort: The sort of this KeysSearchParameters.  # noqa: E501
        :type: str
        """

        self._sort = sort

    @property
    def order(self):
        """Gets the order of this KeysSearchParameters.  # noqa: E501

        Order direction. Can be one of: asc, desc.  # noqa: E501

        :return: The order of this KeysSearchParameters.  # noqa: E501
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this KeysSearchParameters.

        Order direction. Can be one of: asc, desc.  # noqa: E501

        :param order: The order of this KeysSearchParameters.  # noqa: E501
        :type: str
        """

        self._order = order

    @property
    def q(self):
        """Gets the q of this KeysSearchParameters.  # noqa: E501

        Specify a query to do broad search for keys by name (including wildcards).<br><br> The following qualifiers are also supported in the search term:<br> <ul>   <li><code>ids:key_id,...</code> for queries on a comma-separated list of ids</li>   <li><code>name:key_name</code> for text queries on exact key names - spaces, commas, and colons  need to be escaped with double backslashes</li>   <li><code>tags:tag_name</code> to filter for keys with certain tags</li>   <li><code>translated:{true|false}</code> for translation status (also requires <code>locale_id</code> to be specified)</li>   <li><code>updated_at:{>=|<=}2013-02-21T00:00:00Z</code> for date range queries</li>   <li><code>unmentioned_in_upload:upload_id</code> to filter keys unmentioned within upload</li> </ul> Find more examples <a href=\"#overview--usage-examples\">here</a>.   # noqa: E501

        :return: The q of this KeysSearchParameters.  # noqa: E501
        :rtype: str
        """
        return self._q

    @q.setter
    def q(self, q):
        """Sets the q of this KeysSearchParameters.

        Specify a query to do broad search for keys by name (including wildcards).<br><br> The following qualifiers are also supported in the search term:<br> <ul>   <li><code>ids:key_id,...</code> for queries on a comma-separated list of ids</li>   <li><code>name:key_name</code> for text queries on exact key names - spaces, commas, and colons  need to be escaped with double backslashes</li>   <li><code>tags:tag_name</code> to filter for keys with certain tags</li>   <li><code>translated:{true|false}</code> for translation status (also requires <code>locale_id</code> to be specified)</li>   <li><code>updated_at:{>=|<=}2013-02-21T00:00:00Z</code> for date range queries</li>   <li><code>unmentioned_in_upload:upload_id</code> to filter keys unmentioned within upload</li> </ul> Find more examples <a href=\"#overview--usage-examples\">here</a>.   # noqa: E501

        :param q: The q of this KeysSearchParameters.  # noqa: E501
        :type: str
        """

        self._q = q

    @property
    def locale_id(self):
        """Gets the locale_id of this KeysSearchParameters.  # noqa: E501

        Locale used to determine the translation state of a key when filtering for untranslated or translated keys.  # noqa: E501

        :return: The locale_id of this KeysSearchParameters.  # noqa: E501
        :rtype: str
        """
        return self._locale_id

    @locale_id.setter
    def locale_id(self, locale_id):
        """Sets the locale_id of this KeysSearchParameters.

        Locale used to determine the translation state of a key when filtering for untranslated or translated keys.  # noqa: E501

        :param locale_id: The locale_id of this KeysSearchParameters.  # noqa: E501
        :type: str
        """

        self._locale_id = locale_id

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
        if not isinstance(other, KeysSearchParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KeysSearchParameters):
            return True

        return self.to_dict() != other.to_dict()

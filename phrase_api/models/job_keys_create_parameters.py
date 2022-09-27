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


class JobKeysCreateParameters(object):
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
        'translation_key_ids': 'list[str]'
    }

    attribute_map = {
        'branch': 'branch',
        'translation_key_ids': 'translation_key_ids'
    }

    def __init__(self, branch=None, translation_key_ids=None, local_vars_configuration=None):  # noqa: E501
        """JobKeysCreateParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._branch = None
        self._translation_key_ids = None
        self.discriminator = None

        if branch is not None:
            self.branch = branch
        if translation_key_ids is not None:
            self.translation_key_ids = translation_key_ids

    @property
    def branch(self):
        """Gets the branch of this JobKeysCreateParameters.  # noqa: E501

        specify the branch to use  # noqa: E501

        :return: The branch of this JobKeysCreateParameters.  # noqa: E501
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this JobKeysCreateParameters.

        specify the branch to use  # noqa: E501

        :param branch: The branch of this JobKeysCreateParameters.  # noqa: E501
        :type: str
        """

        self._branch = branch

    @property
    def translation_key_ids(self):
        """Gets the translation_key_ids of this JobKeysCreateParameters.  # noqa: E501

        ids of keys that should added to the job  # noqa: E501

        :return: The translation_key_ids of this JobKeysCreateParameters.  # noqa: E501
        :rtype: list[str]
        """
        return self._translation_key_ids

    @translation_key_ids.setter
    def translation_key_ids(self, translation_key_ids):
        """Sets the translation_key_ids of this JobKeysCreateParameters.

        ids of keys that should added to the job  # noqa: E501

        :param translation_key_ids: The translation_key_ids of this JobKeysCreateParameters.  # noqa: E501
        :type: list[str]
        """

        self._translation_key_ids = translation_key_ids

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
        if not isinstance(other, JobKeysCreateParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JobKeysCreateParameters):
            return True

        return self.to_dict() != other.to_dict()

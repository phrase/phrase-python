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


class KeyLinksBatchDestroyParameters(object):
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
        'child_key_ids': 'List[str]',
        'unlink_parent': 'bool'
    }

    attribute_map = {
        'child_key_ids': 'child_key_ids',
        'unlink_parent': 'unlink_parent'
    }

    def __init__(self, child_key_ids=None, unlink_parent=False, local_vars_configuration=None):  # noqa: E501
        """KeyLinksBatchDestroyParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._child_key_ids = None
        self._unlink_parent = None
        self.discriminator = None

        self.child_key_ids = child_key_ids
        if unlink_parent is not None:
            self.unlink_parent = unlink_parent

    @property
    def child_key_ids(self):
        """Gets the child_key_ids of this KeyLinksBatchDestroyParameters.  # noqa: E501

        The IDs of the child keys to unlink from the parent key.  # noqa: E501

        :return: The child_key_ids of this KeyLinksBatchDestroyParameters.  # noqa: E501
        :rtype: List[str]
        """
        return self._child_key_ids

    @child_key_ids.setter
    def child_key_ids(self, child_key_ids):
        """Sets the child_key_ids of this KeyLinksBatchDestroyParameters.

        The IDs of the child keys to unlink from the parent key.  # noqa: E501

        :param child_key_ids: The child_key_ids of this KeyLinksBatchDestroyParameters.  # noqa: E501
        :type: List[str]
        """
        if self.local_vars_configuration.client_side_validation and child_key_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `child_key_ids`, must not be `None`")  # noqa: E501

        self._child_key_ids = child_key_ids

    @property
    def unlink_parent(self):
        """Gets the unlink_parent of this KeyLinksBatchDestroyParameters.  # noqa: E501

        Whether to unlink the parent key as well and unmark it as linked-key.  # noqa: E501

        :return: The unlink_parent of this KeyLinksBatchDestroyParameters.  # noqa: E501
        :rtype: bool
        """
        return self._unlink_parent

    @unlink_parent.setter
    def unlink_parent(self, unlink_parent):
        """Sets the unlink_parent of this KeyLinksBatchDestroyParameters.

        Whether to unlink the parent key as well and unmark it as linked-key.  # noqa: E501

        :param unlink_parent: The unlink_parent of this KeyLinksBatchDestroyParameters.  # noqa: E501
        :type: bool
        """

        self._unlink_parent = unlink_parent

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
        if not isinstance(other, KeyLinksBatchDestroyParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KeyLinksBatchDestroyParameters):
            return True

        return self.to_dict() != other.to_dict()

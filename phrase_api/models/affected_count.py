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


class AffectedCount(object):
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
        'records_affected': 'int'
    }

    attribute_map = {
        'records_affected': 'records_affected'
    }

    def __init__(self, records_affected=None, local_vars_configuration=None):  # noqa: E501
        """AffectedCount - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._records_affected = None
        self.discriminator = None

        if records_affected is not None:
            self.records_affected = records_affected

    @property
    def records_affected(self):
        """Gets the records_affected of this AffectedCount.  # noqa: E501


        :return: The records_affected of this AffectedCount.  # noqa: E501
        :rtype: int
        """
        return self._records_affected

    @records_affected.setter
    def records_affected(self, records_affected):
        """Sets the records_affected of this AffectedCount.


        :param records_affected: The records_affected of this AffectedCount.  # noqa: E501
        :type: int
        """

        self._records_affected = records_affected

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
        if not isinstance(other, AffectedCount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AffectedCount):
            return True

        return self.to_dict() != other.to_dict()

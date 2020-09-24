# coding: utf-8

"""
    Phrase API Reference

    The version of the OpenAPI document: 2.0.0
    Contact: support@phrase.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from phrase_api.configuration import Configuration


class InlineResponse422Errors(object):
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
        'resource': 'str',
        'field': 'str',
        'message': 'str'
    }

    attribute_map = {
        'resource': 'resource',
        'field': 'field',
        'message': 'message'
    }

    def __init__(self, resource=None, field=None, message=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse422Errors - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._resource = None
        self._field = None
        self._message = None
        self.discriminator = None

        if resource is not None:
            self.resource = resource
        if field is not None:
            self.field = field
        if message is not None:
            self.message = message

    @property
    def resource(self):
        """Gets the resource of this InlineResponse422Errors.  # noqa: E501


        :return: The resource of this InlineResponse422Errors.  # noqa: E501
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this InlineResponse422Errors.


        :param resource: The resource of this InlineResponse422Errors.  # noqa: E501
        :type: str
        """

        self._resource = resource

    @property
    def field(self):
        """Gets the field of this InlineResponse422Errors.  # noqa: E501


        :return: The field of this InlineResponse422Errors.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this InlineResponse422Errors.


        :param field: The field of this InlineResponse422Errors.  # noqa: E501
        :type: str
        """

        self._field = field

    @property
    def message(self):
        """Gets the message of this InlineResponse422Errors.  # noqa: E501


        :return: The message of this InlineResponse422Errors.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this InlineResponse422Errors.


        :param message: The message of this InlineResponse422Errors.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if not isinstance(other, InlineResponse422Errors):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse422Errors):
            return True

        return self.to_dict() != other.to_dict()

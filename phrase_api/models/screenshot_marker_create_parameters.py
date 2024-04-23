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


class ScreenshotMarkerCreateParameters(object):
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
        'key_id': 'str',
        'presentation': 'str'
    }

    attribute_map = {
        'branch': 'branch',
        'key_id': 'key_id',
        'presentation': 'presentation'
    }

    def __init__(self, branch=None, key_id=None, presentation=None, local_vars_configuration=None):  # noqa: E501
        """ScreenshotMarkerCreateParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._branch = None
        self._key_id = None
        self._presentation = None
        self.discriminator = None

        if branch is not None:
            self.branch = branch
        self.key_id = key_id
        if presentation is not None:
            self.presentation = presentation

    @property
    def branch(self):
        """Gets the branch of this ScreenshotMarkerCreateParameters.  # noqa: E501

        specify the branch to use  # noqa: E501

        :return: The branch of this ScreenshotMarkerCreateParameters.  # noqa: E501
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this ScreenshotMarkerCreateParameters.

        specify the branch to use  # noqa: E501

        :param branch: The branch of this ScreenshotMarkerCreateParameters.  # noqa: E501
        :type: str
        """

        self._branch = branch

    @property
    def key_id(self):
        """Gets the key_id of this ScreenshotMarkerCreateParameters.  # noqa: E501

        Specify the Key ID which should be highlighted on the specified screenshot. The Key must belong to the project.  # noqa: E501

        :return: The key_id of this ScreenshotMarkerCreateParameters.  # noqa: E501
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """Sets the key_id of this ScreenshotMarkerCreateParameters.

        Specify the Key ID which should be highlighted on the specified screenshot. The Key must belong to the project.  # noqa: E501

        :param key_id: The key_id of this ScreenshotMarkerCreateParameters.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and key_id is None:  # noqa: E501
            raise ValueError("Invalid value for `key_id`, must not be `None`")  # noqa: E501

        self._key_id = key_id

    @property
    def presentation(self):
        """Gets the presentation of this ScreenshotMarkerCreateParameters.  # noqa: E501

        Presentation details of the screenshot marker in JSON format.<br/><br/>Each Screenshot Marker is represented as a rectangular shaped highlight box with the name of the specified Key attached. You can specify the marker position on the screenshot (<code>x</code>-axis and <code>y</code>-axis in pixels) from the top left corner of the screenshot and the dimensions of the marker itself (<code>w</code> and <code>h</code> in pixels).  # noqa: E501

        :return: The presentation of this ScreenshotMarkerCreateParameters.  # noqa: E501
        :rtype: str
        """
        return self._presentation

    @presentation.setter
    def presentation(self, presentation):
        """Sets the presentation of this ScreenshotMarkerCreateParameters.

        Presentation details of the screenshot marker in JSON format.<br/><br/>Each Screenshot Marker is represented as a rectangular shaped highlight box with the name of the specified Key attached. You can specify the marker position on the screenshot (<code>x</code>-axis and <code>y</code>-axis in pixels) from the top left corner of the screenshot and the dimensions of the marker itself (<code>w</code> and <code>h</code> in pixels).  # noqa: E501

        :param presentation: The presentation of this ScreenshotMarkerCreateParameters.  # noqa: E501
        :type: str
        """

        self._presentation = presentation

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
        if not isinstance(other, ScreenshotMarkerCreateParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScreenshotMarkerCreateParameters):
            return True

        return self.to_dict() != other.to_dict()

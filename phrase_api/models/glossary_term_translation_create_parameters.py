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


class GlossaryTermTranslationCreateParameters(object):
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
        'locale_code': 'str',
        'content': 'str'
    }

    attribute_map = {
        'locale_code': 'locale_code',
        'content': 'content'
    }

    def __init__(self, locale_code=None, content=None, local_vars_configuration=None):  # noqa: E501
        """GlossaryTermTranslationCreateParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._locale_code = None
        self._content = None
        self.discriminator = None

        self.locale_code = locale_code
        self.content = content

    @property
    def locale_code(self):
        """Gets the locale_code of this GlossaryTermTranslationCreateParameters.  # noqa: E501

        Identifies the language for this translation  # noqa: E501

        :return: The locale_code of this GlossaryTermTranslationCreateParameters.  # noqa: E501
        :rtype: str
        """
        return self._locale_code

    @locale_code.setter
    def locale_code(self, locale_code):
        """Sets the locale_code of this GlossaryTermTranslationCreateParameters.

        Identifies the language for this translation  # noqa: E501

        :param locale_code: The locale_code of this GlossaryTermTranslationCreateParameters.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and locale_code is None:  # noqa: E501
            raise ValueError("Invalid value for `locale_code`, must not be `None`")  # noqa: E501

        self._locale_code = locale_code

    @property
    def content(self):
        """Gets the content of this GlossaryTermTranslationCreateParameters.  # noqa: E501

        The content of the translation  # noqa: E501

        :return: The content of this GlossaryTermTranslationCreateParameters.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this GlossaryTermTranslationCreateParameters.

        The content of the translation  # noqa: E501

        :param content: The content of this GlossaryTermTranslationCreateParameters.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and content is None:  # noqa: E501
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

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
        if not isinstance(other, GlossaryTermTranslationCreateParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GlossaryTermTranslationCreateParameters):
            return True

        return self.to_dict() != other.to_dict()

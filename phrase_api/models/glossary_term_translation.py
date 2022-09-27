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


class GlossaryTermTranslation(object):
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
        'id': 'str',
        'locale_code': 'str',
        'content': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'locale_code': 'locale_code',
        'content': 'content',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, locale_code=None, content=None, created_at=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """GlossaryTermTranslation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._locale_code = None
        self._content = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if locale_code is not None:
            self.locale_code = locale_code
        if content is not None:
            self.content = content
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this GlossaryTermTranslation.  # noqa: E501


        :return: The id of this GlossaryTermTranslation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GlossaryTermTranslation.


        :param id: The id of this GlossaryTermTranslation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def locale_code(self):
        """Gets the locale_code of this GlossaryTermTranslation.  # noqa: E501


        :return: The locale_code of this GlossaryTermTranslation.  # noqa: E501
        :rtype: str
        """
        return self._locale_code

    @locale_code.setter
    def locale_code(self, locale_code):
        """Sets the locale_code of this GlossaryTermTranslation.


        :param locale_code: The locale_code of this GlossaryTermTranslation.  # noqa: E501
        :type: str
        """

        self._locale_code = locale_code

    @property
    def content(self):
        """Gets the content of this GlossaryTermTranslation.  # noqa: E501


        :return: The content of this GlossaryTermTranslation.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this GlossaryTermTranslation.


        :param content: The content of this GlossaryTermTranslation.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def created_at(self):
        """Gets the created_at of this GlossaryTermTranslation.  # noqa: E501


        :return: The created_at of this GlossaryTermTranslation.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this GlossaryTermTranslation.


        :param created_at: The created_at of this GlossaryTermTranslation.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this GlossaryTermTranslation.  # noqa: E501


        :return: The updated_at of this GlossaryTermTranslation.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this GlossaryTermTranslation.


        :param updated_at: The updated_at of this GlossaryTermTranslation.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
        if not isinstance(other, GlossaryTermTranslation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GlossaryTermTranslation):
            return True

        return self.to_dict() != other.to_dict()

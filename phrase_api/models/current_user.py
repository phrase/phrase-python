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


class CurrentUser(object):
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
        'username': 'str',
        'name': 'str',
        'email': 'str',
        'position': 'str',
        'language': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'username': 'username',
        'name': 'name',
        'email': 'email',
        'position': 'position',
        'language': 'language',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, username=None, name=None, email=None, position=None, language=None, created_at=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """CurrentUser - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._username = None
        self._name = None
        self._email = None
        self._position = None
        self._language = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if username is not None:
            self.username = username
        if name is not None:
            self.name = name
        if email is not None:
            self.email = email
        if position is not None:
            self.position = position
        if language is not None:
            self.language = language
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this CurrentUser.  # noqa: E501


        :return: The id of this CurrentUser.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CurrentUser.


        :param id: The id of this CurrentUser.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def username(self):
        """Gets the username of this CurrentUser.  # noqa: E501


        :return: The username of this CurrentUser.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this CurrentUser.


        :param username: The username of this CurrentUser.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def name(self):
        """Gets the name of this CurrentUser.  # noqa: E501


        :return: The name of this CurrentUser.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CurrentUser.


        :param name: The name of this CurrentUser.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def email(self):
        """Gets the email of this CurrentUser.  # noqa: E501


        :return: The email of this CurrentUser.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CurrentUser.


        :param email: The email of this CurrentUser.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def position(self):
        """Gets the position of this CurrentUser.  # noqa: E501


        :return: The position of this CurrentUser.  # noqa: E501
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this CurrentUser.


        :param position: The position of this CurrentUser.  # noqa: E501
        :type: str
        """

        self._position = position

    @property
    def language(self):
        """Gets the language of this CurrentUser.  # noqa: E501


        :return: The language of this CurrentUser.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this CurrentUser.


        :param language: The language of this CurrentUser.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def created_at(self):
        """Gets the created_at of this CurrentUser.  # noqa: E501


        :return: The created_at of this CurrentUser.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CurrentUser.


        :param created_at: The created_at of this CurrentUser.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this CurrentUser.  # noqa: E501


        :return: The updated_at of this CurrentUser.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this CurrentUser.


        :param updated_at: The updated_at of this CurrentUser.  # noqa: E501
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
        if not isinstance(other, CurrentUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CurrentUser):
            return True

        return self.to_dict() != other.to_dict()

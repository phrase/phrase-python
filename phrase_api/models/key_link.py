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


class KeyLink(object):
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
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'created_by': 'UserPreview',
        'updated_by': 'UserPreview',
        'account': 'Account',
        'parent': 'KeyPreview',
        'children': 'List[KeyPreview]'
    }

    attribute_map = {
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'created_by': 'created_by',
        'updated_by': 'updated_by',
        'account': 'account',
        'parent': 'parent',
        'children': 'children'
    }

    def __init__(self, created_at=None, updated_at=None, created_by=None, updated_by=None, account=None, parent=None, children=None, local_vars_configuration=None):  # noqa: E501
        """KeyLink - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._created_at = None
        self._updated_at = None
        self._created_by = None
        self._updated_by = None
        self._account = None
        self._parent = None
        self._children = None
        self.discriminator = None

        self.created_at = created_at
        self.updated_at = updated_at
        self.created_by = created_by
        self.updated_by = updated_by
        self.account = account
        self.parent = parent
        self.children = children

    @property
    def created_at(self):
        """Gets the created_at of this KeyLink.  # noqa: E501

        The timestamp when the link was created.  # noqa: E501

        :return: The created_at of this KeyLink.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this KeyLink.

        The timestamp when the link was created.  # noqa: E501

        :param created_at: The created_at of this KeyLink.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this KeyLink.  # noqa: E501

        The timestamp when the link was last updated.  # noqa: E501

        :return: The updated_at of this KeyLink.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this KeyLink.

        The timestamp when the link was last updated.  # noqa: E501

        :param updated_at: The updated_at of this KeyLink.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def created_by(self):
        """Gets the created_by of this KeyLink.  # noqa: E501


        :return: The created_by of this KeyLink.  # noqa: E501
        :rtype: UserPreview
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this KeyLink.


        :param created_by: The created_by of this KeyLink.  # noqa: E501
        :type: UserPreview
        """
        if self.local_vars_configuration.client_side_validation and created_by is None:  # noqa: E501
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by

    @property
    def updated_by(self):
        """Gets the updated_by of this KeyLink.  # noqa: E501


        :return: The updated_by of this KeyLink.  # noqa: E501
        :rtype: UserPreview
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this KeyLink.


        :param updated_by: The updated_by of this KeyLink.  # noqa: E501
        :type: UserPreview
        """
        if self.local_vars_configuration.client_side_validation and updated_by is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_by`, must not be `None`")  # noqa: E501

        self._updated_by = updated_by

    @property
    def account(self):
        """Gets the account of this KeyLink.  # noqa: E501


        :return: The account of this KeyLink.  # noqa: E501
        :rtype: Account
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this KeyLink.


        :param account: The account of this KeyLink.  # noqa: E501
        :type: Account
        """
        if self.local_vars_configuration.client_side_validation and account is None:  # noqa: E501
            raise ValueError("Invalid value for `account`, must not be `None`")  # noqa: E501

        self._account = account

    @property
    def parent(self):
        """Gets the parent of this KeyLink.  # noqa: E501


        :return: The parent of this KeyLink.  # noqa: E501
        :rtype: KeyPreview
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this KeyLink.


        :param parent: The parent of this KeyLink.  # noqa: E501
        :type: KeyPreview
        """
        if self.local_vars_configuration.client_side_validation and parent is None:  # noqa: E501
            raise ValueError("Invalid value for `parent`, must not be `None`")  # noqa: E501

        self._parent = parent

    @property
    def children(self):
        """Gets the children of this KeyLink.  # noqa: E501

        The child translation keys linked to the parent.  # noqa: E501

        :return: The children of this KeyLink.  # noqa: E501
        :rtype: List[KeyPreview]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this KeyLink.

        The child translation keys linked to the parent.  # noqa: E501

        :param children: The children of this KeyLink.  # noqa: E501
        :type: List[KeyPreview]
        """
        if self.local_vars_configuration.client_side_validation and children is None:  # noqa: E501
            raise ValueError("Invalid value for `children`, must not be `None`")  # noqa: E501

        self._children = children

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
        if not isinstance(other, KeyLink):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KeyLink):
            return True

        return self.to_dict() != other.to_dict()

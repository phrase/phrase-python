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


class Invitation(object):
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
        'email': 'str',
        'role': 'str',
        'state': 'str',
        'projects': 'list[ProjectShort]',
        'locales': 'list[LocalePreview]',
        'teams': 'list[TeamShort]',
        'default_locale_codes': 'list[str]',
        'permissions': 'object',
        'locale_ids': 'list[str]',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'accepted_at': 'datetime',
        'spaces': 'list[Space]',
        'project_role': 'list[MemberProjectDetailProjectRoles]'
    }

    attribute_map = {
        'id': 'id',
        'email': 'email',
        'role': 'role',
        'state': 'state',
        'projects': 'projects',
        'locales': 'locales',
        'teams': 'teams',
        'default_locale_codes': 'default_locale_codes',
        'permissions': 'permissions',
        'locale_ids': 'locale_ids',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'accepted_at': 'accepted_at',
        'spaces': 'spaces',
        'project_role': 'project_role'
    }

    def __init__(self, id=None, email=None, role=None, state=None, projects=None, locales=None, teams=None, default_locale_codes=None, permissions=None, locale_ids=None, created_at=None, updated_at=None, accepted_at=None, spaces=None, project_role=None, local_vars_configuration=None):  # noqa: E501
        """Invitation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._email = None
        self._role = None
        self._state = None
        self._projects = None
        self._locales = None
        self._teams = None
        self._default_locale_codes = None
        self._permissions = None
        self._locale_ids = None
        self._created_at = None
        self._updated_at = None
        self._accepted_at = None
        self._spaces = None
        self._project_role = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if email is not None:
            self.email = email
        if role is not None:
            self.role = role
        if state is not None:
            self.state = state
        if projects is not None:
            self.projects = projects
        if locales is not None:
            self.locales = locales
        if teams is not None:
            self.teams = teams
        if default_locale_codes is not None:
            self.default_locale_codes = default_locale_codes
        if permissions is not None:
            self.permissions = permissions
        if locale_ids is not None:
            self.locale_ids = locale_ids
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if accepted_at is not None:
            self.accepted_at = accepted_at
        if spaces is not None:
            self.spaces = spaces
        if project_role is not None:
            self.project_role = project_role

    @property
    def id(self):
        """Gets the id of this Invitation.  # noqa: E501


        :return: The id of this Invitation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Invitation.


        :param id: The id of this Invitation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def email(self):
        """Gets the email of this Invitation.  # noqa: E501


        :return: The email of this Invitation.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Invitation.


        :param email: The email of this Invitation.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def role(self):
        """Gets the role of this Invitation.  # noqa: E501


        :return: The role of this Invitation.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this Invitation.


        :param role: The role of this Invitation.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def state(self):
        """Gets the state of this Invitation.  # noqa: E501


        :return: The state of this Invitation.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Invitation.


        :param state: The state of this Invitation.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def projects(self):
        """Gets the projects of this Invitation.  # noqa: E501


        :return: The projects of this Invitation.  # noqa: E501
        :rtype: list[ProjectShort]
        """
        return self._projects

    @projects.setter
    def projects(self, projects):
        """Sets the projects of this Invitation.


        :param projects: The projects of this Invitation.  # noqa: E501
        :type: list[ProjectShort]
        """

        self._projects = projects

    @property
    def locales(self):
        """Gets the locales of this Invitation.  # noqa: E501


        :return: The locales of this Invitation.  # noqa: E501
        :rtype: list[LocalePreview]
        """
        return self._locales

    @locales.setter
    def locales(self, locales):
        """Sets the locales of this Invitation.


        :param locales: The locales of this Invitation.  # noqa: E501
        :type: list[LocalePreview]
        """

        self._locales = locales

    @property
    def teams(self):
        """Gets the teams of this Invitation.  # noqa: E501


        :return: The teams of this Invitation.  # noqa: E501
        :rtype: list[TeamShort]
        """
        return self._teams

    @teams.setter
    def teams(self, teams):
        """Sets the teams of this Invitation.


        :param teams: The teams of this Invitation.  # noqa: E501
        :type: list[TeamShort]
        """

        self._teams = teams

    @property
    def default_locale_codes(self):
        """Gets the default_locale_codes of this Invitation.  # noqa: E501


        :return: The default_locale_codes of this Invitation.  # noqa: E501
        :rtype: list[str]
        """
        return self._default_locale_codes

    @default_locale_codes.setter
    def default_locale_codes(self, default_locale_codes):
        """Sets the default_locale_codes of this Invitation.


        :param default_locale_codes: The default_locale_codes of this Invitation.  # noqa: E501
        :type: list[str]
        """

        self._default_locale_codes = default_locale_codes

    @property
    def permissions(self):
        """Gets the permissions of this Invitation.  # noqa: E501


        :return: The permissions of this Invitation.  # noqa: E501
        :rtype: object
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this Invitation.


        :param permissions: The permissions of this Invitation.  # noqa: E501
        :type: object
        """

        self._permissions = permissions

    @property
    def locale_ids(self):
        """Gets the locale_ids of this Invitation.  # noqa: E501


        :return: The locale_ids of this Invitation.  # noqa: E501
        :rtype: list[str]
        """
        return self._locale_ids

    @locale_ids.setter
    def locale_ids(self, locale_ids):
        """Sets the locale_ids of this Invitation.


        :param locale_ids: The locale_ids of this Invitation.  # noqa: E501
        :type: list[str]
        """

        self._locale_ids = locale_ids

    @property
    def created_at(self):
        """Gets the created_at of this Invitation.  # noqa: E501


        :return: The created_at of this Invitation.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Invitation.


        :param created_at: The created_at of this Invitation.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Invitation.  # noqa: E501


        :return: The updated_at of this Invitation.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Invitation.


        :param updated_at: The updated_at of this Invitation.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def accepted_at(self):
        """Gets the accepted_at of this Invitation.  # noqa: E501


        :return: The accepted_at of this Invitation.  # noqa: E501
        :rtype: datetime
        """
        return self._accepted_at

    @accepted_at.setter
    def accepted_at(self, accepted_at):
        """Sets the accepted_at of this Invitation.


        :param accepted_at: The accepted_at of this Invitation.  # noqa: E501
        :type: datetime
        """

        self._accepted_at = accepted_at

    @property
    def spaces(self):
        """Gets the spaces of this Invitation.  # noqa: E501


        :return: The spaces of this Invitation.  # noqa: E501
        :rtype: list[Space]
        """
        return self._spaces

    @spaces.setter
    def spaces(self, spaces):
        """Sets the spaces of this Invitation.


        :param spaces: The spaces of this Invitation.  # noqa: E501
        :type: list[Space]
        """

        self._spaces = spaces

    @property
    def project_role(self):
        """Gets the project_role of this Invitation.  # noqa: E501


        :return: The project_role of this Invitation.  # noqa: E501
        :rtype: list[MemberProjectDetailProjectRoles]
        """
        return self._project_role

    @project_role.setter
    def project_role(self, project_role):
        """Sets the project_role of this Invitation.


        :param project_role: The project_role of this Invitation.  # noqa: E501
        :type: list[MemberProjectDetailProjectRoles]
        """

        self._project_role = project_role

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
        if not isinstance(other, Invitation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Invitation):
            return True

        return self.to_dict() != other.to_dict()

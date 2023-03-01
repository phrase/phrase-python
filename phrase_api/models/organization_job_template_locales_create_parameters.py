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


class OrganizationJobTemplateLocalesCreateParameters(object):
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
        'locale_name': 'str',
        'locale_code': 'str',
        'user_ids': 'list[str]',
        'reviewer_ids': 'list[str]',
        'translator_team_ids': 'list[str]',
        'reviewer_team_ids': 'list[str]'
    }

    attribute_map = {
        'locale_name': 'locale_name',
        'locale_code': 'locale_code',
        'user_ids': 'user_ids',
        'reviewer_ids': 'reviewer_ids',
        'translator_team_ids': 'translator_team_ids',
        'reviewer_team_ids': 'reviewer_team_ids'
    }

    def __init__(self, locale_name=None, locale_code=None, user_ids=None, reviewer_ids=None, translator_team_ids=None, reviewer_team_ids=None, local_vars_configuration=None):  # noqa: E501
        """OrganizationJobTemplateLocalesCreateParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._locale_name = None
        self._locale_code = None
        self._user_ids = None
        self._reviewer_ids = None
        self._translator_team_ids = None
        self._reviewer_team_ids = None
        self.discriminator = None

        self.locale_name = locale_name
        self.locale_code = locale_code
        if user_ids is not None:
            self.user_ids = user_ids
        if reviewer_ids is not None:
            self.reviewer_ids = reviewer_ids
        if translator_team_ids is not None:
            self.translator_team_ids = translator_team_ids
        if reviewer_team_ids is not None:
            self.reviewer_team_ids = reviewer_team_ids

    @property
    def locale_name(self):
        """Gets the locale_name of this OrganizationJobTemplateLocalesCreateParameters.  # noqa: E501

        locale name  # noqa: E501

        :return: The locale_name of this OrganizationJobTemplateLocalesCreateParameters.  # noqa: E501
        :rtype: str
        """
        return self._locale_name

    @locale_name.setter
    def locale_name(self, locale_name):
        """Sets the locale_name of this OrganizationJobTemplateLocalesCreateParameters.

        locale name  # noqa: E501

        :param locale_name: The locale_name of this OrganizationJobTemplateLocalesCreateParameters.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and locale_name is None:  # noqa: E501
            raise ValueError("Invalid value for `locale_name`, must not be `None`")  # noqa: E501

        self._locale_name = locale_name

    @property
    def locale_code(self):
        """Gets the locale_code of this OrganizationJobTemplateLocalesCreateParameters.  # noqa: E501

        locale code  # noqa: E501

        :return: The locale_code of this OrganizationJobTemplateLocalesCreateParameters.  # noqa: E501
        :rtype: str
        """
        return self._locale_code

    @locale_code.setter
    def locale_code(self, locale_code):
        """Sets the locale_code of this OrganizationJobTemplateLocalesCreateParameters.

        locale code  # noqa: E501

        :param locale_code: The locale_code of this OrganizationJobTemplateLocalesCreateParameters.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and locale_code is None:  # noqa: E501
            raise ValueError("Invalid value for `locale_code`, must not be `None`")  # noqa: E501

        self._locale_code = locale_code

    @property
    def user_ids(self):
        """Gets the user_ids of this OrganizationJobTemplateLocalesCreateParameters.  # noqa: E501

        Array of user ids to be assigned to the job template locale  # noqa: E501

        :return: The user_ids of this OrganizationJobTemplateLocalesCreateParameters.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_ids

    @user_ids.setter
    def user_ids(self, user_ids):
        """Sets the user_ids of this OrganizationJobTemplateLocalesCreateParameters.

        Array of user ids to be assigned to the job template locale  # noqa: E501

        :param user_ids: The user_ids of this OrganizationJobTemplateLocalesCreateParameters.  # noqa: E501
        :type: list[str]
        """

        self._user_ids = user_ids

    @property
    def reviewer_ids(self):
        """Gets the reviewer_ids of this OrganizationJobTemplateLocalesCreateParameters.  # noqa: E501

        Array of reviewer ids to be assigned to the job template locale  # noqa: E501

        :return: The reviewer_ids of this OrganizationJobTemplateLocalesCreateParameters.  # noqa: E501
        :rtype: list[str]
        """
        return self._reviewer_ids

    @reviewer_ids.setter
    def reviewer_ids(self, reviewer_ids):
        """Sets the reviewer_ids of this OrganizationJobTemplateLocalesCreateParameters.

        Array of reviewer ids to be assigned to the job template locale  # noqa: E501

        :param reviewer_ids: The reviewer_ids of this OrganizationJobTemplateLocalesCreateParameters.  # noqa: E501
        :type: list[str]
        """

        self._reviewer_ids = reviewer_ids

    @property
    def translator_team_ids(self):
        """Gets the translator_team_ids of this OrganizationJobTemplateLocalesCreateParameters.  # noqa: E501

        Array of team ids to be assigned to the job locale as translators  # noqa: E501

        :return: The translator_team_ids of this OrganizationJobTemplateLocalesCreateParameters.  # noqa: E501
        :rtype: list[str]
        """
        return self._translator_team_ids

    @translator_team_ids.setter
    def translator_team_ids(self, translator_team_ids):
        """Sets the translator_team_ids of this OrganizationJobTemplateLocalesCreateParameters.

        Array of team ids to be assigned to the job locale as translators  # noqa: E501

        :param translator_team_ids: The translator_team_ids of this OrganizationJobTemplateLocalesCreateParameters.  # noqa: E501
        :type: list[str]
        """

        self._translator_team_ids = translator_team_ids

    @property
    def reviewer_team_ids(self):
        """Gets the reviewer_team_ids of this OrganizationJobTemplateLocalesCreateParameters.  # noqa: E501

        Array of team ids to be assigned to the job locale as reviewers  # noqa: E501

        :return: The reviewer_team_ids of this OrganizationJobTemplateLocalesCreateParameters.  # noqa: E501
        :rtype: list[str]
        """
        return self._reviewer_team_ids

    @reviewer_team_ids.setter
    def reviewer_team_ids(self, reviewer_team_ids):
        """Sets the reviewer_team_ids of this OrganizationJobTemplateLocalesCreateParameters.

        Array of team ids to be assigned to the job locale as reviewers  # noqa: E501

        :param reviewer_team_ids: The reviewer_team_ids of this OrganizationJobTemplateLocalesCreateParameters.  # noqa: E501
        :type: list[str]
        """

        self._reviewer_team_ids = reviewer_team_ids

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
        if not isinstance(other, OrganizationJobTemplateLocalesCreateParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrganizationJobTemplateLocalesCreateParameters):
            return True

        return self.to_dict() != other.to_dict()

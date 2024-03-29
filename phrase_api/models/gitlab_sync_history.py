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


class GitlabSyncHistory(object):
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
        'status': 'str',
        'action': 'str',
        'errors': 'List[GitlabSyncHistoryErrorsInner]',
        'var_date': 'datetime',
        'details': 'object'
    }

    attribute_map = {
        'status': 'status',
        'action': 'action',
        'errors': 'errors',
        'var_date': 'date',
        'details': 'details'
    }

    def __init__(self, status=None, action=None, errors=None, var_date=None, details=None, local_vars_configuration=None):  # noqa: E501
        """GitlabSyncHistory - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._status = None
        self._action = None
        self._errors = None
        self._var_date = None
        self._details = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if action is not None:
            self.action = action
        if errors is not None:
            self.errors = errors
        if var_date is not None:
            self.var_date = var_date
        if details is not None:
            self.details = details

    @property
    def status(self):
        """Gets the status of this GitlabSyncHistory.  # noqa: E501


        :return: The status of this GitlabSyncHistory.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GitlabSyncHistory.


        :param status: The status of this GitlabSyncHistory.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def action(self):
        """Gets the action of this GitlabSyncHistory.  # noqa: E501


        :return: The action of this GitlabSyncHistory.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this GitlabSyncHistory.


        :param action: The action of this GitlabSyncHistory.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def errors(self):
        """Gets the errors of this GitlabSyncHistory.  # noqa: E501


        :return: The errors of this GitlabSyncHistory.  # noqa: E501
        :rtype: List[GitlabSyncHistoryErrorsInner]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this GitlabSyncHistory.


        :param errors: The errors of this GitlabSyncHistory.  # noqa: E501
        :type: List[GitlabSyncHistoryErrorsInner]
        """

        self._errors = errors

    @property
    def var_date(self):
        """Gets the var_date of this GitlabSyncHistory.  # noqa: E501


        :return: The var_date of this GitlabSyncHistory.  # noqa: E501
        :rtype: datetime
        """
        return self._var_date

    @var_date.setter
    def var_date(self, var_date):
        """Sets the var_date of this GitlabSyncHistory.


        :param var_date: The var_date of this GitlabSyncHistory.  # noqa: E501
        :type: datetime
        """

        self._var_date = var_date

    @property
    def details(self):
        """Gets the details of this GitlabSyncHistory.  # noqa: E501


        :return: The details of this GitlabSyncHistory.  # noqa: E501
        :rtype: object
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this GitlabSyncHistory.


        :param details: The details of this GitlabSyncHistory.  # noqa: E501
        :type: object
        """

        self._details = details

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
        if not isinstance(other, GitlabSyncHistory):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GitlabSyncHistory):
            return True

        return self.to_dict() != other.to_dict()

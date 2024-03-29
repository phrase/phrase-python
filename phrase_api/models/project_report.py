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


class ProjectReport(object):
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
        'locales_count': 'int',
        'keys_count': 'int',
        'translations_count': 'int',
        'untranslated_keys_count': 'int',
        'unverified_translations_count': 'int',
        'reviewed_translations_count': 'int',
        'managed_words_count': 'int',
        'project': 'ProjectShort'
    }

    attribute_map = {
        'locales_count': 'locales_count',
        'keys_count': 'keys_count',
        'translations_count': 'translations_count',
        'untranslated_keys_count': 'untranslated_keys_count',
        'unverified_translations_count': 'unverified_translations_count',
        'reviewed_translations_count': 'reviewed_translations_count',
        'managed_words_count': 'managed_words_count',
        'project': 'project'
    }

    def __init__(self, locales_count=None, keys_count=None, translations_count=None, untranslated_keys_count=None, unverified_translations_count=None, reviewed_translations_count=None, managed_words_count=None, project=None, local_vars_configuration=None):  # noqa: E501
        """ProjectReport - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._locales_count = None
        self._keys_count = None
        self._translations_count = None
        self._untranslated_keys_count = None
        self._unverified_translations_count = None
        self._reviewed_translations_count = None
        self._managed_words_count = None
        self._project = None
        self.discriminator = None

        if locales_count is not None:
            self.locales_count = locales_count
        if keys_count is not None:
            self.keys_count = keys_count
        if translations_count is not None:
            self.translations_count = translations_count
        if untranslated_keys_count is not None:
            self.untranslated_keys_count = untranslated_keys_count
        if unverified_translations_count is not None:
            self.unverified_translations_count = unverified_translations_count
        if reviewed_translations_count is not None:
            self.reviewed_translations_count = reviewed_translations_count
        if managed_words_count is not None:
            self.managed_words_count = managed_words_count
        if project is not None:
            self.project = project

    @property
    def locales_count(self):
        """Gets the locales_count of this ProjectReport.  # noqa: E501


        :return: The locales_count of this ProjectReport.  # noqa: E501
        :rtype: int
        """
        return self._locales_count

    @locales_count.setter
    def locales_count(self, locales_count):
        """Sets the locales_count of this ProjectReport.


        :param locales_count: The locales_count of this ProjectReport.  # noqa: E501
        :type: int
        """

        self._locales_count = locales_count

    @property
    def keys_count(self):
        """Gets the keys_count of this ProjectReport.  # noqa: E501


        :return: The keys_count of this ProjectReport.  # noqa: E501
        :rtype: int
        """
        return self._keys_count

    @keys_count.setter
    def keys_count(self, keys_count):
        """Sets the keys_count of this ProjectReport.


        :param keys_count: The keys_count of this ProjectReport.  # noqa: E501
        :type: int
        """

        self._keys_count = keys_count

    @property
    def translations_count(self):
        """Gets the translations_count of this ProjectReport.  # noqa: E501


        :return: The translations_count of this ProjectReport.  # noqa: E501
        :rtype: int
        """
        return self._translations_count

    @translations_count.setter
    def translations_count(self, translations_count):
        """Sets the translations_count of this ProjectReport.


        :param translations_count: The translations_count of this ProjectReport.  # noqa: E501
        :type: int
        """

        self._translations_count = translations_count

    @property
    def untranslated_keys_count(self):
        """Gets the untranslated_keys_count of this ProjectReport.  # noqa: E501


        :return: The untranslated_keys_count of this ProjectReport.  # noqa: E501
        :rtype: int
        """
        return self._untranslated_keys_count

    @untranslated_keys_count.setter
    def untranslated_keys_count(self, untranslated_keys_count):
        """Sets the untranslated_keys_count of this ProjectReport.


        :param untranslated_keys_count: The untranslated_keys_count of this ProjectReport.  # noqa: E501
        :type: int
        """

        self._untranslated_keys_count = untranslated_keys_count

    @property
    def unverified_translations_count(self):
        """Gets the unverified_translations_count of this ProjectReport.  # noqa: E501


        :return: The unverified_translations_count of this ProjectReport.  # noqa: E501
        :rtype: int
        """
        return self._unverified_translations_count

    @unverified_translations_count.setter
    def unverified_translations_count(self, unverified_translations_count):
        """Sets the unverified_translations_count of this ProjectReport.


        :param unverified_translations_count: The unverified_translations_count of this ProjectReport.  # noqa: E501
        :type: int
        """

        self._unverified_translations_count = unverified_translations_count

    @property
    def reviewed_translations_count(self):
        """Gets the reviewed_translations_count of this ProjectReport.  # noqa: E501


        :return: The reviewed_translations_count of this ProjectReport.  # noqa: E501
        :rtype: int
        """
        return self._reviewed_translations_count

    @reviewed_translations_count.setter
    def reviewed_translations_count(self, reviewed_translations_count):
        """Sets the reviewed_translations_count of this ProjectReport.


        :param reviewed_translations_count: The reviewed_translations_count of this ProjectReport.  # noqa: E501
        :type: int
        """

        self._reviewed_translations_count = reviewed_translations_count

    @property
    def managed_words_count(self):
        """Gets the managed_words_count of this ProjectReport.  # noqa: E501


        :return: The managed_words_count of this ProjectReport.  # noqa: E501
        :rtype: int
        """
        return self._managed_words_count

    @managed_words_count.setter
    def managed_words_count(self, managed_words_count):
        """Sets the managed_words_count of this ProjectReport.


        :param managed_words_count: The managed_words_count of this ProjectReport.  # noqa: E501
        :type: int
        """

        self._managed_words_count = managed_words_count

    @property
    def project(self):
        """Gets the project of this ProjectReport.  # noqa: E501


        :return: The project of this ProjectReport.  # noqa: E501
        :rtype: ProjectShort
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this ProjectReport.


        :param project: The project of this ProjectReport.  # noqa: E501
        :type: ProjectShort
        """

        self._project = project

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
        if not isinstance(other, ProjectReport):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectReport):
            return True

        return self.to_dict() != other.to_dict()

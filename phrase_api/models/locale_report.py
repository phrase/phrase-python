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


class LocaleReport(object):
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
        'keys_count': 'int',
        'translated_translations_percentage': 'float',
        'unverified_translations_percentage': 'float',
        'reviewed_translations_percentage': 'float',
        'untranslated_keys_percentage': 'float',
        'completed_translations_count': 'int',
        'untranslated_keys_count': 'int',
        'unverified_translations_count': 'int',
        'reviewed_translations_count': 'int',
        'source_word_count': 'int',
        'word_count': 'int',
        'word_count_unverified': 'int',
        'word_count_missing': 'int',
        'locale': 'LocalePreview'
    }

    attribute_map = {
        'keys_count': 'keys_count',
        'translated_translations_percentage': 'translated_translations_percentage',
        'unverified_translations_percentage': 'unverified_translations_percentage',
        'reviewed_translations_percentage': 'reviewed_translations_percentage',
        'untranslated_keys_percentage': 'untranslated_keys_percentage',
        'completed_translations_count': 'completed_translations_count',
        'untranslated_keys_count': 'untranslated_keys_count',
        'unverified_translations_count': 'unverified_translations_count',
        'reviewed_translations_count': 'reviewed_translations_count',
        'source_word_count': 'source_word_count',
        'word_count': 'word_count',
        'word_count_unverified': 'word_count_unverified',
        'word_count_missing': 'word_count_missing',
        'locale': 'locale'
    }

    def __init__(self, keys_count=None, translated_translations_percentage=None, unverified_translations_percentage=None, reviewed_translations_percentage=None, untranslated_keys_percentage=None, completed_translations_count=None, untranslated_keys_count=None, unverified_translations_count=None, reviewed_translations_count=None, source_word_count=None, word_count=None, word_count_unverified=None, word_count_missing=None, locale=None, local_vars_configuration=None):  # noqa: E501
        """LocaleReport - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._keys_count = None
        self._translated_translations_percentage = None
        self._unverified_translations_percentage = None
        self._reviewed_translations_percentage = None
        self._untranslated_keys_percentage = None
        self._completed_translations_count = None
        self._untranslated_keys_count = None
        self._unverified_translations_count = None
        self._reviewed_translations_count = None
        self._source_word_count = None
        self._word_count = None
        self._word_count_unverified = None
        self._word_count_missing = None
        self._locale = None
        self.discriminator = None

        if keys_count is not None:
            self.keys_count = keys_count
        if translated_translations_percentage is not None:
            self.translated_translations_percentage = translated_translations_percentage
        if unverified_translations_percentage is not None:
            self.unverified_translations_percentage = unverified_translations_percentage
        if reviewed_translations_percentage is not None:
            self.reviewed_translations_percentage = reviewed_translations_percentage
        if untranslated_keys_percentage is not None:
            self.untranslated_keys_percentage = untranslated_keys_percentage
        if completed_translations_count is not None:
            self.completed_translations_count = completed_translations_count
        if untranslated_keys_count is not None:
            self.untranslated_keys_count = untranslated_keys_count
        if unverified_translations_count is not None:
            self.unverified_translations_count = unverified_translations_count
        if reviewed_translations_count is not None:
            self.reviewed_translations_count = reviewed_translations_count
        if source_word_count is not None:
            self.source_word_count = source_word_count
        if word_count is not None:
            self.word_count = word_count
        if word_count_unverified is not None:
            self.word_count_unverified = word_count_unverified
        if word_count_missing is not None:
            self.word_count_missing = word_count_missing
        if locale is not None:
            self.locale = locale

    @property
    def keys_count(self):
        """Gets the keys_count of this LocaleReport.  # noqa: E501


        :return: The keys_count of this LocaleReport.  # noqa: E501
        :rtype: int
        """
        return self._keys_count

    @keys_count.setter
    def keys_count(self, keys_count):
        """Sets the keys_count of this LocaleReport.


        :param keys_count: The keys_count of this LocaleReport.  # noqa: E501
        :type: int
        """

        self._keys_count = keys_count

    @property
    def translated_translations_percentage(self):
        """Gets the translated_translations_percentage of this LocaleReport.  # noqa: E501


        :return: The translated_translations_percentage of this LocaleReport.  # noqa: E501
        :rtype: float
        """
        return self._translated_translations_percentage

    @translated_translations_percentage.setter
    def translated_translations_percentage(self, translated_translations_percentage):
        """Sets the translated_translations_percentage of this LocaleReport.


        :param translated_translations_percentage: The translated_translations_percentage of this LocaleReport.  # noqa: E501
        :type: float
        """

        self._translated_translations_percentage = translated_translations_percentage

    @property
    def unverified_translations_percentage(self):
        """Gets the unverified_translations_percentage of this LocaleReport.  # noqa: E501


        :return: The unverified_translations_percentage of this LocaleReport.  # noqa: E501
        :rtype: float
        """
        return self._unverified_translations_percentage

    @unverified_translations_percentage.setter
    def unverified_translations_percentage(self, unverified_translations_percentage):
        """Sets the unverified_translations_percentage of this LocaleReport.


        :param unverified_translations_percentage: The unverified_translations_percentage of this LocaleReport.  # noqa: E501
        :type: float
        """

        self._unverified_translations_percentage = unverified_translations_percentage

    @property
    def reviewed_translations_percentage(self):
        """Gets the reviewed_translations_percentage of this LocaleReport.  # noqa: E501


        :return: The reviewed_translations_percentage of this LocaleReport.  # noqa: E501
        :rtype: float
        """
        return self._reviewed_translations_percentage

    @reviewed_translations_percentage.setter
    def reviewed_translations_percentage(self, reviewed_translations_percentage):
        """Sets the reviewed_translations_percentage of this LocaleReport.


        :param reviewed_translations_percentage: The reviewed_translations_percentage of this LocaleReport.  # noqa: E501
        :type: float
        """

        self._reviewed_translations_percentage = reviewed_translations_percentage

    @property
    def untranslated_keys_percentage(self):
        """Gets the untranslated_keys_percentage of this LocaleReport.  # noqa: E501


        :return: The untranslated_keys_percentage of this LocaleReport.  # noqa: E501
        :rtype: float
        """
        return self._untranslated_keys_percentage

    @untranslated_keys_percentage.setter
    def untranslated_keys_percentage(self, untranslated_keys_percentage):
        """Sets the untranslated_keys_percentage of this LocaleReport.


        :param untranslated_keys_percentage: The untranslated_keys_percentage of this LocaleReport.  # noqa: E501
        :type: float
        """

        self._untranslated_keys_percentage = untranslated_keys_percentage

    @property
    def completed_translations_count(self):
        """Gets the completed_translations_count of this LocaleReport.  # noqa: E501


        :return: The completed_translations_count of this LocaleReport.  # noqa: E501
        :rtype: int
        """
        return self._completed_translations_count

    @completed_translations_count.setter
    def completed_translations_count(self, completed_translations_count):
        """Sets the completed_translations_count of this LocaleReport.


        :param completed_translations_count: The completed_translations_count of this LocaleReport.  # noqa: E501
        :type: int
        """

        self._completed_translations_count = completed_translations_count

    @property
    def untranslated_keys_count(self):
        """Gets the untranslated_keys_count of this LocaleReport.  # noqa: E501


        :return: The untranslated_keys_count of this LocaleReport.  # noqa: E501
        :rtype: int
        """
        return self._untranslated_keys_count

    @untranslated_keys_count.setter
    def untranslated_keys_count(self, untranslated_keys_count):
        """Sets the untranslated_keys_count of this LocaleReport.


        :param untranslated_keys_count: The untranslated_keys_count of this LocaleReport.  # noqa: E501
        :type: int
        """

        self._untranslated_keys_count = untranslated_keys_count

    @property
    def unverified_translations_count(self):
        """Gets the unverified_translations_count of this LocaleReport.  # noqa: E501


        :return: The unverified_translations_count of this LocaleReport.  # noqa: E501
        :rtype: int
        """
        return self._unverified_translations_count

    @unverified_translations_count.setter
    def unverified_translations_count(self, unverified_translations_count):
        """Sets the unverified_translations_count of this LocaleReport.


        :param unverified_translations_count: The unverified_translations_count of this LocaleReport.  # noqa: E501
        :type: int
        """

        self._unverified_translations_count = unverified_translations_count

    @property
    def reviewed_translations_count(self):
        """Gets the reviewed_translations_count of this LocaleReport.  # noqa: E501


        :return: The reviewed_translations_count of this LocaleReport.  # noqa: E501
        :rtype: int
        """
        return self._reviewed_translations_count

    @reviewed_translations_count.setter
    def reviewed_translations_count(self, reviewed_translations_count):
        """Sets the reviewed_translations_count of this LocaleReport.


        :param reviewed_translations_count: The reviewed_translations_count of this LocaleReport.  # noqa: E501
        :type: int
        """

        self._reviewed_translations_count = reviewed_translations_count

    @property
    def source_word_count(self):
        """Gets the source_word_count of this LocaleReport.  # noqa: E501


        :return: The source_word_count of this LocaleReport.  # noqa: E501
        :rtype: int
        """
        return self._source_word_count

    @source_word_count.setter
    def source_word_count(self, source_word_count):
        """Sets the source_word_count of this LocaleReport.


        :param source_word_count: The source_word_count of this LocaleReport.  # noqa: E501
        :type: int
        """

        self._source_word_count = source_word_count

    @property
    def word_count(self):
        """Gets the word_count of this LocaleReport.  # noqa: E501


        :return: The word_count of this LocaleReport.  # noqa: E501
        :rtype: int
        """
        return self._word_count

    @word_count.setter
    def word_count(self, word_count):
        """Sets the word_count of this LocaleReport.


        :param word_count: The word_count of this LocaleReport.  # noqa: E501
        :type: int
        """

        self._word_count = word_count

    @property
    def word_count_unverified(self):
        """Gets the word_count_unverified of this LocaleReport.  # noqa: E501


        :return: The word_count_unverified of this LocaleReport.  # noqa: E501
        :rtype: int
        """
        return self._word_count_unverified

    @word_count_unverified.setter
    def word_count_unverified(self, word_count_unverified):
        """Sets the word_count_unverified of this LocaleReport.


        :param word_count_unverified: The word_count_unverified of this LocaleReport.  # noqa: E501
        :type: int
        """

        self._word_count_unverified = word_count_unverified

    @property
    def word_count_missing(self):
        """Gets the word_count_missing of this LocaleReport.  # noqa: E501


        :return: The word_count_missing of this LocaleReport.  # noqa: E501
        :rtype: int
        """
        return self._word_count_missing

    @word_count_missing.setter
    def word_count_missing(self, word_count_missing):
        """Sets the word_count_missing of this LocaleReport.


        :param word_count_missing: The word_count_missing of this LocaleReport.  # noqa: E501
        :type: int
        """

        self._word_count_missing = word_count_missing

    @property
    def locale(self):
        """Gets the locale of this LocaleReport.  # noqa: E501


        :return: The locale of this LocaleReport.  # noqa: E501
        :rtype: LocalePreview
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this LocaleReport.


        :param locale: The locale of this LocaleReport.  # noqa: E501
        :type: LocalePreview
        """

        self._locale = locale

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
        if not isinstance(other, LocaleReport):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LocaleReport):
            return True

        return self.to_dict() != other.to_dict()

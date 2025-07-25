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


class TranslationCreateParameters(object):
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
        'locale_id': 'str',
        'key_id': 'str',
        'content': 'str',
        'plural_suffix': 'str',
        'unverified': 'bool',
        'excluded': 'bool',
        'autotranslate': 'bool'
    }

    attribute_map = {
        'branch': 'branch',
        'locale_id': 'locale_id',
        'key_id': 'key_id',
        'content': 'content',
        'plural_suffix': 'plural_suffix',
        'unverified': 'unverified',
        'excluded': 'excluded',
        'autotranslate': 'autotranslate'
    }

    def __init__(self, branch=None, locale_id=None, key_id=None, content=None, plural_suffix=None, unverified=None, excluded=None, autotranslate=None, local_vars_configuration=None):  # noqa: E501
        """TranslationCreateParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._branch = None
        self._locale_id = None
        self._key_id = None
        self._content = None
        self._plural_suffix = None
        self._unverified = None
        self._excluded = None
        self._autotranslate = None
        self.discriminator = None

        if branch is not None:
            self.branch = branch
        if locale_id is not None:
            self.locale_id = locale_id
        if key_id is not None:
            self.key_id = key_id
        if content is not None:
            self.content = content
        if plural_suffix is not None:
            self.plural_suffix = plural_suffix
        if unverified is not None:
            self.unverified = unverified
        if excluded is not None:
            self.excluded = excluded
        if autotranslate is not None:
            self.autotranslate = autotranslate

    @property
    def branch(self):
        """Gets the branch of this TranslationCreateParameters.  # noqa: E501

        specify the branch to use  # noqa: E501

        :return: The branch of this TranslationCreateParameters.  # noqa: E501
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this TranslationCreateParameters.

        specify the branch to use  # noqa: E501

        :param branch: The branch of this TranslationCreateParameters.  # noqa: E501
        :type: str
        """

        self._branch = branch

    @property
    def locale_id(self):
        """Gets the locale_id of this TranslationCreateParameters.  # noqa: E501

        Locale. Can be the name or id of the locale. Preferred is id  # noqa: E501

        :return: The locale_id of this TranslationCreateParameters.  # noqa: E501
        :rtype: str
        """
        return self._locale_id

    @locale_id.setter
    def locale_id(self, locale_id):
        """Sets the locale_id of this TranslationCreateParameters.

        Locale. Can be the name or id of the locale. Preferred is id  # noqa: E501

        :param locale_id: The locale_id of this TranslationCreateParameters.  # noqa: E501
        :type: str
        """

        self._locale_id = locale_id

    @property
    def key_id(self):
        """Gets the key_id of this TranslationCreateParameters.  # noqa: E501

        Key  # noqa: E501

        :return: The key_id of this TranslationCreateParameters.  # noqa: E501
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """Sets the key_id of this TranslationCreateParameters.

        Key  # noqa: E501

        :param key_id: The key_id of this TranslationCreateParameters.  # noqa: E501
        :type: str
        """

        self._key_id = key_id

    @property
    def content(self):
        """Gets the content of this TranslationCreateParameters.  # noqa: E501

        Translation content  # noqa: E501

        :return: The content of this TranslationCreateParameters.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this TranslationCreateParameters.

        Translation content  # noqa: E501

        :param content: The content of this TranslationCreateParameters.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def plural_suffix(self):
        """Gets the plural_suffix of this TranslationCreateParameters.  # noqa: E501

        Plural suffix. Can be one of: zero, one, two, few, many, other. Must be specified if the key associated to the translation is pluralized.  # noqa: E501

        :return: The plural_suffix of this TranslationCreateParameters.  # noqa: E501
        :rtype: str
        """
        return self._plural_suffix

    @plural_suffix.setter
    def plural_suffix(self, plural_suffix):
        """Sets the plural_suffix of this TranslationCreateParameters.

        Plural suffix. Can be one of: zero, one, two, few, many, other. Must be specified if the key associated to the translation is pluralized.  # noqa: E501

        :param plural_suffix: The plural_suffix of this TranslationCreateParameters.  # noqa: E501
        :type: str
        """

        self._plural_suffix = plural_suffix

    @property
    def unverified(self):
        """Gets the unverified of this TranslationCreateParameters.  # noqa: E501

        Indicates whether translation is unverified. Part of the [Advanced Workflows](https://support.phrase.com/hc/en-us/articles/5784094755484) feature.  # noqa: E501

        :return: The unverified of this TranslationCreateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._unverified

    @unverified.setter
    def unverified(self, unverified):
        """Sets the unverified of this TranslationCreateParameters.

        Indicates whether translation is unverified. Part of the [Advanced Workflows](https://support.phrase.com/hc/en-us/articles/5784094755484) feature.  # noqa: E501

        :param unverified: The unverified of this TranslationCreateParameters.  # noqa: E501
        :type: bool
        """

        self._unverified = unverified

    @property
    def excluded(self):
        """Gets the excluded of this TranslationCreateParameters.  # noqa: E501

        Indicates whether translation is excluded.  # noqa: E501

        :return: The excluded of this TranslationCreateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._excluded

    @excluded.setter
    def excluded(self, excluded):
        """Sets the excluded of this TranslationCreateParameters.

        Indicates whether translation is excluded.  # noqa: E501

        :param excluded: The excluded of this TranslationCreateParameters.  # noqa: E501
        :type: bool
        """

        self._excluded = excluded

    @property
    def autotranslate(self):
        """Gets the autotranslate of this TranslationCreateParameters.  # noqa: E501

        Indicates whether the translation should be auto-translated. Responses with status 422 if provided for translation within a non-default locale or the project does not have the Autopilot feature enabled.  # noqa: E501

        :return: The autotranslate of this TranslationCreateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._autotranslate

    @autotranslate.setter
    def autotranslate(self, autotranslate):
        """Sets the autotranslate of this TranslationCreateParameters.

        Indicates whether the translation should be auto-translated. Responses with status 422 if provided for translation within a non-default locale or the project does not have the Autopilot feature enabled.  # noqa: E501

        :param autotranslate: The autotranslate of this TranslationCreateParameters.  # noqa: E501
        :type: bool
        """

        self._autotranslate = autotranslate

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
        if not isinstance(other, TranslationCreateParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TranslationCreateParameters):
            return True

        return self.to_dict() != other.to_dict()

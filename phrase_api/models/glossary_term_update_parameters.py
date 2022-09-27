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


class GlossaryTermUpdateParameters(object):
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
        'term': 'str',
        'description': 'str',
        'translatable': 'bool',
        'case_sensitive': 'bool'
    }

    attribute_map = {
        'term': 'term',
        'description': 'description',
        'translatable': 'translatable',
        'case_sensitive': 'case_sensitive'
    }

    def __init__(self, term=None, description=None, translatable=None, case_sensitive=None, local_vars_configuration=None):  # noqa: E501
        """GlossaryTermUpdateParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._term = None
        self._description = None
        self._translatable = None
        self._case_sensitive = None
        self.discriminator = None

        if term is not None:
            self.term = term
        if description is not None:
            self.description = description
        if translatable is not None:
            self.translatable = translatable
        if case_sensitive is not None:
            self.case_sensitive = case_sensitive

    @property
    def term(self):
        """Gets the term of this GlossaryTermUpdateParameters.  # noqa: E501

        Glossary term  # noqa: E501

        :return: The term of this GlossaryTermUpdateParameters.  # noqa: E501
        :rtype: str
        """
        return self._term

    @term.setter
    def term(self, term):
        """Sets the term of this GlossaryTermUpdateParameters.

        Glossary term  # noqa: E501

        :param term: The term of this GlossaryTermUpdateParameters.  # noqa: E501
        :type: str
        """

        self._term = term

    @property
    def description(self):
        """Gets the description of this GlossaryTermUpdateParameters.  # noqa: E501

        Description of term  # noqa: E501

        :return: The description of this GlossaryTermUpdateParameters.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GlossaryTermUpdateParameters.

        Description of term  # noqa: E501

        :param description: The description of this GlossaryTermUpdateParameters.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def translatable(self):
        """Gets the translatable of this GlossaryTermUpdateParameters.  # noqa: E501

        Indicates whether the term should be used for all languages or can be translated  # noqa: E501

        :return: The translatable of this GlossaryTermUpdateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._translatable

    @translatable.setter
    def translatable(self, translatable):
        """Sets the translatable of this GlossaryTermUpdateParameters.

        Indicates whether the term should be used for all languages or can be translated  # noqa: E501

        :param translatable: The translatable of this GlossaryTermUpdateParameters.  # noqa: E501
        :type: bool
        """

        self._translatable = translatable

    @property
    def case_sensitive(self):
        """Gets the case_sensitive of this GlossaryTermUpdateParameters.  # noqa: E501

        Indicates whether the term is case sensitive  # noqa: E501

        :return: The case_sensitive of this GlossaryTermUpdateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._case_sensitive

    @case_sensitive.setter
    def case_sensitive(self, case_sensitive):
        """Sets the case_sensitive of this GlossaryTermUpdateParameters.

        Indicates whether the term is case sensitive  # noqa: E501

        :param case_sensitive: The case_sensitive of this GlossaryTermUpdateParameters.  # noqa: E501
        :type: bool
        """

        self._case_sensitive = case_sensitive

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
        if not isinstance(other, GlossaryTermUpdateParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GlossaryTermUpdateParameters):
            return True

        return self.to_dict() != other.to_dict()

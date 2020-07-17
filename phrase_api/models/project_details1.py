# coding: utf-8

"""
    Phrase API Reference

    The version of the OpenAPI document: 2.0.0
    Contact: support@phrase.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from phrase_api.configuration import Configuration


class ProjectDetails1(object):
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
        'slug': 'str',
        'shares_translation_memory': 'bool'
    }

    attribute_map = {
        'slug': 'slug',
        'shares_translation_memory': 'shares_translation_memory'
    }

    def __init__(self, slug=None, shares_translation_memory=None, local_vars_configuration=None):  # noqa: E501
        """ProjectDetails1 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._slug = None
        self._shares_translation_memory = None
        self.discriminator = None

        if slug is not None:
            self.slug = slug
        if shares_translation_memory is not None:
            self.shares_translation_memory = shares_translation_memory

    @property
    def slug(self):
        """Gets the slug of this ProjectDetails1.  # noqa: E501


        :return: The slug of this ProjectDetails1.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this ProjectDetails1.


        :param slug: The slug of this ProjectDetails1.  # noqa: E501
        :type: str
        """

        self._slug = slug

    @property
    def shares_translation_memory(self):
        """Gets the shares_translation_memory of this ProjectDetails1.  # noqa: E501


        :return: The shares_translation_memory of this ProjectDetails1.  # noqa: E501
        :rtype: bool
        """
        return self._shares_translation_memory

    @shares_translation_memory.setter
    def shares_translation_memory(self, shares_translation_memory):
        """Sets the shares_translation_memory of this ProjectDetails1.


        :param shares_translation_memory: The shares_translation_memory of this ProjectDetails1.  # noqa: E501
        :type: bool
        """

        self._shares_translation_memory = shares_translation_memory

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
        if not isinstance(other, ProjectDetails1):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectDetails1):
            return True

        return self.to_dict() != other.to_dict()
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


class Format(object):
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
        'name': 'str',
        'api_name': 'str',
        'description': 'str',
        'extension': 'str',
        'default_encoding': 'str',
        'importable': 'bool',
        'exportable': 'bool',
        'default_file': 'str',
        'renders_default_locale': 'bool',
        'includes_locale_information': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'api_name': 'api_name',
        'description': 'description',
        'extension': 'extension',
        'default_encoding': 'default_encoding',
        'importable': 'importable',
        'exportable': 'exportable',
        'default_file': 'default_file',
        'renders_default_locale': 'renders_default_locale',
        'includes_locale_information': 'includes_locale_information'
    }

    def __init__(self, name=None, api_name=None, description=None, extension=None, default_encoding=None, importable=None, exportable=None, default_file=None, renders_default_locale=None, includes_locale_information=None, local_vars_configuration=None):  # noqa: E501
        """Format - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._api_name = None
        self._description = None
        self._extension = None
        self._default_encoding = None
        self._importable = None
        self._exportable = None
        self._default_file = None
        self._renders_default_locale = None
        self._includes_locale_information = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if api_name is not None:
            self.api_name = api_name
        if description is not None:
            self.description = description
        if extension is not None:
            self.extension = extension
        if default_encoding is not None:
            self.default_encoding = default_encoding
        if importable is not None:
            self.importable = importable
        if exportable is not None:
            self.exportable = exportable
        if default_file is not None:
            self.default_file = default_file
        if renders_default_locale is not None:
            self.renders_default_locale = renders_default_locale
        if includes_locale_information is not None:
            self.includes_locale_information = includes_locale_information

    @property
    def name(self):
        """Gets the name of this Format.  # noqa: E501


        :return: The name of this Format.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Format.


        :param name: The name of this Format.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def api_name(self):
        """Gets the api_name of this Format.  # noqa: E501


        :return: The api_name of this Format.  # noqa: E501
        :rtype: str
        """
        return self._api_name

    @api_name.setter
    def api_name(self, api_name):
        """Sets the api_name of this Format.


        :param api_name: The api_name of this Format.  # noqa: E501
        :type: str
        """

        self._api_name = api_name

    @property
    def description(self):
        """Gets the description of this Format.  # noqa: E501


        :return: The description of this Format.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Format.


        :param description: The description of this Format.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def extension(self):
        """Gets the extension of this Format.  # noqa: E501


        :return: The extension of this Format.  # noqa: E501
        :rtype: str
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """Sets the extension of this Format.


        :param extension: The extension of this Format.  # noqa: E501
        :type: str
        """

        self._extension = extension

    @property
    def default_encoding(self):
        """Gets the default_encoding of this Format.  # noqa: E501


        :return: The default_encoding of this Format.  # noqa: E501
        :rtype: str
        """
        return self._default_encoding

    @default_encoding.setter
    def default_encoding(self, default_encoding):
        """Sets the default_encoding of this Format.


        :param default_encoding: The default_encoding of this Format.  # noqa: E501
        :type: str
        """

        self._default_encoding = default_encoding

    @property
    def importable(self):
        """Gets the importable of this Format.  # noqa: E501


        :return: The importable of this Format.  # noqa: E501
        :rtype: bool
        """
        return self._importable

    @importable.setter
    def importable(self, importable):
        """Sets the importable of this Format.


        :param importable: The importable of this Format.  # noqa: E501
        :type: bool
        """

        self._importable = importable

    @property
    def exportable(self):
        """Gets the exportable of this Format.  # noqa: E501


        :return: The exportable of this Format.  # noqa: E501
        :rtype: bool
        """
        return self._exportable

    @exportable.setter
    def exportable(self, exportable):
        """Sets the exportable of this Format.


        :param exportable: The exportable of this Format.  # noqa: E501
        :type: bool
        """

        self._exportable = exportable

    @property
    def default_file(self):
        """Gets the default_file of this Format.  # noqa: E501


        :return: The default_file of this Format.  # noqa: E501
        :rtype: str
        """
        return self._default_file

    @default_file.setter
    def default_file(self, default_file):
        """Sets the default_file of this Format.


        :param default_file: The default_file of this Format.  # noqa: E501
        :type: str
        """

        self._default_file = default_file

    @property
    def renders_default_locale(self):
        """Gets the renders_default_locale of this Format.  # noqa: E501


        :return: The renders_default_locale of this Format.  # noqa: E501
        :rtype: bool
        """
        return self._renders_default_locale

    @renders_default_locale.setter
    def renders_default_locale(self, renders_default_locale):
        """Sets the renders_default_locale of this Format.


        :param renders_default_locale: The renders_default_locale of this Format.  # noqa: E501
        :type: bool
        """

        self._renders_default_locale = renders_default_locale

    @property
    def includes_locale_information(self):
        """Gets the includes_locale_information of this Format.  # noqa: E501


        :return: The includes_locale_information of this Format.  # noqa: E501
        :rtype: bool
        """
        return self._includes_locale_information

    @includes_locale_information.setter
    def includes_locale_information(self, includes_locale_information):
        """Sets the includes_locale_information of this Format.


        :param includes_locale_information: The includes_locale_information of this Format.  # noqa: E501
        :type: bool
        """

        self._includes_locale_information = includes_locale_information

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
        if not isinstance(other, Format):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Format):
            return True

        return self.to_dict() != other.to_dict()

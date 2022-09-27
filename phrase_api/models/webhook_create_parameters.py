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


class WebhookCreateParameters(object):
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
        'callback_url': 'str',
        'secret': 'str',
        'description': 'str',
        'events': 'str',
        'active': 'bool',
        'include_branches': 'bool'
    }

    attribute_map = {
        'callback_url': 'callback_url',
        'secret': 'secret',
        'description': 'description',
        'events': 'events',
        'active': 'active',
        'include_branches': 'include_branches'
    }

    def __init__(self, callback_url=None, secret=None, description=None, events=None, active=None, include_branches=None, local_vars_configuration=None):  # noqa: E501
        """WebhookCreateParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._callback_url = None
        self._secret = None
        self._description = None
        self._events = None
        self._active = None
        self._include_branches = None
        self.discriminator = None

        if callback_url is not None:
            self.callback_url = callback_url
        if secret is not None:
            self.secret = secret
        if description is not None:
            self.description = description
        if events is not None:
            self.events = events
        if active is not None:
            self.active = active
        if include_branches is not None:
            self.include_branches = include_branches

    @property
    def callback_url(self):
        """Gets the callback_url of this WebhookCreateParameters.  # noqa: E501

        Callback URL to send requests to  # noqa: E501

        :return: The callback_url of this WebhookCreateParameters.  # noqa: E501
        :rtype: str
        """
        return self._callback_url

    @callback_url.setter
    def callback_url(self, callback_url):
        """Sets the callback_url of this WebhookCreateParameters.

        Callback URL to send requests to  # noqa: E501

        :param callback_url: The callback_url of this WebhookCreateParameters.  # noqa: E501
        :type: str
        """

        self._callback_url = callback_url

    @property
    def secret(self):
        """Gets the secret of this WebhookCreateParameters.  # noqa: E501

        Webhook secret used to calculate signature. If empty, the default project secret will be used.  # noqa: E501

        :return: The secret of this WebhookCreateParameters.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this WebhookCreateParameters.

        Webhook secret used to calculate signature. If empty, the default project secret will be used.  # noqa: E501

        :param secret: The secret of this WebhookCreateParameters.  # noqa: E501
        :type: str
        """

        self._secret = secret

    @property
    def description(self):
        """Gets the description of this WebhookCreateParameters.  # noqa: E501

        Webhook description  # noqa: E501

        :return: The description of this WebhookCreateParameters.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WebhookCreateParameters.

        Webhook description  # noqa: E501

        :param description: The description of this WebhookCreateParameters.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def events(self):
        """Gets the events of this WebhookCreateParameters.  # noqa: E501

        List of event names to trigger the webhook (separated by comma)  # noqa: E501

        :return: The events of this WebhookCreateParameters.  # noqa: E501
        :rtype: str
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this WebhookCreateParameters.

        List of event names to trigger the webhook (separated by comma)  # noqa: E501

        :param events: The events of this WebhookCreateParameters.  # noqa: E501
        :type: str
        """

        self._events = events

    @property
    def active(self):
        """Gets the active of this WebhookCreateParameters.  # noqa: E501

        Whether webhook is active or inactive  # noqa: E501

        :return: The active of this WebhookCreateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this WebhookCreateParameters.

        Whether webhook is active or inactive  # noqa: E501

        :param active: The active of this WebhookCreateParameters.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def include_branches(self):
        """Gets the include_branches of this WebhookCreateParameters.  # noqa: E501

        If enabled, webhook will also be triggered for events from branches of the project specified.  # noqa: E501

        :return: The include_branches of this WebhookCreateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._include_branches

    @include_branches.setter
    def include_branches(self, include_branches):
        """Sets the include_branches of this WebhookCreateParameters.

        If enabled, webhook will also be triggered for events from branches of the project specified.  # noqa: E501

        :param include_branches: The include_branches of this WebhookCreateParameters.  # noqa: E501
        :type: bool
        """

        self._include_branches = include_branches

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
        if not isinstance(other, WebhookCreateParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WebhookCreateParameters):
            return True

        return self.to_dict() != other.to_dict()

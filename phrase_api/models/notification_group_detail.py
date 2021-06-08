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


class NotificationGroupDetail(object):
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
        'event_name': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'notifications_count': 'int',
        'latest_notification': 'object'
    }

    attribute_map = {
        'id': 'id',
        'event_name': 'event_name',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'notifications_count': 'notifications_count',
        'latest_notification': 'latest_notification'
    }

    def __init__(self, id=None, event_name=None, created_at=None, updated_at=None, notifications_count=None, latest_notification=None, local_vars_configuration=None):  # noqa: E501
        """NotificationGroupDetail - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._event_name = None
        self._created_at = None
        self._updated_at = None
        self._notifications_count = None
        self._latest_notification = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if event_name is not None:
            self.event_name = event_name
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if notifications_count is not None:
            self.notifications_count = notifications_count
        if latest_notification is not None:
            self.latest_notification = latest_notification

    @property
    def id(self):
        """Gets the id of this NotificationGroupDetail.  # noqa: E501


        :return: The id of this NotificationGroupDetail.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NotificationGroupDetail.


        :param id: The id of this NotificationGroupDetail.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def event_name(self):
        """Gets the event_name of this NotificationGroupDetail.  # noqa: E501


        :return: The event_name of this NotificationGroupDetail.  # noqa: E501
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this NotificationGroupDetail.


        :param event_name: The event_name of this NotificationGroupDetail.  # noqa: E501
        :type: str
        """

        self._event_name = event_name

    @property
    def created_at(self):
        """Gets the created_at of this NotificationGroupDetail.  # noqa: E501


        :return: The created_at of this NotificationGroupDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this NotificationGroupDetail.


        :param created_at: The created_at of this NotificationGroupDetail.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this NotificationGroupDetail.  # noqa: E501


        :return: The updated_at of this NotificationGroupDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this NotificationGroupDetail.


        :param updated_at: The updated_at of this NotificationGroupDetail.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def notifications_count(self):
        """Gets the notifications_count of this NotificationGroupDetail.  # noqa: E501


        :return: The notifications_count of this NotificationGroupDetail.  # noqa: E501
        :rtype: int
        """
        return self._notifications_count

    @notifications_count.setter
    def notifications_count(self, notifications_count):
        """Sets the notifications_count of this NotificationGroupDetail.


        :param notifications_count: The notifications_count of this NotificationGroupDetail.  # noqa: E501
        :type: int
        """

        self._notifications_count = notifications_count

    @property
    def latest_notification(self):
        """Gets the latest_notification of this NotificationGroupDetail.  # noqa: E501


        :return: The latest_notification of this NotificationGroupDetail.  # noqa: E501
        :rtype: object
        """
        return self._latest_notification

    @latest_notification.setter
    def latest_notification(self, latest_notification):
        """Sets the latest_notification of this NotificationGroupDetail.


        :param latest_notification: The latest_notification of this NotificationGroupDetail.  # noqa: E501
        :type: object
        """

        self._latest_notification = latest_notification

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
        if not isinstance(other, NotificationGroupDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NotificationGroupDetail):
            return True

        return self.to_dict() != other.to_dict()

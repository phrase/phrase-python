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


class Upload(object):
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
        'filename': 'str',
        'format': 'str',
        'state': 'str',
        'tag': 'str',
        'tags': 'List[str]',
        'url': 'str',
        'summary': 'UploadSummary',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'filename': 'filename',
        'format': 'format',
        'state': 'state',
        'tag': 'tag',
        'tags': 'tags',
        'url': 'url',
        'summary': 'summary',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, filename=None, format=None, state=None, tag=None, tags=None, url=None, summary=None, created_at=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """Upload - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._filename = None
        self._format = None
        self._state = None
        self._tag = None
        self._tags = None
        self._url = None
        self._summary = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if filename is not None:
            self.filename = filename
        if format is not None:
            self.format = format
        if state is not None:
            self.state = state
        if tag is not None:
            self.tag = tag
        if tags is not None:
            self.tags = tags
        if url is not None:
            self.url = url
        if summary is not None:
            self.summary = summary
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this Upload.  # noqa: E501


        :return: The id of this Upload.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Upload.


        :param id: The id of this Upload.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def filename(self):
        """Gets the filename of this Upload.  # noqa: E501


        :return: The filename of this Upload.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this Upload.


        :param filename: The filename of this Upload.  # noqa: E501
        :type: str
        """

        self._filename = filename

    @property
    def format(self):
        """Gets the format of this Upload.  # noqa: E501


        :return: The format of this Upload.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this Upload.


        :param format: The format of this Upload.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def state(self):
        """Gets the state of this Upload.  # noqa: E501


        :return: The state of this Upload.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Upload.


        :param state: The state of this Upload.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def tag(self):
        """Gets the tag of this Upload.  # noqa: E501

        Unique tag of the upload   # noqa: E501

        :return: The tag of this Upload.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this Upload.

        Unique tag of the upload   # noqa: E501

        :param tag: The tag of this Upload.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def tags(self):
        """Gets the tags of this Upload.  # noqa: E501

        List of tags that were assigned to the uploaded keys   # noqa: E501

        :return: The tags of this Upload.  # noqa: E501
        :rtype: List[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Upload.

        List of tags that were assigned to the uploaded keys   # noqa: E501

        :param tags: The tags of this Upload.  # noqa: E501
        :type: List[str]
        """

        self._tags = tags

    @property
    def url(self):
        """Gets the url of this Upload.  # noqa: E501

        The URL to the upload in Phrase Strings app.   # noqa: E501

        :return: The url of this Upload.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Upload.

        The URL to the upload in Phrase Strings app.   # noqa: E501

        :param url: The url of this Upload.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def summary(self):
        """Gets the summary of this Upload.  # noqa: E501


        :return: The summary of this Upload.  # noqa: E501
        :rtype: UploadSummary
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this Upload.


        :param summary: The summary of this Upload.  # noqa: E501
        :type: UploadSummary
        """

        self._summary = summary

    @property
    def created_at(self):
        """Gets the created_at of this Upload.  # noqa: E501


        :return: The created_at of this Upload.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Upload.


        :param created_at: The created_at of this Upload.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Upload.  # noqa: E501


        :return: The updated_at of this Upload.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Upload.


        :param updated_at: The updated_at of this Upload.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
        if not isinstance(other, Upload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Upload):
            return True

        return self.to_dict() != other.to_dict()

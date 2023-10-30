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


class DistributionPreview(object):
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
        'name': 'str',
        'project': 'ProjectShort',
        'platforms': 'List[str]',
        'release_count': 'int',
        'created_at': 'datetime',
        'deleted_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'project': 'project',
        'platforms': 'platforms',
        'release_count': 'release_count',
        'created_at': 'created_at',
        'deleted_at': 'deleted_at'
    }

    def __init__(self, id=None, name=None, project=None, platforms=None, release_count=None, created_at=None, deleted_at=None, local_vars_configuration=None):  # noqa: E501
        """DistributionPreview - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._project = None
        self._platforms = None
        self._release_count = None
        self._created_at = None
        self._deleted_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if project is not None:
            self.project = project
        if platforms is not None:
            self.platforms = platforms
        if release_count is not None:
            self.release_count = release_count
        if created_at is not None:
            self.created_at = created_at
        if deleted_at is not None:
            self.deleted_at = deleted_at

    @property
    def id(self):
        """Gets the id of this DistributionPreview.  # noqa: E501


        :return: The id of this DistributionPreview.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DistributionPreview.


        :param id: The id of this DistributionPreview.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this DistributionPreview.  # noqa: E501


        :return: The name of this DistributionPreview.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DistributionPreview.


        :param name: The name of this DistributionPreview.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def project(self):
        """Gets the project of this DistributionPreview.  # noqa: E501


        :return: The project of this DistributionPreview.  # noqa: E501
        :rtype: ProjectShort
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this DistributionPreview.


        :param project: The project of this DistributionPreview.  # noqa: E501
        :type: ProjectShort
        """

        self._project = project

    @property
    def platforms(self):
        """Gets the platforms of this DistributionPreview.  # noqa: E501


        :return: The platforms of this DistributionPreview.  # noqa: E501
        :rtype: List[str]
        """
        return self._platforms

    @platforms.setter
    def platforms(self, platforms):
        """Sets the platforms of this DistributionPreview.


        :param platforms: The platforms of this DistributionPreview.  # noqa: E501
        :type: List[str]
        """

        self._platforms = platforms

    @property
    def release_count(self):
        """Gets the release_count of this DistributionPreview.  # noqa: E501


        :return: The release_count of this DistributionPreview.  # noqa: E501
        :rtype: int
        """
        return self._release_count

    @release_count.setter
    def release_count(self, release_count):
        """Sets the release_count of this DistributionPreview.


        :param release_count: The release_count of this DistributionPreview.  # noqa: E501
        :type: int
        """

        self._release_count = release_count

    @property
    def created_at(self):
        """Gets the created_at of this DistributionPreview.  # noqa: E501


        :return: The created_at of this DistributionPreview.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DistributionPreview.


        :param created_at: The created_at of this DistributionPreview.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def deleted_at(self):
        """Gets the deleted_at of this DistributionPreview.  # noqa: E501


        :return: The deleted_at of this DistributionPreview.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this DistributionPreview.


        :param deleted_at: The deleted_at of this DistributionPreview.  # noqa: E501
        :type: datetime
        """

        self._deleted_at = deleted_at

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
        if not isinstance(other, DistributionPreview):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DistributionPreview):
            return True

        return self.to_dict() != other.to_dict()

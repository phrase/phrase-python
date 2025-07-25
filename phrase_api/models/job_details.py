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


class JobDetails(object):
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
        'briefing': 'str',
        'due_date': 'datetime',
        'state': 'str',
        'ticket_url': 'str',
        'project': 'ProjectShort',
        'branch': 'BranchName',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'owner': 'UserPreview',
        'job_tag_name': 'str',
        'source_translations_updated_at': 'datetime',
        'source_locale': 'LocalePreview',
        'locales': 'List[LocalePreview]',
        'keys': 'List[KeyPreview]',
        'annotations': 'List[JobAnnotationShort]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'briefing': 'briefing',
        'due_date': 'due_date',
        'state': 'state',
        'ticket_url': 'ticket_url',
        'project': 'project',
        'branch': 'branch',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'owner': 'owner',
        'job_tag_name': 'job_tag_name',
        'source_translations_updated_at': 'source_translations_updated_at',
        'source_locale': 'source_locale',
        'locales': 'locales',
        'keys': 'keys',
        'annotations': 'annotations'
    }

    def __init__(self, id=None, name=None, briefing=None, due_date=None, state=None, ticket_url=None, project=None, branch=None, created_at=None, updated_at=None, owner=None, job_tag_name=None, source_translations_updated_at=None, source_locale=None, locales=None, keys=None, annotations=None, local_vars_configuration=None):  # noqa: E501
        """JobDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._briefing = None
        self._due_date = None
        self._state = None
        self._ticket_url = None
        self._project = None
        self._branch = None
        self._created_at = None
        self._updated_at = None
        self._owner = None
        self._job_tag_name = None
        self._source_translations_updated_at = None
        self._source_locale = None
        self._locales = None
        self._keys = None
        self._annotations = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if briefing is not None:
            self.briefing = briefing
        self.due_date = due_date
        if state is not None:
            self.state = state
        if ticket_url is not None:
            self.ticket_url = ticket_url
        if project is not None:
            self.project = project
        if branch is not None:
            self.branch = branch
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if owner is not None:
            self.owner = owner
        if job_tag_name is not None:
            self.job_tag_name = job_tag_name
        if source_translations_updated_at is not None:
            self.source_translations_updated_at = source_translations_updated_at
        if source_locale is not None:
            self.source_locale = source_locale
        if locales is not None:
            self.locales = locales
        if keys is not None:
            self.keys = keys
        if annotations is not None:
            self.annotations = annotations

    @property
    def id(self):
        """Gets the id of this JobDetails.  # noqa: E501


        :return: The id of this JobDetails.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JobDetails.


        :param id: The id of this JobDetails.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this JobDetails.  # noqa: E501


        :return: The name of this JobDetails.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JobDetails.


        :param name: The name of this JobDetails.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def briefing(self):
        """Gets the briefing of this JobDetails.  # noqa: E501


        :return: The briefing of this JobDetails.  # noqa: E501
        :rtype: str
        """
        return self._briefing

    @briefing.setter
    def briefing(self, briefing):
        """Sets the briefing of this JobDetails.


        :param briefing: The briefing of this JobDetails.  # noqa: E501
        :type: str
        """

        self._briefing = briefing

    @property
    def due_date(self):
        """Gets the due_date of this JobDetails.  # noqa: E501


        :return: The due_date of this JobDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this JobDetails.


        :param due_date: The due_date of this JobDetails.  # noqa: E501
        :type: datetime
        """

        self._due_date = due_date

    @property
    def state(self):
        """Gets the state of this JobDetails.  # noqa: E501


        :return: The state of this JobDetails.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this JobDetails.


        :param state: The state of this JobDetails.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def ticket_url(self):
        """Gets the ticket_url of this JobDetails.  # noqa: E501


        :return: The ticket_url of this JobDetails.  # noqa: E501
        :rtype: str
        """
        return self._ticket_url

    @ticket_url.setter
    def ticket_url(self, ticket_url):
        """Sets the ticket_url of this JobDetails.


        :param ticket_url: The ticket_url of this JobDetails.  # noqa: E501
        :type: str
        """

        self._ticket_url = ticket_url

    @property
    def project(self):
        """Gets the project of this JobDetails.  # noqa: E501


        :return: The project of this JobDetails.  # noqa: E501
        :rtype: ProjectShort
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this JobDetails.


        :param project: The project of this JobDetails.  # noqa: E501
        :type: ProjectShort
        """

        self._project = project

    @property
    def branch(self):
        """Gets the branch of this JobDetails.  # noqa: E501


        :return: The branch of this JobDetails.  # noqa: E501
        :rtype: BranchName
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this JobDetails.


        :param branch: The branch of this JobDetails.  # noqa: E501
        :type: BranchName
        """

        self._branch = branch

    @property
    def created_at(self):
        """Gets the created_at of this JobDetails.  # noqa: E501


        :return: The created_at of this JobDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this JobDetails.


        :param created_at: The created_at of this JobDetails.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this JobDetails.  # noqa: E501


        :return: The updated_at of this JobDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this JobDetails.


        :param updated_at: The updated_at of this JobDetails.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def owner(self):
        """Gets the owner of this JobDetails.  # noqa: E501


        :return: The owner of this JobDetails.  # noqa: E501
        :rtype: UserPreview
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this JobDetails.


        :param owner: The owner of this JobDetails.  # noqa: E501
        :type: UserPreview
        """

        self._owner = owner

    @property
    def job_tag_name(self):
        """Gets the job_tag_name of this JobDetails.  # noqa: E501


        :return: The job_tag_name of this JobDetails.  # noqa: E501
        :rtype: str
        """
        return self._job_tag_name

    @job_tag_name.setter
    def job_tag_name(self, job_tag_name):
        """Sets the job_tag_name of this JobDetails.


        :param job_tag_name: The job_tag_name of this JobDetails.  # noqa: E501
        :type: str
        """

        self._job_tag_name = job_tag_name

    @property
    def source_translations_updated_at(self):
        """Gets the source_translations_updated_at of this JobDetails.  # noqa: E501


        :return: The source_translations_updated_at of this JobDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._source_translations_updated_at

    @source_translations_updated_at.setter
    def source_translations_updated_at(self, source_translations_updated_at):
        """Sets the source_translations_updated_at of this JobDetails.


        :param source_translations_updated_at: The source_translations_updated_at of this JobDetails.  # noqa: E501
        :type: datetime
        """

        self._source_translations_updated_at = source_translations_updated_at

    @property
    def source_locale(self):
        """Gets the source_locale of this JobDetails.  # noqa: E501


        :return: The source_locale of this JobDetails.  # noqa: E501
        :rtype: LocalePreview
        """
        return self._source_locale

    @source_locale.setter
    def source_locale(self, source_locale):
        """Sets the source_locale of this JobDetails.


        :param source_locale: The source_locale of this JobDetails.  # noqa: E501
        :type: LocalePreview
        """

        self._source_locale = source_locale

    @property
    def locales(self):
        """Gets the locales of this JobDetails.  # noqa: E501


        :return: The locales of this JobDetails.  # noqa: E501
        :rtype: List[LocalePreview]
        """
        return self._locales

    @locales.setter
    def locales(self, locales):
        """Sets the locales of this JobDetails.


        :param locales: The locales of this JobDetails.  # noqa: E501
        :type: List[LocalePreview]
        """

        self._locales = locales

    @property
    def keys(self):
        """Gets the keys of this JobDetails.  # noqa: E501


        :return: The keys of this JobDetails.  # noqa: E501
        :rtype: List[KeyPreview]
        """
        return self._keys

    @keys.setter
    def keys(self, keys):
        """Sets the keys of this JobDetails.


        :param keys: The keys of this JobDetails.  # noqa: E501
        :type: List[KeyPreview]
        """

        self._keys = keys

    @property
    def annotations(self):
        """Gets the annotations of this JobDetails.  # noqa: E501


        :return: The annotations of this JobDetails.  # noqa: E501
        :rtype: List[JobAnnotationShort]
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this JobDetails.


        :param annotations: The annotations of this JobDetails.  # noqa: E501
        :type: List[JobAnnotationShort]
        """

        self._annotations = annotations

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
        if not isinstance(other, JobDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JobDetails):
            return True

        return self.to_dict() != other.to_dict()

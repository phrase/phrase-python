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


class ProjectUpdateParameters(object):
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
        'account_id': 'str',
        'name': 'str',
        'point_of_contact': 'str',
        'main_format': 'str',
        'media': 'str',
        'shares_translation_memory': 'bool',
        'project_image': 'bytearray',
        'remove_project_image': 'bool',
        'workflow': 'str',
        'machine_translation_enabled': 'bool',
        'enable_branching': 'bool',
        'protect_master_branch': 'bool',
        'enable_all_data_type_translation_keys_for_translators': 'bool',
        'enable_icu_message_format': 'bool',
        'zero_plural_form_enabled': 'bool',
        'autotranslate_enabled': 'bool',
        'autotranslate_check_new_translation_keys': 'bool',
        'autotranslate_check_new_uploads': 'bool',
        'autotranslate_check_new_locales': 'bool',
        'autotranslate_mark_as_unverified': 'bool',
        'autotranslate_use_machine_translation': 'bool',
        'autotranslate_use_translation_memory': 'bool',
        'default_encoding': 'str'
    }

    attribute_map = {
        'account_id': 'account_id',
        'name': 'name',
        'point_of_contact': 'point_of_contact',
        'main_format': 'main_format',
        'media': 'media',
        'shares_translation_memory': 'shares_translation_memory',
        'project_image': 'project_image',
        'remove_project_image': 'remove_project_image',
        'workflow': 'workflow',
        'machine_translation_enabled': 'machine_translation_enabled',
        'enable_branching': 'enable_branching',
        'protect_master_branch': 'protect_master_branch',
        'enable_all_data_type_translation_keys_for_translators': 'enable_all_data_type_translation_keys_for_translators',
        'enable_icu_message_format': 'enable_icu_message_format',
        'zero_plural_form_enabled': 'zero_plural_form_enabled',
        'autotranslate_enabled': 'autotranslate_enabled',
        'autotranslate_check_new_translation_keys': 'autotranslate_check_new_translation_keys',
        'autotranslate_check_new_uploads': 'autotranslate_check_new_uploads',
        'autotranslate_check_new_locales': 'autotranslate_check_new_locales',
        'autotranslate_mark_as_unverified': 'autotranslate_mark_as_unverified',
        'autotranslate_use_machine_translation': 'autotranslate_use_machine_translation',
        'autotranslate_use_translation_memory': 'autotranslate_use_translation_memory',
        'default_encoding': 'default_encoding'
    }

    def __init__(self, account_id=None, name=None, point_of_contact=None, main_format=None, media=None, shares_translation_memory=None, project_image=None, remove_project_image=None, workflow=None, machine_translation_enabled=None, enable_branching=None, protect_master_branch=None, enable_all_data_type_translation_keys_for_translators=None, enable_icu_message_format=None, zero_plural_form_enabled=None, autotranslate_enabled=None, autotranslate_check_new_translation_keys=None, autotranslate_check_new_uploads=None, autotranslate_check_new_locales=None, autotranslate_mark_as_unverified=None, autotranslate_use_machine_translation=None, autotranslate_use_translation_memory=None, default_encoding=None, local_vars_configuration=None):  # noqa: E501
        """ProjectUpdateParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._name = None
        self._point_of_contact = None
        self._main_format = None
        self._media = None
        self._shares_translation_memory = None
        self._project_image = None
        self._remove_project_image = None
        self._workflow = None
        self._machine_translation_enabled = None
        self._enable_branching = None
        self._protect_master_branch = None
        self._enable_all_data_type_translation_keys_for_translators = None
        self._enable_icu_message_format = None
        self._zero_plural_form_enabled = None
        self._autotranslate_enabled = None
        self._autotranslate_check_new_translation_keys = None
        self._autotranslate_check_new_uploads = None
        self._autotranslate_check_new_locales = None
        self._autotranslate_mark_as_unverified = None
        self._autotranslate_use_machine_translation = None
        self._autotranslate_use_translation_memory = None
        self._default_encoding = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if name is not None:
            self.name = name
        if point_of_contact is not None:
            self.point_of_contact = point_of_contact
        if main_format is not None:
            self.main_format = main_format
        if media is not None:
            self.media = media
        if shares_translation_memory is not None:
            self.shares_translation_memory = shares_translation_memory
        if project_image is not None:
            self.project_image = project_image
        if remove_project_image is not None:
            self.remove_project_image = remove_project_image
        if workflow is not None:
            self.workflow = workflow
        if machine_translation_enabled is not None:
            self.machine_translation_enabled = machine_translation_enabled
        if enable_branching is not None:
            self.enable_branching = enable_branching
        if protect_master_branch is not None:
            self.protect_master_branch = protect_master_branch
        if enable_all_data_type_translation_keys_for_translators is not None:
            self.enable_all_data_type_translation_keys_for_translators = enable_all_data_type_translation_keys_for_translators
        if enable_icu_message_format is not None:
            self.enable_icu_message_format = enable_icu_message_format
        if zero_plural_form_enabled is not None:
            self.zero_plural_form_enabled = zero_plural_form_enabled
        if autotranslate_enabled is not None:
            self.autotranslate_enabled = autotranslate_enabled
        if autotranslate_check_new_translation_keys is not None:
            self.autotranslate_check_new_translation_keys = autotranslate_check_new_translation_keys
        if autotranslate_check_new_uploads is not None:
            self.autotranslate_check_new_uploads = autotranslate_check_new_uploads
        if autotranslate_check_new_locales is not None:
            self.autotranslate_check_new_locales = autotranslate_check_new_locales
        if autotranslate_mark_as_unverified is not None:
            self.autotranslate_mark_as_unverified = autotranslate_mark_as_unverified
        if autotranslate_use_machine_translation is not None:
            self.autotranslate_use_machine_translation = autotranslate_use_machine_translation
        if autotranslate_use_translation_memory is not None:
            self.autotranslate_use_translation_memory = autotranslate_use_translation_memory
        if default_encoding is not None:
            self.default_encoding = default_encoding

    @property
    def account_id(self):
        """Gets the account_id of this ProjectUpdateParameters.  # noqa: E501

        Required if the requesting user is a member of multiple accounts. Account ID to specify the actual account the project should be created in.  # noqa: E501

        :return: The account_id of this ProjectUpdateParameters.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this ProjectUpdateParameters.

        Required if the requesting user is a member of multiple accounts. Account ID to specify the actual account the project should be created in.  # noqa: E501

        :param account_id: The account_id of this ProjectUpdateParameters.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def name(self):
        """Gets the name of this ProjectUpdateParameters.  # noqa: E501

        (Optional) Name of the project  # noqa: E501

        :return: The name of this ProjectUpdateParameters.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectUpdateParameters.

        (Optional) Name of the project  # noqa: E501

        :param name: The name of this ProjectUpdateParameters.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def point_of_contact(self):
        """Gets the point_of_contact of this ProjectUpdateParameters.  # noqa: E501

        (Optional) User ID of the point of contact for the project. Pass `null` to unset.  # noqa: E501

        :return: The point_of_contact of this ProjectUpdateParameters.  # noqa: E501
        :rtype: str
        """
        return self._point_of_contact

    @point_of_contact.setter
    def point_of_contact(self, point_of_contact):
        """Sets the point_of_contact of this ProjectUpdateParameters.

        (Optional) User ID of the point of contact for the project. Pass `null` to unset.  # noqa: E501

        :param point_of_contact: The point_of_contact of this ProjectUpdateParameters.  # noqa: E501
        :type: str
        """

        self._point_of_contact = point_of_contact

    @property
    def main_format(self):
        """Gets the main_format of this ProjectUpdateParameters.  # noqa: E501

        (Optional) Main file format specified by its API Extension name. Used for locale downloads if no format is specified. For API Extension names of available file formats see <a href=\"https://support.phrase.com/hc/en-us/sections/6111343326364\">Format Guide</a> or our <a href=\"#formats\">Formats API Endpoint</a>.  # noqa: E501

        :return: The main_format of this ProjectUpdateParameters.  # noqa: E501
        :rtype: str
        """
        return self._main_format

    @main_format.setter
    def main_format(self, main_format):
        """Sets the main_format of this ProjectUpdateParameters.

        (Optional) Main file format specified by its API Extension name. Used for locale downloads if no format is specified. For API Extension names of available file formats see <a href=\"https://support.phrase.com/hc/en-us/sections/6111343326364\">Format Guide</a> or our <a href=\"#formats\">Formats API Endpoint</a>.  # noqa: E501

        :param main_format: The main_format of this ProjectUpdateParameters.  # noqa: E501
        :type: str
        """

        self._main_format = main_format

    @property
    def media(self):
        """Gets the media of this ProjectUpdateParameters.  # noqa: E501

        (Optional) Main technology stack used in the project. It affects for example the suggested placeholder style. Predefined values include: `Ruby`, `JavaScript`, `AngularJS`, `React`, `iOS`, `Android`, `Python`, `PHP`, `Java`, `Go`, `Windows Phone`, `Rails`, `Node.js`, `.NET`, `Django`, `Symfony`, `Yii Framework`, `Zend Framework`, `Apple App Store Description`, `Google Play Description`, but it can also take any other value.  # noqa: E501

        :return: The media of this ProjectUpdateParameters.  # noqa: E501
        :rtype: str
        """
        return self._media

    @media.setter
    def media(self, media):
        """Sets the media of this ProjectUpdateParameters.

        (Optional) Main technology stack used in the project. It affects for example the suggested placeholder style. Predefined values include: `Ruby`, `JavaScript`, `AngularJS`, `React`, `iOS`, `Android`, `Python`, `PHP`, `Java`, `Go`, `Windows Phone`, `Rails`, `Node.js`, `.NET`, `Django`, `Symfony`, `Yii Framework`, `Zend Framework`, `Apple App Store Description`, `Google Play Description`, but it can also take any other value.  # noqa: E501

        :param media: The media of this ProjectUpdateParameters.  # noqa: E501
        :type: str
        """

        self._media = media

    @property
    def shares_translation_memory(self):
        """Gets the shares_translation_memory of this ProjectUpdateParameters.  # noqa: E501

        (Optional) Indicates whether the project should share the account's translation memory  # noqa: E501

        :return: The shares_translation_memory of this ProjectUpdateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._shares_translation_memory

    @shares_translation_memory.setter
    def shares_translation_memory(self, shares_translation_memory):
        """Sets the shares_translation_memory of this ProjectUpdateParameters.

        (Optional) Indicates whether the project should share the account's translation memory  # noqa: E501

        :param shares_translation_memory: The shares_translation_memory of this ProjectUpdateParameters.  # noqa: E501
        :type: bool
        """

        self._shares_translation_memory = shares_translation_memory

    @property
    def project_image(self):
        """Gets the project_image of this ProjectUpdateParameters.  # noqa: E501

        (Optional) Image to identify the project  # noqa: E501

        :return: The project_image of this ProjectUpdateParameters.  # noqa: E501
        :rtype: bytearray
        """
        return self._project_image

    @project_image.setter
    def project_image(self, project_image):
        """Sets the project_image of this ProjectUpdateParameters.

        (Optional) Image to identify the project  # noqa: E501

        :param project_image: The project_image of this ProjectUpdateParameters.  # noqa: E501
        :type: bytearray
        """

        self._project_image = project_image

    @property
    def remove_project_image(self):
        """Gets the remove_project_image of this ProjectUpdateParameters.  # noqa: E501

        (Optional) Indicates whether the project image should be deleted.  # noqa: E501

        :return: The remove_project_image of this ProjectUpdateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._remove_project_image

    @remove_project_image.setter
    def remove_project_image(self, remove_project_image):
        """Sets the remove_project_image of this ProjectUpdateParameters.

        (Optional) Indicates whether the project image should be deleted.  # noqa: E501

        :param remove_project_image: The remove_project_image of this ProjectUpdateParameters.  # noqa: E501
        :type: bool
        """

        self._remove_project_image = remove_project_image

    @property
    def workflow(self):
        """Gets the workflow of this ProjectUpdateParameters.  # noqa: E501

        (Optional) Review Workflow. \"simple\" / \"review\". <a href=\"https://support.phrase.com/hc/en-us/articles/5784094755484\">Read more</a>  # noqa: E501

        :return: The workflow of this ProjectUpdateParameters.  # noqa: E501
        :rtype: str
        """
        return self._workflow

    @workflow.setter
    def workflow(self, workflow):
        """Sets the workflow of this ProjectUpdateParameters.

        (Optional) Review Workflow. \"simple\" / \"review\". <a href=\"https://support.phrase.com/hc/en-us/articles/5784094755484\">Read more</a>  # noqa: E501

        :param workflow: The workflow of this ProjectUpdateParameters.  # noqa: E501
        :type: str
        """

        self._workflow = workflow

    @property
    def machine_translation_enabled(self):
        """Gets the machine_translation_enabled of this ProjectUpdateParameters.  # noqa: E501

        (Optional) Enable machine translation support in the project. Required for Pre-Translation  # noqa: E501

        :return: The machine_translation_enabled of this ProjectUpdateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._machine_translation_enabled

    @machine_translation_enabled.setter
    def machine_translation_enabled(self, machine_translation_enabled):
        """Sets the machine_translation_enabled of this ProjectUpdateParameters.

        (Optional) Enable machine translation support in the project. Required for Pre-Translation  # noqa: E501

        :param machine_translation_enabled: The machine_translation_enabled of this ProjectUpdateParameters.  # noqa: E501
        :type: bool
        """

        self._machine_translation_enabled = machine_translation_enabled

    @property
    def enable_branching(self):
        """Gets the enable_branching of this ProjectUpdateParameters.  # noqa: E501

        (Optional) Enable branching in the project  # noqa: E501

        :return: The enable_branching of this ProjectUpdateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._enable_branching

    @enable_branching.setter
    def enable_branching(self, enable_branching):
        """Sets the enable_branching of this ProjectUpdateParameters.

        (Optional) Enable branching in the project  # noqa: E501

        :param enable_branching: The enable_branching of this ProjectUpdateParameters.  # noqa: E501
        :type: bool
        """

        self._enable_branching = enable_branching

    @property
    def protect_master_branch(self):
        """Gets the protect_master_branch of this ProjectUpdateParameters.  # noqa: E501

        (Optional) Protect the master branch in project where branching is enabled  # noqa: E501

        :return: The protect_master_branch of this ProjectUpdateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._protect_master_branch

    @protect_master_branch.setter
    def protect_master_branch(self, protect_master_branch):
        """Sets the protect_master_branch of this ProjectUpdateParameters.

        (Optional) Protect the master branch in project where branching is enabled  # noqa: E501

        :param protect_master_branch: The protect_master_branch of this ProjectUpdateParameters.  # noqa: E501
        :type: bool
        """

        self._protect_master_branch = protect_master_branch

    @property
    def enable_all_data_type_translation_keys_for_translators(self):
        """Gets the enable_all_data_type_translation_keys_for_translators of this ProjectUpdateParameters.  # noqa: E501

        (Optional) Otherwise, translators are not allowed to edit translations other than strings  # noqa: E501

        :return: The enable_all_data_type_translation_keys_for_translators of this ProjectUpdateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._enable_all_data_type_translation_keys_for_translators

    @enable_all_data_type_translation_keys_for_translators.setter
    def enable_all_data_type_translation_keys_for_translators(self, enable_all_data_type_translation_keys_for_translators):
        """Sets the enable_all_data_type_translation_keys_for_translators of this ProjectUpdateParameters.

        (Optional) Otherwise, translators are not allowed to edit translations other than strings  # noqa: E501

        :param enable_all_data_type_translation_keys_for_translators: The enable_all_data_type_translation_keys_for_translators of this ProjectUpdateParameters.  # noqa: E501
        :type: bool
        """

        self._enable_all_data_type_translation_keys_for_translators = enable_all_data_type_translation_keys_for_translators

    @property
    def enable_icu_message_format(self):
        """Gets the enable_icu_message_format of this ProjectUpdateParameters.  # noqa: E501

        (Optional) We can validate and highlight your ICU messages. <a href=\"https://support.phrase.com/hc/en-us/articles/5822319545116\">Read more</a>  # noqa: E501

        :return: The enable_icu_message_format of this ProjectUpdateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._enable_icu_message_format

    @enable_icu_message_format.setter
    def enable_icu_message_format(self, enable_icu_message_format):
        """Sets the enable_icu_message_format of this ProjectUpdateParameters.

        (Optional) We can validate and highlight your ICU messages. <a href=\"https://support.phrase.com/hc/en-us/articles/5822319545116\">Read more</a>  # noqa: E501

        :param enable_icu_message_format: The enable_icu_message_format of this ProjectUpdateParameters.  # noqa: E501
        :type: bool
        """

        self._enable_icu_message_format = enable_icu_message_format

    @property
    def zero_plural_form_enabled(self):
        """Gets the zero_plural_form_enabled of this ProjectUpdateParameters.  # noqa: E501

        (Optional) Displays the input fields for the 'ZERO' plural form for every key as well although only some languages require the 'ZERO' explicitly.  # noqa: E501

        :return: The zero_plural_form_enabled of this ProjectUpdateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._zero_plural_form_enabled

    @zero_plural_form_enabled.setter
    def zero_plural_form_enabled(self, zero_plural_form_enabled):
        """Sets the zero_plural_form_enabled of this ProjectUpdateParameters.

        (Optional) Displays the input fields for the 'ZERO' plural form for every key as well although only some languages require the 'ZERO' explicitly.  # noqa: E501

        :param zero_plural_form_enabled: The zero_plural_form_enabled of this ProjectUpdateParameters.  # noqa: E501
        :type: bool
        """

        self._zero_plural_form_enabled = zero_plural_form_enabled

    @property
    def autotranslate_enabled(self):
        """Gets the autotranslate_enabled of this ProjectUpdateParameters.  # noqa: E501

        (Optional) Autopilot, requires machine_translation_enabled. <a href=\"https://support.phrase.com/hc/en-us/articles/5822187934364\">Read more</a>  # noqa: E501

        :return: The autotranslate_enabled of this ProjectUpdateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._autotranslate_enabled

    @autotranslate_enabled.setter
    def autotranslate_enabled(self, autotranslate_enabled):
        """Sets the autotranslate_enabled of this ProjectUpdateParameters.

        (Optional) Autopilot, requires machine_translation_enabled. <a href=\"https://support.phrase.com/hc/en-us/articles/5822187934364\">Read more</a>  # noqa: E501

        :param autotranslate_enabled: The autotranslate_enabled of this ProjectUpdateParameters.  # noqa: E501
        :type: bool
        """

        self._autotranslate_enabled = autotranslate_enabled

    @property
    def autotranslate_check_new_translation_keys(self):
        """Gets the autotranslate_check_new_translation_keys of this ProjectUpdateParameters.  # noqa: E501

        (Optional) Requires autotranslate_enabled to be true  # noqa: E501

        :return: The autotranslate_check_new_translation_keys of this ProjectUpdateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._autotranslate_check_new_translation_keys

    @autotranslate_check_new_translation_keys.setter
    def autotranslate_check_new_translation_keys(self, autotranslate_check_new_translation_keys):
        """Sets the autotranslate_check_new_translation_keys of this ProjectUpdateParameters.

        (Optional) Requires autotranslate_enabled to be true  # noqa: E501

        :param autotranslate_check_new_translation_keys: The autotranslate_check_new_translation_keys of this ProjectUpdateParameters.  # noqa: E501
        :type: bool
        """

        self._autotranslate_check_new_translation_keys = autotranslate_check_new_translation_keys

    @property
    def autotranslate_check_new_uploads(self):
        """Gets the autotranslate_check_new_uploads of this ProjectUpdateParameters.  # noqa: E501

        (Optional) Requires autotranslate_enabled to be true  # noqa: E501

        :return: The autotranslate_check_new_uploads of this ProjectUpdateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._autotranslate_check_new_uploads

    @autotranslate_check_new_uploads.setter
    def autotranslate_check_new_uploads(self, autotranslate_check_new_uploads):
        """Sets the autotranslate_check_new_uploads of this ProjectUpdateParameters.

        (Optional) Requires autotranslate_enabled to be true  # noqa: E501

        :param autotranslate_check_new_uploads: The autotranslate_check_new_uploads of this ProjectUpdateParameters.  # noqa: E501
        :type: bool
        """

        self._autotranslate_check_new_uploads = autotranslate_check_new_uploads

    @property
    def autotranslate_check_new_locales(self):
        """Gets the autotranslate_check_new_locales of this ProjectUpdateParameters.  # noqa: E501

        (Optional) Requires autotranslate_enabled to be true  # noqa: E501

        :return: The autotranslate_check_new_locales of this ProjectUpdateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._autotranslate_check_new_locales

    @autotranslate_check_new_locales.setter
    def autotranslate_check_new_locales(self, autotranslate_check_new_locales):
        """Sets the autotranslate_check_new_locales of this ProjectUpdateParameters.

        (Optional) Requires autotranslate_enabled to be true  # noqa: E501

        :param autotranslate_check_new_locales: The autotranslate_check_new_locales of this ProjectUpdateParameters.  # noqa: E501
        :type: bool
        """

        self._autotranslate_check_new_locales = autotranslate_check_new_locales

    @property
    def autotranslate_mark_as_unverified(self):
        """Gets the autotranslate_mark_as_unverified of this ProjectUpdateParameters.  # noqa: E501

        (Optional) Requires autotranslate_enabled to be true  # noqa: E501

        :return: The autotranslate_mark_as_unverified of this ProjectUpdateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._autotranslate_mark_as_unverified

    @autotranslate_mark_as_unverified.setter
    def autotranslate_mark_as_unverified(self, autotranslate_mark_as_unverified):
        """Sets the autotranslate_mark_as_unverified of this ProjectUpdateParameters.

        (Optional) Requires autotranslate_enabled to be true  # noqa: E501

        :param autotranslate_mark_as_unverified: The autotranslate_mark_as_unverified of this ProjectUpdateParameters.  # noqa: E501
        :type: bool
        """

        self._autotranslate_mark_as_unverified = autotranslate_mark_as_unverified

    @property
    def autotranslate_use_machine_translation(self):
        """Gets the autotranslate_use_machine_translation of this ProjectUpdateParameters.  # noqa: E501

        (Optional) Requires autotranslate_enabled to be true  # noqa: E501

        :return: The autotranslate_use_machine_translation of this ProjectUpdateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._autotranslate_use_machine_translation

    @autotranslate_use_machine_translation.setter
    def autotranslate_use_machine_translation(self, autotranslate_use_machine_translation):
        """Sets the autotranslate_use_machine_translation of this ProjectUpdateParameters.

        (Optional) Requires autotranslate_enabled to be true  # noqa: E501

        :param autotranslate_use_machine_translation: The autotranslate_use_machine_translation of this ProjectUpdateParameters.  # noqa: E501
        :type: bool
        """

        self._autotranslate_use_machine_translation = autotranslate_use_machine_translation

    @property
    def autotranslate_use_translation_memory(self):
        """Gets the autotranslate_use_translation_memory of this ProjectUpdateParameters.  # noqa: E501

        (Optional) Requires autotranslate_enabled to be true  # noqa: E501

        :return: The autotranslate_use_translation_memory of this ProjectUpdateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._autotranslate_use_translation_memory

    @autotranslate_use_translation_memory.setter
    def autotranslate_use_translation_memory(self, autotranslate_use_translation_memory):
        """Sets the autotranslate_use_translation_memory of this ProjectUpdateParameters.

        (Optional) Requires autotranslate_enabled to be true  # noqa: E501

        :param autotranslate_use_translation_memory: The autotranslate_use_translation_memory of this ProjectUpdateParameters.  # noqa: E501
        :type: bool
        """

        self._autotranslate_use_translation_memory = autotranslate_use_translation_memory

    @property
    def default_encoding(self):
        """Gets the default_encoding of this ProjectUpdateParameters.  # noqa: E501

        (Optional) Sets the default encoding for Uploads. If you leave it empty, we will try to guess it automatically for you when you Upload a file. You can still override this value by setting the <a href='#post-/projects/-project_id-/uploads'>`file_encoding`</a> parameter for Uploads.  # noqa: E501

        :return: The default_encoding of this ProjectUpdateParameters.  # noqa: E501
        :rtype: str
        """
        return self._default_encoding

    @default_encoding.setter
    def default_encoding(self, default_encoding):
        """Sets the default_encoding of this ProjectUpdateParameters.

        (Optional) Sets the default encoding for Uploads. If you leave it empty, we will try to guess it automatically for you when you Upload a file. You can still override this value by setting the <a href='#post-/projects/-project_id-/uploads'>`file_encoding`</a> parameter for Uploads.  # noqa: E501

        :param default_encoding: The default_encoding of this ProjectUpdateParameters.  # noqa: E501
        :type: str
        """
        allowed_values = ["UTF-8", "UTF-16", "UTF-16BE", "UTF-16LE", "ISO-8859-1"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and default_encoding not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `default_encoding` ({0}), must be one of {1}"  # noqa: E501
                .format(default_encoding, allowed_values)
            )

        self._default_encoding = default_encoding

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
        if not isinstance(other, ProjectUpdateParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectUpdateParameters):
            return True

        return self.to_dict() != other.to_dict()

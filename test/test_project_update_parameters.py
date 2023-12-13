# coding: utf-8

"""
    Phrase Strings API Reference

    The version of the OpenAPI document: 2.0.0
    Contact: support@phrase.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import phrase_api
from phrase_api.models.project_update_parameters import ProjectUpdateParameters  # noqa: E501
from phrase_api.rest import ApiException

class TestProjectUpdateParameters(unittest.TestCase):
    """ProjectUpdateParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProjectUpdateParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.project_update_parameters.ProjectUpdateParameters()  # noqa: E501

        """
        if include_optional :
            return ProjectUpdateParameters(
                account_id = 'abcd1234', 
                name = 'My Android Project', 
                point_of_contact = 'abcd1234', 
                main_format = 'yml', 
                media = 'Python', 
                shares_translation_memory = True, 
                project_image = '[B@7ba4591', 
                remove_project_image = False, 
                workflow = 'review', 
                machine_translation_enabled = True, 
                enable_branching = True, 
                protect_master_branch = True, 
                enable_all_data_type_translation_keys_for_translators = True, 
                enable_icu_message_format = True, 
                zero_plural_form_enabled = True, 
                autotranslate_enabled = True, 
                autotranslate_check_new_translation_keys = True, 
                autotranslate_check_new_uploads = True, 
                autotranslate_check_new_locales = True, 
                autotranslate_mark_as_unverified = True, 
                autotranslate_use_machine_translation = True, 
                autotranslate_use_translation_memory = True, 
                smart_suggest_enabled = True, 
                smart_suggest_use_glossary = True, 
                smart_suggest_use_machine_translation = True
            )
        else :
            return ProjectUpdateParameters(
        )
        """

    def testProjectUpdateParameters(self):
        """Test ProjectUpdateParameters"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

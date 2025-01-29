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
from phrase_api.models.key_create_parameters import KeyCreateParameters  # noqa: E501
from phrase_api.rest import ApiException

class TestKeyCreateParameters(unittest.TestCase):
    """KeyCreateParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test KeyCreateParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.key_create_parameters.KeyCreateParameters()  # noqa: E501

        """
        if include_optional :
            return KeyCreateParameters(
                branch = 'my-feature-branch', 
                name = 'home.index.headline', 
                description = 'Some description worth knowing...', 
                plural = True, 
                name_plural = 'home.index.headlines', 
                data_type = 'number', 
                tags = 'awesome-feature,needs-proofreading', 
                max_characters_allowed = 140, 
                screenshot = '[B@1148eca4', 
                remove_screenshot = True, 
                unformatted = True, 
                default_translation_content = 'Default translation content', 
                autotranslate = True, 
                xml_space_preserve = True, 
                original_file = '', 
                localized_format_string = '', 
                localized_format_key = '', 
                custom_metadata = {"fruit":"Apple","vegetable":"Tomato"}
            )
        else :
            return KeyCreateParameters(
                name = 'home.index.headline',
        )
        """

    def testKeyCreateParameters(self):
        """Test KeyCreateParameters"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

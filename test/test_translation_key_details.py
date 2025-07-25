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
from phrase_api.models.translation_key_details import TranslationKeyDetails  # noqa: E501
from phrase_api.rest import ApiException

class TestTranslationKeyDetails(unittest.TestCase):
    """TranslationKeyDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TranslationKeyDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.translation_key_details.TranslationKeyDetails()  # noqa: E501

        """
        if include_optional :
            return TranslationKeyDetails(
                id = '', 
                name = '', 
                description = '', 
                name_hash = '', 
                plural = True, 
                use_ordinal_rules = True, 
                tags = [
                    ''
                    ], 
                data_type = '', 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                name_plural = '', 
                comments_count = 56, 
                max_characters_allowed = 56, 
                screenshot_url = '', 
                unformatted = True, 
                xml_space_preserve = True, 
                original_file = '', 
                format_value_type = '', 
                creator = phrase_api.models.user_preview.user_preview(
                    id = '', 
                    username = '', 
                    name = '', 
                    gravatar_uid = '', ), 
                custom_metadata = {
                    'key' : ''
                    }
            )
        else :
            return TranslationKeyDetails(
        )
        """

    def testTranslationKeyDetails(self):
        """Test TranslationKeyDetails"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

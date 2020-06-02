# coding: utf-8

"""
    Phrase API Reference

    The version of the OpenAPI document: 2.0.0
    Contact: support@phrase.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import phrase-api
from phrase-api.models.translation_key_details import TranslationKeyDetails  # noqa: E501
from phrase-api.rest import ApiException

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
        # model = phrase-api.models.translation_key_details.TranslationKeyDetails()  # noqa: E501
        if include_optional :
            return TranslationKeyDetails(
                id = '0', 
                name = '0', 
                description = '0', 
                name_hash = '0', 
                plural = True, 
                tags = [
                    '0'
                    ], 
                data_type = '0', 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                name_plural = '0', 
                comments_count = 56, 
                max_characters_allowed = 56, 
                screenshot_url = '0', 
                unformatted = True, 
                xml_space_preserve = True, 
                original_file = '0', 
                format_value_type = '0', 
                creator = phrase-api.models.user_preview.user_preview(
                    id = '0', 
                    username = '0', 
                    name = '0', )
            )
        else :
            return TranslationKeyDetails(
        )

    def testTranslationKeyDetails(self):
        """Test TranslationKeyDetails"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

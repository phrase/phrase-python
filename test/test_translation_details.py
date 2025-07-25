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
from phrase_api.models.translation_details import TranslationDetails  # noqa: E501
from phrase_api.rest import ApiException

class TestTranslationDetails(unittest.TestCase):
    """TranslationDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TranslationDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.translation_details.TranslationDetails()  # noqa: E501

        """
        if include_optional :
            return TranslationDetails(
                id = '', 
                content = '', 
                unverified = True, 
                excluded = True, 
                plural_suffix = '', 
                key = phrase_api.models.key_preview.key_preview(
                    id = '', 
                    name = '', 
                    plural = True, 
                    use_ordinal_rules = True, ), 
                locale = {"id":"abcd1234cdef1234abcd1234cdef1234","name":"English","code":"en-GB"}, 
                placeholders = [
                    ''
                    ], 
                state = '', 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                user = phrase_api.models.user_preview.user_preview(
                    id = '', 
                    username = '', 
                    name = '', 
                    gravatar_uid = '', ), 
                word_count = 56, 
                linked_translation = {"id":"abcd1234cdef1234abcd1234cdef1234","content":"My parent translation"}
            )
        else :
            return TranslationDetails(
        )
        """

    def testTranslationDetails(self):
        """Test TranslationDetails"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

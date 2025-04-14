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
from phrase_api.models.upload_summary import UploadSummary  # noqa: E501
from phrase_api.rest import ApiException

class TestUploadSummary(unittest.TestCase):
    """UploadSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UploadSummary
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.upload_summary.UploadSummary()  # noqa: E501

        """
        if include_optional :
            return UploadSummary(
                locales_created = 56, 
                translation_keys_created = 56, 
                translation_keys_updated = 56, 
                translation_keys_unmentioned = 56, 
                translations_created = 56, 
                translations_updated = 56, 
                tags_created = 56, 
                translation_keys_ignored = 56, 
                processed_translations = 56, 
                upload_total_translations = 56
            )
        else :
            return UploadSummary(
        )
        """

    def testUploadSummary(self):
        """Test UploadSummary"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

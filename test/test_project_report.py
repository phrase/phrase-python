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
from phrase_api.models.project_report import ProjectReport  # noqa: E501
from phrase_api.rest import ApiException

class TestProjectReport(unittest.TestCase):
    """ProjectReport unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProjectReport
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.project_report.ProjectReport()  # noqa: E501

        """
        if include_optional :
            return ProjectReport(
                locales_count = 56, 
                keys_count = 56, 
                translations_count = 56, 
                untranslated_keys_count = 56, 
                unverified_translations_count = 56, 
                reviewed_translations_count = 56, 
                managed_words_count = 56, 
                project = {"id":"abcd1234cdef1234abcd1234cdef1234","name":"My Android Project","main_format":"xml","created_at":"2015-01-28T09:52:53Z","updated_at":"2015-01-28T09:52:53Z"}
            )
        else :
            return ProjectReport(
        )
        """

    def testProjectReport(self):
        """Test ProjectReport"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

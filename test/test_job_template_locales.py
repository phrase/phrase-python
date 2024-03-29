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
from phrase_api.models.job_template_locales import JobTemplateLocales  # noqa: E501
from phrase_api.rest import ApiException

class TestJobTemplateLocales(unittest.TestCase):
    """JobTemplateLocales unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test JobTemplateLocales
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.job_template_locales.JobTemplateLocales()  # noqa: E501

        """
        if include_optional :
            return JobTemplateLocales(
                id = '', 
                job_template = phrase_api.models.job_template_preview.job_template_preview(
                    id = '', 
                    name = '', ), 
                locale = {"id":"abcd1234cdef1234abcd1234cdef1234","name":"English","code":"en-GB"}, 
                users = [
                    phrase_api.models.locale_user_preview.locale_user_preview(
                        id = '', 
                        username = '', 
                        name = '', 
                        role = '', )
                    ], 
                teams = [
                    phrase_api.models.locale_team_preview.locale_team_preview(
                        id = '', 
                        name = '', 
                        role = '', )
                    ]
            )
        else :
            return JobTemplateLocales(
        )
        """

    def testJobTemplateLocales(self):
        """Test JobTemplateLocales"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

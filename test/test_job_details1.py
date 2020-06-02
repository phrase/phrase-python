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
from phrase-api.models.job_details1 import JobDetails1  # noqa: E501
from phrase-api.rest import ApiException

class TestJobDetails1(unittest.TestCase):
    """JobDetails1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test JobDetails1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase-api.models.job_details1.JobDetails1()  # noqa: E501
        if include_optional :
            return JobDetails1(
                owner = phrase-api.models.user_preview.user_preview(
                    id = '0', 
                    username = '0', 
                    name = '0', ), 
                job_tag_name = '0', 
                locales = [
                    {"id":"abcd1234cdef1234abcd1234cdef1234","name":"English","code":"en-GB"}
                    ], 
                keys = [
                    phrase-api.models.key_preview.key_preview(
                        id = '0', 
                        name = '0', 
                        plural = True, )
                    ]
            )
        else :
            return JobDetails1(
        )

    def testJobDetails1(self):
        """Test JobDetails1"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

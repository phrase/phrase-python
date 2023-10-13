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
from phrase_api.models.project_locales1 import ProjectLocales1  # noqa: E501
from phrase_api.rest import ApiException

class TestProjectLocales1(unittest.TestCase):
    """ProjectLocales1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProjectLocales1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.project_locales1.ProjectLocales1()  # noqa: E501

        """
        if include_optional :
            return ProjectLocales1(
                locales = [
                    {"id":"abcd1234cdef1234abcd1234cdef1234","name":"English","code":"en-GB"}
                    ]
            )
        else :
            return ProjectLocales1(
        )
        """

    def testProjectLocales1(self):
        """Test ProjectLocales1"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

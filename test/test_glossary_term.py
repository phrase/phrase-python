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
from phrase-api.models.glossary_term import GlossaryTerm  # noqa: E501
from phrase-api.rest import ApiException

class TestGlossaryTerm(unittest.TestCase):
    """GlossaryTerm unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GlossaryTerm
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase-api.models.glossary_term.GlossaryTerm()  # noqa: E501
        if include_optional :
            return GlossaryTerm(
                id = '0', 
                term = '0', 
                description = '0', 
                translatable = True, 
                case_sensitive = True, 
                translations = [
                    {"id":"abcd1234cdef1234abcd1234cdef1234","locale_code":"en-US","content":"Save","created_at":"2015-01-28T09:52:53Z","updated_at":"2015-01-28T09:52:53Z"}
                    ], 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return GlossaryTerm(
        )

    def testGlossaryTerm(self):
        """Test GlossaryTerm"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

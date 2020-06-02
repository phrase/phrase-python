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
from phrase-api.models.styleguide_details1 import StyleguideDetails1  # noqa: E501
from phrase-api.rest import ApiException

class TestStyleguideDetails1(unittest.TestCase):
    """StyleguideDetails1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StyleguideDetails1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase-api.models.styleguide_details1.StyleguideDetails1()  # noqa: E501
        if include_optional :
            return StyleguideDetails1(
                public_url = '0', 
                audience = '0', 
                target_audience = '0', 
                grammatical_person = '0', 
                vocabulary_type = '0', 
                business = '0', 
                company_branding = '0', 
                formatting = '0', 
                glossary_terms = '0', 
                grammar_consistency = '0', 
                literal_translation = '0', 
                overall_tone = '0', 
                samples = '0'
            )
        else :
            return StyleguideDetails1(
        )

    def testStyleguideDetails1(self):
        """Test StyleguideDetails1"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

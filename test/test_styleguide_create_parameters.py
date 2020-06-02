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
from phrase-api.models.styleguide_create_parameters import StyleguideCreateParameters  # noqa: E501
from phrase-api.rest import ApiException

class TestStyleguideCreateParameters(unittest.TestCase):
    """StyleguideCreateParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StyleguideCreateParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase-api.models.styleguide_create_parameters.StyleguideCreateParameters()  # noqa: E501
        if include_optional :
            return StyleguideCreateParameters(
                title = 'Web application style guide', 
                audience = 'customer-facing', 
                target_audience = 'teenager', 
                grammatical_person = 'first_person_singular', 
                vocabulary_type = 'technical', 
                business = 'We are a travel site that helps customers find the best hotels and flights.', 
                company_branding = 'ACME Inc. should never be translated.', 
                formatting = 'Never use capital letters', 
                glossary_terms = 'Appartement, cabin, loft', 
                grammar_consistency = '0', 
                literal_translation = 'Neutral', 
                overall_tone = 'Tone should be fun and light', 
                samples = 'http://www.myexample.com/my/document/path/to/samples.pdf'
            )
        else :
            return StyleguideCreateParameters(
        )

    def testStyleguideCreateParameters(self):
        """Test StyleguideCreateParameters"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

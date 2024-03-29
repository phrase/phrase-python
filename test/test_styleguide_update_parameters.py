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
from phrase_api.models.styleguide_update_parameters import StyleguideUpdateParameters  # noqa: E501
from phrase_api.rest import ApiException

class TestStyleguideUpdateParameters(unittest.TestCase):
    """StyleguideUpdateParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StyleguideUpdateParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.styleguide_update_parameters.StyleguideUpdateParameters()  # noqa: E501

        """
        if include_optional :
            return StyleguideUpdateParameters(
                title = 'Web application style guide', 
                audience = 'customer-facing', 
                target_audience = 'teenager', 
                grammatical_person = 'first_person_singular', 
                vocabulary_type = 'technical', 
                business = 'We are a travel site that helps customers find the best hotels and flights.', 
                company_branding = 'ACME Inc. should never be translated.', 
                formatting = 'Never use capital letters', 
                glossary_terms = 'Apartment, cabin, loft', 
                grammar_consistency = '', 
                literal_translation = 'Neutral', 
                overall_tone = 'Tone should be fun and light', 
                samples = 'http://www.myexample.com/my/document/path/to/samples.pdf'
            )
        else :
            return StyleguideUpdateParameters(
        )
        """

    def testStyleguideUpdateParameters(self):
        """Test StyleguideUpdateParameters"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

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
from phrase_api.models.keys_tag_parameters import KeysTagParameters  # noqa: E501
from phrase_api.rest import ApiException

class TestKeysTagParameters(unittest.TestCase):
    """KeysTagParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test KeysTagParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.keys_tag_parameters.KeysTagParameters()  # noqa: E501

        """
        if include_optional :
            return KeysTagParameters(
                branch = 'my-feature-branch', 
                q = 'mykey* translated:true', 
                locale_id = 'abcd1234abcd1234abcd1234abcd1234', 
                tags = 'landing-page,release-1.2'
            )
        else :
            return KeysTagParameters(
        )
        """

    def testKeysTagParameters(self):
        """Test KeysTagParameters"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

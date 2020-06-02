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
from phrase-api.models.keys_search_parameters import KeysSearchParameters  # noqa: E501
from phrase-api.rest import ApiException

class TestKeysSearchParameters(unittest.TestCase):
    """KeysSearchParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test KeysSearchParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase-api.models.keys_search_parameters.KeysSearchParameters()  # noqa: E501
        if include_optional :
            return KeysSearchParameters(
                branch = 'my-feature-branch', 
                sort = 'updated_at', 
                order = 'desc', 
                q = 'mykey* translated:true', 
                locale_id = 'abcd1234abcd1234abcd1234abcd1234'
            )
        else :
            return KeysSearchParameters(
        )

    def testKeysSearchParameters(self):
        """Test KeysSearchParameters"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

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
from phrase_api.models.key_links_create_parameters import KeyLinksCreateParameters  # noqa: E501
from phrase_api.rest import ApiException

class TestKeyLinksCreateParameters(unittest.TestCase):
    """KeyLinksCreateParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test KeyLinksCreateParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.key_links_create_parameters.KeyLinksCreateParameters()  # noqa: E501

        """
        if include_optional :
            return KeyLinksCreateParameters(
                child_key_ids = ["child_key_id1","child_key_id2"]
            )
        else :
            return KeyLinksCreateParameters(
                child_key_ids = ["child_key_id1","child_key_id2"],
        )
        """

    def testKeyLinksCreateParameters(self):
        """Test KeyLinksCreateParameters"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

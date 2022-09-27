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
from phrase_api.models.account_details1 import AccountDetails1  # noqa: E501
from phrase_api.rest import ApiException

class TestAccountDetails1(unittest.TestCase):
    """AccountDetails1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AccountDetails1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.account_details1.AccountDetails1()  # noqa: E501
        if include_optional :
            return AccountDetails1(
                subscription = {"is_current":true,"trial_expired":false}, 
                slug = '0'
            )
        else :
            return AccountDetails1(
        )

    def testAccountDetails1(self):
        """Test AccountDetails1"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

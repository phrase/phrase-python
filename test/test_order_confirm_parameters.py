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
from phrase-api.models.order_confirm_parameters import OrderConfirmParameters  # noqa: E501
from phrase-api.rest import ApiException

class TestOrderConfirmParameters(unittest.TestCase):
    """OrderConfirmParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OrderConfirmParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase-api.models.order_confirm_parameters.OrderConfirmParameters()  # noqa: E501
        if include_optional :
            return OrderConfirmParameters(
                branch = 'my-feature-branch'
            )
        else :
            return OrderConfirmParameters(
        )

    def testOrderConfirmParameters(self):
        """Test OrderConfirmParameters"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

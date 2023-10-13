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
from phrase_api.models.screenshot_marker_create_parameters import ScreenshotMarkerCreateParameters  # noqa: E501
from phrase_api.rest import ApiException

class TestScreenshotMarkerCreateParameters(unittest.TestCase):
    """ScreenshotMarkerCreateParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ScreenshotMarkerCreateParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.screenshot_marker_create_parameters.ScreenshotMarkerCreateParameters()  # noqa: E501

        """
        if include_optional :
            return ScreenshotMarkerCreateParameters(
                branch = 'my-feature-branch', 
                key_id = 'abcd1234abcd1234abcd1234abcd1234', 
                presentation = '{ "x": 100, "y": 100, "w": 100, "h": 100 }'
            )
        else :
            return ScreenshotMarkerCreateParameters(
        )
        """

    def testScreenshotMarkerCreateParameters(self):
        """Test ScreenshotMarkerCreateParameters"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

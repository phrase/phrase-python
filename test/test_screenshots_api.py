# coding: utf-8

"""
    Phrase API Reference

    The version of the OpenAPI document: 2.0.0
    Contact: support@phrase.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import phrase_api
from phrase_api.api.screenshots_api import ScreenshotsApi  # noqa: E501
from phrase_api.rest import ApiException


class TestScreenshotsApi(unittest.TestCase):
    """ScreenshotsApi unit test stubs"""

    def setUp(self):
        self.api = phrase_api.api.screenshots_api.ScreenshotsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_screenshot_create(self):
        """Test case for screenshot_create

        Create a screenshot  # noqa: E501
        """
        pass

    def test_screenshot_delete(self):
        """Test case for screenshot_delete

        Delete a screenshot  # noqa: E501
        """
        pass

    def test_screenshot_show(self):
        """Test case for screenshot_show

        Get a single screenshot  # noqa: E501
        """
        pass

    def test_screenshot_update(self):
        """Test case for screenshot_update

        Update a screenshot  # noqa: E501
        """
        pass

    def test_screenshots_list(self):
        """Test case for screenshots_list

        List screenshots  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

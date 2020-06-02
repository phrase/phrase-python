# coding: utf-8

"""
    Phrase API Reference

    The version of the OpenAPI document: 2.0.0
    Contact: support@phrase.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import phrase-api
from phrase-api.api.tags_api import TagsApi  # noqa: E501
from phrase-api.rest import ApiException


class TestTagsApi(unittest.TestCase):
    """TagsApi unit test stubs"""

    def setUp(self):
        self.api = phrase-api.api.tags_api.TagsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_tag_create(self):
        """Test case for tag_create

        Create a tag  # noqa: E501
        """
        pass

    def test_tag_delete(self):
        """Test case for tag_delete

        Delete a tag  # noqa: E501
        """
        pass

    def test_tag_show(self):
        """Test case for tag_show

        Get a single tag  # noqa: E501
        """
        pass

    def test_tags_list(self):
        """Test case for tags_list

        List tags  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

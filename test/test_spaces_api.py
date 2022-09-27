# coding: utf-8

"""
    Phrase Strings API Reference

    The version of the OpenAPI document: 2.0.0
    Contact: support@phrase.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import phrase_api
from phrase_api.api.spaces_api import SpacesApi  # noqa: E501
from phrase_api.rest import ApiException


class TestSpacesApi(unittest.TestCase):
    """SpacesApi unit test stubs"""

    def setUp(self):
        self.api = phrase_api.api.spaces_api.SpacesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_space_create(self):
        """Test case for space_create

        Create a Space  # noqa: E501
        """
        pass

    def test_space_delete(self):
        """Test case for space_delete

        Delete Space  # noqa: E501
        """
        pass

    def test_space_show(self):
        """Test case for space_show

        Get Space  # noqa: E501
        """
        pass

    def test_space_update(self):
        """Test case for space_update

        Update Space  # noqa: E501
        """
        pass

    def test_spaces_list(self):
        """Test case for spaces_list

        List Spaces  # noqa: E501
        """
        pass

    def test_spaces_projects_create(self):
        """Test case for spaces_projects_create

        Add Project  # noqa: E501
        """
        pass

    def test_spaces_projects_delete(self):
        """Test case for spaces_projects_delete

        Remove Project  # noqa: E501
        """
        pass

    def test_spaces_projects_list(self):
        """Test case for spaces_projects_list

        List Projects  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

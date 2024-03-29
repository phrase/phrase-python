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
from phrase_api.api.branches_api import BranchesApi  # noqa: E501
from phrase_api.rest import ApiException


class TestBranchesApi(unittest.TestCase):
    """BranchesApi unit test stubs"""

    def setUp(self):
        self.api = phrase_api.api.branches_api.BranchesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_branch_compare(self):
        """Test case for branch_compare

        Compare branches  # noqa: E501
        """
        pass

    def test_branch_create(self):
        """Test case for branch_create

        Create a branch  # noqa: E501
        """
        pass

    def test_branch_delete(self):
        """Test case for branch_delete

        Delete a branch  # noqa: E501
        """
        pass

    def test_branch_merge(self):
        """Test case for branch_merge

        Merge a branch  # noqa: E501
        """
        pass

    def test_branch_show(self):
        """Test case for branch_show

        Get a single branch  # noqa: E501
        """
        pass

    def test_branch_update(self):
        """Test case for branch_update

        Update a branch  # noqa: E501
        """
        pass

    def test_branches_list(self):
        """Test case for branches_list

        List branches  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

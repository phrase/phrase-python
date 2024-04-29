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
from phrase_api.api.repo_syncs_api import RepoSyncsApi  # noqa: E501
from phrase_api.rest import ApiException


class TestRepoSyncsApi(unittest.TestCase):
    """RepoSyncsApi unit test stubs"""

    def setUp(self):
        self.api = phrase_api.api.repo_syncs_api.RepoSyncsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_repo_sync_activate(self):
        """Test case for repo_sync_activate

        Activate a Repo Sync  # noqa: E501
        """
        pass

    def test_repo_sync_deactivate(self):
        """Test case for repo_sync_deactivate

        Deactivate a Repo Sync  # noqa: E501
        """
        pass

    def test_repo_sync_events(self):
        """Test case for repo_sync_events

        Repository Syncs History  # noqa: E501
        """
        pass

    def test_repo_sync_export(self):
        """Test case for repo_sync_export

        Export to code repository  # noqa: E501
        """
        pass

    def test_repo_sync_import(self):
        """Test case for repo_sync_import

        Import from code repository  # noqa: E501
        """
        pass

    def test_repo_sync_list(self):
        """Test case for repo_sync_list

        Get Repo Syncs  # noqa: E501
        """
        pass

    def test_repo_sync_show(self):
        """Test case for repo_sync_show

        Get a single Repo Sync  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
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
from phrase_api.api.repo_sync_events_api import RepoSyncEventsApi  # noqa: E501
from phrase_api.rest import ApiException


class TestRepoSyncEventsApi(unittest.TestCase):
    """RepoSyncEventsApi unit test stubs"""

    def setUp(self):
        self.api = phrase_api.api.repo_sync_events_api.RepoSyncEventsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_repo_sync_event_list(self):
        """Test case for repo_sync_event_list

        Repository Syncs History  # noqa: E501
        """
        pass

    def test_repo_sync_event_show(self):
        """Test case for repo_sync_event_show

        Get a single Repo Sync Event  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

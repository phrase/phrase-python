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
from phrase_api.api.notification_groups_api import NotificationGroupsApi  # noqa: E501
from phrase_api.rest import ApiException


class TestNotificationGroupsApi(unittest.TestCase):
    """NotificationGroupsApi unit test stubs"""

    def setUp(self):
        self.api = phrase_api.api.notification_groups_api.NotificationGroupsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_notification_groups_list(self):
        """Test case for notification_groups_list

        List notification groups  # noqa: E501
        """
        pass

    def test_notification_groups_mark_all_as_read(self):
        """Test case for notification_groups_mark_all_as_read

        Mark all notification groups as read  # noqa: E501
        """
        pass

    def test_notification_groups_mark_as_read(self):
        """Test case for notification_groups_mark_as_read

        Mark a notification group as read  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

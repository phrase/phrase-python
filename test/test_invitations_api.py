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
from phrase_api.api.invitations_api import InvitationsApi  # noqa: E501
from phrase_api.rest import ApiException


class TestInvitationsApi(unittest.TestCase):
    """InvitationsApi unit test stubs"""

    def setUp(self):
        self.api = phrase_api.api.invitations_api.InvitationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_invitation_create(self):
        """Test case for invitation_create

        Create a new invitation  # noqa: E501
        """
        pass

    def test_invitation_delete(self):
        """Test case for invitation_delete

        Delete an invitation  # noqa: E501
        """
        pass

    def test_invitation_resend(self):
        """Test case for invitation_resend

        Resend an invitation  # noqa: E501
        """
        pass

    def test_invitation_show(self):
        """Test case for invitation_show

        Get a single invitation  # noqa: E501
        """
        pass

    def test_invitation_update(self):
        """Test case for invitation_update

        Update an invitation  # noqa: E501
        """
        pass

    def test_invitation_update_settings(self):
        """Test case for invitation_update_settings

        Update a member's invitation access  # noqa: E501
        """
        pass

    def test_invitations_list(self):
        """Test case for invitations_list

        List invitations  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

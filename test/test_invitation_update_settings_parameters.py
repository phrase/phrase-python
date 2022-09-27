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
from phrase_api.models.invitation_update_settings_parameters import InvitationUpdateSettingsParameters  # noqa: E501
from phrase_api.rest import ApiException

class TestInvitationUpdateSettingsParameters(unittest.TestCase):
    """InvitationUpdateSettingsParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InvitationUpdateSettingsParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.invitation_update_settings_parameters.InvitationUpdateSettingsParameters()  # noqa: E501
        if include_optional :
            return InvitationUpdateSettingsParameters(
                project_role = 'Developer', 
                locale_ids = ["abcd1234abcd1234abcd1234","abcd1234abcd1234abcd1235"]
            )
        else :
            return InvitationUpdateSettingsParameters(
        )

    def testInvitationUpdateSettingsParameters(self):
        """Test InvitationUpdateSettingsParameters"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

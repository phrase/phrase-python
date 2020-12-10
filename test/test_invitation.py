# coding: utf-8

"""
    Phrase API Reference

    The version of the OpenAPI document: 2.0.0
    Contact: support@phrase.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import phrase_api
from phrase_api.models.invitation import Invitation  # noqa: E501
from phrase_api.rest import ApiException

class TestInvitation(unittest.TestCase):
    """Invitation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Invitation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.invitation.Invitation()  # noqa: E501
        if include_optional :
            return Invitation(
                id = '0', 
                email = '0', 
                role = '0', 
                state = '0', 
                projects = [
                    {"id":"abcd1234cdef1234abcd1234cdef1234","name":"My Android Project","main_format":"xml","created_at":"2015-01-28T09:52:53Z","updated_at":"2015-01-28T09:52:53Z"}
                    ], 
                locales = [
                    {"id":"abcd1234cdef1234abcd1234cdef1234","name":"English","code":"en-GB"}
                    ], 
                default_locale_codes = [
                    '0'
                    ], 
                permissions = None, 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                accepted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                spaces = [
                    phrase_api.models.member_spaces.member_spaces(
                        id = '0', 
                        name = '0', 
                        created_at = null, 
                        updated_at = null, 
                        projects_count = 56, )
                    ]
            )
        else :
            return Invitation(
        )

    def testInvitation(self):
        """Test Invitation"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

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
from phrase_api.models.comment import Comment  # noqa: E501
from phrase_api.rest import ApiException

class TestComment(unittest.TestCase):
    """Comment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Comment
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.comment.Comment()  # noqa: E501

        """
        if include_optional :
            return Comment(
                id = '0', 
                message = '0', 
                has_replies = True, 
                user = phrase_api.models.user_preview.user_preview(
                    id = '0', 
                    username = '0', 
                    name = '0', 
                    gravatar_uid = '0', ), 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                mentioned_users = [
                    phrase_api.models.user_preview.user_preview(
                        id = '0', 
                        username = '0', 
                        name = '0', 
                        gravatar_uid = '0', )
                    ], 
                locales = [
                    {"id":"abcd1234cdef1234abcd1234cdef1234","name":"English","code":"en-GB"}
                    ]
            )
        else :
            return Comment(
        )
        """

    def testComment(self):
        """Test Comment"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

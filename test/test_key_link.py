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
from phrase_api.models.key_link import KeyLink  # noqa: E501
from phrase_api.rest import ApiException

class TestKeyLink(unittest.TestCase):
    """KeyLink unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test KeyLink
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.key_link.KeyLink()  # noqa: E501

        """
        if include_optional :
            return KeyLink(
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                created_by = phrase_api.models.user_preview.user_preview(
                    id = '', 
                    username = '', 
                    name = '', 
                    gravatar_uid = '', ), 
                updated_by = phrase_api.models.user_preview.user_preview(
                    id = '', 
                    username = '', 
                    name = '', 
                    gravatar_uid = '', ), 
                account = {"id":"abcd1234","name":"Company Account","slug":"company_account","company":"My Awesome Company","created_at":"2015-01-28T09:52:53Z","updated_at":"2015-01-28T09:52:53Z","company_logo_url":"http://assets.example.com/company_logo.png"}, 
                parent = phrase_api.models.key_preview.key_preview(
                    id = '', 
                    name = '', 
                    plural = True, 
                    use_ordinal_rules = True, ), 
                children = [
                    phrase_api.models.key_preview.key_preview(
                        id = '', 
                        name = '', 
                        plural = True, 
                        use_ordinal_rules = True, )
                    ]
            )
        else :
            return KeyLink(
        )
        """

    def testKeyLink(self):
        """Test KeyLink"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

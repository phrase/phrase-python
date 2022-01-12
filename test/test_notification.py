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
from phrase_api.models.notification import Notification  # noqa: E501
from phrase_api.rest import ApiException

class TestNotification(unittest.TestCase):
    """Notification unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Notification
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.notification.Notification()  # noqa: E501
        if include_optional :
            return Notification(
                id = '0', 
                event_name = '0', 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                delivered_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                seen_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                data = None, 
                resource = None, 
                locale = {"id":"abcd1234cdef1234abcd1234cdef1234","name":"de","code":"de-DE","default":true,"main":false,"rtl":false,"plural_forms":["zero","one","other"],"source_locale":{"id":"abcd1234cdef1234abcd1234cdef1234","name":"en","code":"en-GB"},"created_at":"2015-01-28T09:52:53Z","updated_at":"2015-01-28T09:52:53Z"}, 
                user = phrase_api.models.user_preview.user_preview(
                    id = '0', 
                    username = '0', 
                    name = '0', 
                    gravatar_uid = '0', ), 
                project = {"id":"abcd1234cdef1234abcd1234cdef1234","name":"My Android Project","slug":"android_project","main_format":"xml","project_image_url":"http://assets.example.com/project.png","account":"account","space":"space","created_at":"2015-01-28T09:52:53Z","updated_at":"2015-01-28T09:52:53Z"}, 
                account = {"id":"abcd1234","name":"Company Account","slug":"company_account","company":"My Awesome Company","created_at":"2015-01-28T09:52:53Z","updated_at":"2015-01-28T09:52:53Z","company_logo_url":"http://assets.example.com/company_logo.png"}, 
                group = {"id":"abcd1234cdef1234abcd1234cdef1234","event_name":"keys:create","created_at":"2015-01-28T09:52:53Z","updated_at":"2015-01-28T09:52:53Z"}
            )
        else :
            return Notification(
        )

    def testNotification(self):
        """Test Notification"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

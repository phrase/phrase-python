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
from phrase_api.models.release import Release  # noqa: E501
from phrase_api.rest import ApiException

class TestRelease(unittest.TestCase):
    """Release unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Release
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.release.Release()  # noqa: E501

        """
        if include_optional :
            return Release(
                id = '', 
                version = 56, 
                app_min_version = '', 
                app_max_version = '', 
                description = '', 
                platforms = [
                    ''
                    ], 
                environments = [
                    ''
                    ], 
                locales = [
                    {"id":"abcd1234cdef1234abcd1234cdef1234","name":"English","code":"en-GB"}
                    ], 
                tags = [
                    ''
                    ], 
                project = {"id":"abcd1234cdef1234abcd1234cdef1234","name":"My Android Project","main_format":"xml","created_at":"2015-01-28T09:52:53Z","updated_at":"2015-01-28T09:52:53Z"}, 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return Release(
        )
        """

    def testRelease(self):
        """Test Release"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

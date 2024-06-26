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
from phrase_api.models.release_trigger import ReleaseTrigger  # noqa: E501
from phrase_api.rest import ApiException

class TestReleaseTrigger(unittest.TestCase):
    """ReleaseTrigger unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ReleaseTrigger
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.release_trigger.ReleaseTrigger()  # noqa: E501

        """
        if include_optional :
            return ReleaseTrigger(
                id = '', 
                branch = '', 
                cron_schedule = '', 
                time_zone = '', 
                next_run_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                app_min_version = '', 
                app_max_version = '', 
                locales = [
                    {"id":"abcd1234cdef1234abcd1234cdef1234","name":"English","code":"en-GB"}
                    ], 
                tags = [
                    ''
                    ], 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return ReleaseTrigger(
        )
        """

    def testReleaseTrigger(self):
        """Test ReleaseTrigger"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

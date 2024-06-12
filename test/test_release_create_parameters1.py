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
from phrase_api.models.release_create_parameters1 import ReleaseCreateParameters1  # noqa: E501
from phrase_api.rest import ApiException

class TestReleaseCreateParameters1(unittest.TestCase):
    """ReleaseCreateParameters1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ReleaseCreateParameters1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.release_create_parameters1.ReleaseCreateParameters1()  # noqa: E501

        """
        if include_optional :
            return ReleaseCreateParameters1(
                cron_schedule = '15 18 * * 1,3', 
                time_zone = 'Europe/Berlin', 
                locale_ids = ["abcd1234cdef1234abcd1234cdef1234","fff565db236400772368235db2c6117e"], 
                tags = ["android","feature1"], 
                branch = 'my-feature-branch', 
                app_min_version = '1.0.0', 
                app_max_version = '2.0.0'
            )
        else :
            return ReleaseCreateParameters1(
        )
        """

    def testReleaseCreateParameters1(self):
        """Test ReleaseCreateParameters1"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

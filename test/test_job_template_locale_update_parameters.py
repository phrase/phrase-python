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
from phrase_api.models.job_template_locale_update_parameters import JobTemplateLocaleUpdateParameters  # noqa: E501
from phrase_api.rest import ApiException

class TestJobTemplateLocaleUpdateParameters(unittest.TestCase):
    """JobTemplateLocaleUpdateParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test JobTemplateLocaleUpdateParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.job_template_locale_update_parameters.JobTemplateLocaleUpdateParameters()  # noqa: E501
        if include_optional :
            return JobTemplateLocaleUpdateParameters(
                branch = 'my-feature-branch', 
                locale_id = 'abcd1234cdef1234abcd1234cdef1234', 
                user_ids = ["abcd1234cdef1234abcd1234cdef1234"], 
                reviewer_ids = ["abcd1234cdef1234abcd1234cdef1234"], 
                translator_team_ids = ["abcd1234cdef1234abcd1234cdef1234"], 
                reviewer_team_ids = ["abcd1234cdef1234abcd1234cdef1234"]
            )
        else :
            return JobTemplateLocaleUpdateParameters(
        )

    def testJobTemplateLocaleUpdateParameters(self):
        """Test JobTemplateLocaleUpdateParameters"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

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

import phrase-api
from phrase-api.models.project_create_parameters import ProjectCreateParameters  # noqa: E501
from phrase-api.rest import ApiException

class TestProjectCreateParameters(unittest.TestCase):
    """ProjectCreateParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProjectCreateParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase-api.models.project_create_parameters.ProjectCreateParameters()  # noqa: E501
        if include_optional :
            return ProjectCreateParameters(
                name = 'My Android Project', 
                main_format = 'yml', 
                shares_translation_memory = True, 
                project_image = bytes(b'blah'), 
                remove_project_image = True, 
                account_id = 'abcd1234'
            )
        else :
            return ProjectCreateParameters(
        )

    def testProjectCreateParameters(self):
        """Test ProjectCreateParameters"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

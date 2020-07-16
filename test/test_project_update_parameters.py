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
from phrase_api.models.project_update_parameters import ProjectUpdateParameters  # noqa: E501
from phrase_api.rest import ApiException

class TestProjectUpdateParameters(unittest.TestCase):
    """ProjectUpdateParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProjectUpdateParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.project_update_parameters.ProjectUpdateParameters()  # noqa: E501
        if include_optional :
            return ProjectUpdateParameters(
                name = 'My Android Project', 
                main_format = 'yml', 
                shares_translation_memory = True, 
                project_image = bytes(b'blah'), 
                remove_project_image = True, 
                account_id = 'abcd1234'
            )
        else :
            return ProjectUpdateParameters(
        )

    def testProjectUpdateParameters(self):
        """Test ProjectUpdateParameters"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

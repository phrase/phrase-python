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
from phrase_api.models.project_details import ProjectDetails  # noqa: E501
from phrase_api.rest import ApiException

class TestProjectDetails(unittest.TestCase):
    """ProjectDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProjectDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.project_details.ProjectDetails()  # noqa: E501
        if include_optional :
            return ProjectDetails(
                id = '0', 
                name = '0', 
                main_format = '0', 
                project_image_url = '0', 
                account = {"id":"abcd1234","name":"Company Account","company":"My Awesome Company","created_at":"2015-01-28T09:52:53Z","updated_at":"2015-01-28T09:52:53Z"}, 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                slug = '0', 
                shares_translation_memory = True
            )
        else :
            return ProjectDetails(
        )

    def testProjectDetails(self):
        """Test ProjectDetails"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

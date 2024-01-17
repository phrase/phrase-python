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
from phrase_api.models.projects_quality_performance_score_request import ProjectsQualityPerformanceScoreRequest  # noqa: E501
from phrase_api.rest import ApiException

class TestProjectsQualityPerformanceScoreRequest(unittest.TestCase):
    """ProjectsQualityPerformanceScoreRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProjectsQualityPerformanceScoreRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.projects_quality_performance_score_request.ProjectsQualityPerformanceScoreRequest()  # noqa: E501

        """
        if include_optional :
            return ProjectsQualityPerformanceScoreRequest(
                translation_ids = [
                    'translation_id_1'
                    ]
            )
        else :
            return ProjectsQualityPerformanceScoreRequest(
        )
        """

    def testProjectsQualityPerformanceScoreRequest(self):
        """Test ProjectsQualityPerformanceScoreRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

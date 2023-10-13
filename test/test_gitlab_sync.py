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
from phrase_api.models.gitlab_sync import GitlabSync  # noqa: E501
from phrase_api.rest import ApiException

class TestGitlabSync(unittest.TestCase):
    """GitlabSync unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GitlabSync
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.gitlab_sync.GitlabSync()  # noqa: E501

        """
        if include_optional :
            return GitlabSync(
                id = '0', 
                project_id = '0', 
                gitlab_project_id = 56, 
                gitlab_branch_name = '0', 
                auto_import = True, 
                auto_import_secret = '0', 
                auto_import_url = '0', 
                self_hosted_api_url = '0', 
                last_exported_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                last_imported_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                last_status = '0'
            )
        else :
            return GitlabSync(
        )
        """

    def testGitlabSync(self):
        """Test GitlabSync"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

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
from phrase_api.models.account_search_result import AccountSearchResult  # noqa: E501
from phrase_api.rest import ApiException

class TestAccountSearchResult(unittest.TestCase):
    """AccountSearchResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AccountSearchResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.account_search_result.AccountSearchResult()  # noqa: E501

        """
        if include_optional :
            return AccountSearchResult(
                query = '', 
                excerpt = '', 
                key = phrase_api.models.key_preview.key_preview(
                    id = '', 
                    name = '', 
                    plural = True, 
                    use_ordinal_rules = True, ), 
                locale = {"id":"abcd1234cdef1234abcd1234cdef1234","name":"English","code":"en-GB"}, 
                project = {"id":"abcd1234cdef1234abcd1234cdef1234","name":"My Android Project","slug":"android_project","main_format":"xml","project_image_url":"http://assets.example.com/project.png","account":"account","space":"space","created_at":"2015-01-28T09:52:53Z","updated_at":"2015-01-28T09:52:53Z"}, 
                translation = {"id":"abcd1234cdef1234abcd1234cdef1234","content":"My translation","unverified":false,"excluded":false,"plural_suffix":"","key":{"id":"abcd1234cdef1234abcd1234cdef1234","name":"home.index.headline","plural":false,"use_ordinal_rules":false},"locale":{"id":"abcd1234cdef1234abcd1234cdef1234","name":"de","code":"de-DE"},"placeholders":["%{count}"],"state":"translated","created_at":"2015-01-28T09:52:53Z","updated_at":"2015-01-28T09:52:53Z"}, 
                other_translations = [
                    {"id":"abcd1234cdef1234abcd1234cdef1234","content":"My translation","unverified":false,"excluded":false,"plural_suffix":"","key":{"id":"abcd1234cdef1234abcd1234cdef1234","name":"home.index.headline","plural":false,"use_ordinal_rules":false},"locale":{"id":"abcd1234cdef1234abcd1234cdef1234","name":"de","code":"de-DE"},"placeholders":["%{count}"],"state":"translated","created_at":"2015-01-28T09:52:53Z","updated_at":"2015-01-28T09:52:53Z"}
                    ]
            )
        else :
            return AccountSearchResult(
        )
        """

    def testAccountSearchResult(self):
        """Test AccountSearchResult"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

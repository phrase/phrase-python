# coding: utf-8

"""
    Phrase Strings API Reference

    The version of the OpenAPI document: 2.0.0
    Contact: support@phrase.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import phrase_api
from phrase_api.api.job_comments_api import JobCommentsApi  # noqa: E501
from phrase_api.rest import ApiException


class TestJobCommentsApi(unittest.TestCase):
    """JobCommentsApi unit test stubs"""

    def setUp(self):
        self.api = phrase_api.api.job_comments_api.JobCommentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_job_comment_create(self):
        """Test case for job_comment_create

        Create a job comment  # noqa: E501
        """
        pass

    def test_job_comment_delete(self):
        """Test case for job_comment_delete

        Delete a job comment  # noqa: E501
        """
        pass

    def test_job_comment_show(self):
        """Test case for job_comment_show

        Get a single job comment  # noqa: E501
        """
        pass

    def test_job_comment_update(self):
        """Test case for job_comment_update

        Update a job comment  # noqa: E501
        """
        pass

    def test_job_comments_list(self):
        """Test case for job_comments_list

        List job comments  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

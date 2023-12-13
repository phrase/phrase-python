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
from phrase_api.api.comment_reactions_api import CommentReactionsApi  # noqa: E501
from phrase_api.rest import ApiException


class TestCommentReactionsApi(unittest.TestCase):
    """CommentReactionsApi unit test stubs"""

    def setUp(self):
        self.api = phrase_api.api.comment_reactions_api.CommentReactionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_reaction_create(self):
        """Test case for reaction_create

        Create a reaction  # noqa: E501
        """
        pass

    def test_reaction_delete(self):
        """Test case for reaction_delete

        Delete a reaction  # noqa: E501
        """
        pass

    def test_reaction_show(self):
        """Test case for reaction_show

        Get a single reaction  # noqa: E501
        """
        pass

    def test_reactions_list(self):
        """Test case for reactions_list

        List reactions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
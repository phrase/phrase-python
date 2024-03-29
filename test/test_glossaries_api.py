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
from phrase_api.api.glossaries_api import GlossariesApi  # noqa: E501
from phrase_api.rest import ApiException


class TestGlossariesApi(unittest.TestCase):
    """GlossariesApi unit test stubs"""

    def setUp(self):
        self.api = phrase_api.api.glossaries_api.GlossariesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_glossaries_list(self):
        """Test case for glossaries_list

        List term bases  # noqa: E501
        """
        pass

    def test_glossary_create(self):
        """Test case for glossary_create

        Create a term base  # noqa: E501
        """
        pass

    def test_glossary_delete(self):
        """Test case for glossary_delete

        Delete a term base  # noqa: E501
        """
        pass

    def test_glossary_show(self):
        """Test case for glossary_show

        Get a single term base  # noqa: E501
        """
        pass

    def test_glossary_update(self):
        """Test case for glossary_update

        Update a term base  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

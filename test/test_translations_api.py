# coding: utf-8

"""
    Phrase API Reference

    The version of the OpenAPI document: 2.0.0
    Contact: support@phrase.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import phrase_api
from phrase_api.api.translations_api import TranslationsApi  # noqa: E501
from phrase_api.rest import ApiException


class TestTranslationsApi(unittest.TestCase):
    """TranslationsApi unit test stubs"""

    def setUp(self):
        self.api = phrase_api.api.translations_api.TranslationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_translation_create(self):
        """Test case for translation_create

        Create a translation  # noqa: E501
        """
        pass

    def test_translation_exclude(self):
        """Test case for translation_exclude

        Exclude a translation from export  # noqa: E501
        """
        pass

    def test_translation_include(self):
        """Test case for translation_include

        Revoke exclusion of a translation in export  # noqa: E501
        """
        pass

    def test_translation_review(self):
        """Test case for translation_review

        Review a translation  # noqa: E501
        """
        pass

    def test_translation_show(self):
        """Test case for translation_show

        Get a single translation  # noqa: E501
        """
        pass

    def test_translation_unverify(self):
        """Test case for translation_unverify

        Mark a translation as unverified  # noqa: E501
        """
        pass

    def test_translation_update(self):
        """Test case for translation_update

        Update a translation  # noqa: E501
        """
        pass

    def test_translation_verify(self):
        """Test case for translation_verify

        Verify a translation  # noqa: E501
        """
        pass

    def test_translations_by_key(self):
        """Test case for translations_by_key

        List translations by key  # noqa: E501
        """
        pass

    def test_translations_by_locale(self):
        """Test case for translations_by_locale

        List translations by locale  # noqa: E501
        """
        pass

    def test_translations_exclude_collection(self):
        """Test case for translations_exclude_collection

        Set exclude from export flag on translations selected by query  # noqa: E501
        """
        pass

    def test_translations_include_collection(self):
        """Test case for translations_include_collection

        Remove exlude from import flag from translations selected by query  # noqa: E501
        """
        pass

    def test_translations_list(self):
        """Test case for translations_list

        List all translations  # noqa: E501
        """
        pass

    def test_translations_review_collection(self):
        """Test case for translations_review_collection

        Review translations selected by query  # noqa: E501
        """
        pass

    def test_translations_search(self):
        """Test case for translations_search

        Search translations  # noqa: E501
        """
        pass

    def test_translations_unverify_collection(self):
        """Test case for translations_unverify_collection

        Mark translations selected by query as unverified  # noqa: E501
        """
        pass

    def test_translations_verify_collection(self):
        """Test case for translations_verify_collection

        Verify translations selected by query  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

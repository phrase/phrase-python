# coding: utf-8

"""
    Phrase Strings API Reference

    The version of the OpenAPI document: 2.0.0
    Contact: support@phrase.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
from unittest.mock import Mock, patch

import phrase_api
from phrase_api.api.uploads_api import UploadsApi  # noqa: E501
from phrase_api.rest import ApiException


class TestUploadsApi(unittest.TestCase):
    """UploadsApi unit test stubs"""

    def setUp(self):
        self.configuration = phrase_api.Configuration()
        self.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
        self.configuration.api_key_prefix['Authorization'] = 'token'

    def tearDown(self):
        pass

    @patch('urllib3.PoolManager.urlopen')
    def test_upload_create(self, mock_post):
        """Test case for upload_create

        Upload a new file  # noqa: E501
        """
        mock_post.return_value = Mock(ok=True)
        mock_post.return_value.data = '{"id": "upload_id", "format": "simple_json"}'.encode()
        mock_post.return_value.getencoding.return_value = 'utf-8'
        mock_post.return_value.status = 201
        mock_post.return_value.getheader.side_effect = { 'Content-Type': "application/json" }.get

        project_id = "project_id_example"
        with phrase_api.ApiClient(self.configuration) as api_client:
            api_instance = phrase_api.UploadsApi(api_client)
            api_response = api_instance.upload_create(
                project_id,
                file="./test/fixtures/en.json",
                file_format="simple_json",
                locale_id="en"
            )

            self.assertEqual("https://api.phrase.com/v2/projects/project_id_example/uploads", mock_post.call_args_list[0].args[1])

            self.assertIsNotNone(api_response)
            self.assertIsInstance(api_response, phrase_api.models.upload.Upload)
            self.assertEqual("upload_id", api_response.id)
            self.assertEqual("simple_json", api_response.format)

    def test_upload_show(self):
        """Test case for upload_show

        Get a single upload  # noqa: E501
        """
        pass

    def test_uploads_list(self):
        """Test case for uploads_list

        List uploads  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

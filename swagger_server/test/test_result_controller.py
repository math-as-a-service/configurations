# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestResultController(BaseTestCase):
    """ResultController integration test stubs"""

    def test_get_result(self):
        """Test case for get_result

        Poll for result of an evaluation
        """
        response = self.client.open(
            '/v1/result',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

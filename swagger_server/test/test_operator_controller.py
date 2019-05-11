# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestOperatorController(BaseTestCase):
    """OperatorController integration test stubs"""

    def test_add_operator(self):
        """Test case for add_operator

        Create an operator
        """
        response = self.client.open(
            '/v1/operator',
            method='POST',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_operator(self):
        """Test case for delete_operator

        Delete operator object
        """
        response = self.client.open(
            '/v1/operator/{operator_id}'.format(operator_id=789),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_operator(self):
        """Test case for get_operator

        Retrieve operator object
        """
        response = self.client.open(
            '/v1/operator/{operator_id}'.format(operator_id=789),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_operator(self):
        """Test case for put_operator

        Update operator object
        """
        response = self.client.open(
            '/v1/operator/{operator_id}'.format(operator_id=789),
            method='PUT',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

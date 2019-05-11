# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestExpressionController(BaseTestCase):
    """ExpressionController integration test stubs"""

    def test_add_expression(self):
        """Test case for add_expression

        Create an empty expression
        """
        response = self.client.open(
            '/v1/expression',
            method='POST',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_expression(self):
        """Test case for delete_expression

        Delete expression object
        """
        response = self.client.open(
            '/v1/expression/{expression_id}'.format(expression_id=789),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_expression(self):
        """Test case for get_expression

        Retrieve expression object
        """
        response = self.client.open(
            '/v1/expression/{expression_id}'.format(expression_id=789),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_expression(self):
        """Test case for put_expression

        Update expression object
        """
        response = self.client.open(
            '/v1/expression/{expression_id}'.format(expression_id=789),
            method='PUT',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

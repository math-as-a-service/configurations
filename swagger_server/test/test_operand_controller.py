# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestOperandController(BaseTestCase):
    """OperandController integration test stubs"""

    def test_add_operand(self):
        """Test case for add_operand

        Create an operand
        """
        response = self.client.open(
            '/v1/operand',
            method='POST',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_operand(self):
        """Test case for delete_operand

        Delete operand object
        """
        response = self.client.open(
            '/v1/operand/{operand_id}'.format(operand_id=789),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_operand(self):
        """Test case for get_operand

        Retrieve operand object
        """
        response = self.client.open(
            '/v1/operand/{operand_id}'.format(operand_id=789),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_operand(self):
        """Test case for put_operand

        Update operand object
        """
        response = self.client.open(
            '/v1/operand/{operand_id}'.format(operand_id=789),
            method='PUT',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

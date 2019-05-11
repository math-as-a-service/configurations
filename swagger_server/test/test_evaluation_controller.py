# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestEvaluationController(BaseTestCase):
    """EvaluationController integration test stubs"""

    def test_add_evaluation(self):
        """Test case for add_evaluation

        Begin evaluation of an expression
        """
        response = self.client.open(
            '/v1/evaluation',
            method='POST',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_evaluation(self):
        """Test case for get_evaluation

        Poll for result of an evaluation
        """
        response = self.client.open(
            '/v1/evaluation/{evaluation_id}'.format(evaluation_id=789),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

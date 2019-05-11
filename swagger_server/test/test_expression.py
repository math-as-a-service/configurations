class TestExpression:
    def test_create_and_get_expression(self, client):
        expression_response = client.post('/expression')
        assert expression_response.status_code == 200

        response = client.get('/expression/dne')
        assert response.status_code == 404

        response = client.get('/expression/{}'.format(
            expression_response.json['id'])
        )

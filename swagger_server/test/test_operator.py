class TestOperator:
    def test_add_and_get_operator(self, client):
        response = client.post('/operator')
        assert response.status_code == 400

        response = client.post(
            '/operator',
            json={
                'expression_id': None,
            }
        )
        assert response.status_code == 400

        expression_response = client.post('/expression')
        response = client.post(
            '/operator',
            json={
                'expression_id': expression_response.json['id'],
                'rank': 0,
                'value': '100',
                'type': 4,
            }
        )
        assert response.status_code == 200

        response = client.get('/operator/{}'.format(response.json['operator_id']))
        assert response.status_code == 200
        assert response.json['id'] is not None

    def test_delete_operator(self, client):
        response = client.delete('/operator/dne')
        assert response.status_code == 404

        expression_response = client.post('/expression')
        operator_response = client.post(
            '/operator',
            json={
                'expression_id': expression_response.json['id'],
                'rank': 0,
                'value': '100',
                'type': 4,
            }
        )
        response = client.delete('/operator/{}'.format(
            operator_response.json['operator_id'],
        ))
        assert response.status_code == 200

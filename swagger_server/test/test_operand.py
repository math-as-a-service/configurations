class TestOperand:
    def test_add_and_get_operand(self, client):
        response = client.post('/operand')
        assert response.status_code == 400

        response = client.post(
            '/operand',
            json={
                'expression_id': None,
            }
        )
        assert response.status_code == 400

        expression_response = client.post('/expression')
        response = client.post(
            '/operand',
            json={
                'expression_id': expression_response.json['id'],
                'rank': 0,
                'value': '100',
                'type': 4,
            }
        )
        assert response.status_code == 200

        response = client.get('/operand/{}'.format(response.json['operand_id']))
        assert response.status_code == 200
        assert response.json['id'] is not None

    def test_delete_operand(self, client):
        response = client.delete('/operand/dne')
        assert response.status_code == 404

        expression_response = client.post('/expression')
        operand_response = client.post(
            '/operand',
            json={
                'expression_id': expression_response.json['id'],
                'rank': 0,
                'value': '100',
                'type': 4,
            }
        )
        response = client.delete('/operand/{}'.format(
            operand_response.json['operand_id'],
        ))
        assert response.status_code == 200

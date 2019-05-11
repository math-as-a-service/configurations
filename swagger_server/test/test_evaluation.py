class TestEvaluation:
    def test_get(self, client):
        response = client.get('/evaluation/dne')
        assert response.status_code == 404

    def test_get_and_create(self, client):
        response = client.post(
            '/evaluation',
            json='chonus',
        )

        assert response.status_code == 400

        response = client.post(
            '/evaluation',
            json={
                'expression_id': None,
            },
        )

        assert response.status_code == 400

        expression_response = client.post('/expression')
        response = client.post(
            '/evaluation',
            json={
                'expression_id': expression_response.json['id'],
            },
        )
        assert response.status_code == 200
        assert response.json['evaluation_id'] is not None


from swagger_server.models.result import Result


class TestResult(object):
    def test_get_result(self, client):
        response = client.get('/result/dne')
        assert response.status_code == 404

# class TestEvaluation:
#     def test_get(self, client):
#         response = client.get('/evaluation/dne')
#         assert response.status_code == 404

#     def test_create(self, client):
#         response = client.post(
#             '/evaluation',
#             json='chonus',
#         )

#         assert response.status_code == 400

#         response = client.post(
#             '/evaluation',
#             json={
#                 'expression_id': None,
#             },
#         )

#         assert response.status_code == 400

#         expression_response = client.post('/expression')
#         import pdb
#         pdb.set_trace()
#         print(expression_response.json())
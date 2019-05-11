class TestCombinedRequest:
    def test_entire_workflow(self, client):
        """
        Create an expression
        """
        expression_response = client.post('/expression')
        expression_id = expression_response.json['id']

        """
        Create first operand
        """
        first_operand_response = client.post(
            '/operand',
            json={
                'expression_id': expression_id,
                'rank': 0,
                'value': '1',
                'type': 4,
            }
        )
        first_operand_id = first_operand_response.json['operand_id']

        """
        Create first operator
        """
        first_operator_response = client.post(
            '/operator',
            json={
                'expression_id': expression_id,
                'rank': 1,
                'value': '+',
                'type': 4,
            }
        )
        first_operator_id = first_operator_response.json['operator_id']

        """
        Create second operand
        """
        second_operand_response = client.post(
            '/operand',
            json={
                'expression_id': expression_id,
                'rank': 2,
                'value': '1',
                'type': 4,
            }
        )
        second_operand_id = second_operand_response.json['operand_id']

        evaluation_response = client.post(
            '/evaluation',
            json={
                'expression_id': expression_id,
            },
        )
        evaluation_id = evaluation_response.json['evaluation_id']

        evaluation = client.get('/evaluation/{}'.format(evaluation_id))
        
        result_response = client.get('/result/{}'.format(evaluation.json['result_id']))
        print(result_response.json, result_response.status_code)

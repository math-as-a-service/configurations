from operator import attrgetter

from swagger_server.models.evaluation import Evaluation
from swagger_server.models.operand import Operand
from swagger_server.models.operator import Operator
from swagger_server.models.result import Result

from peewee import *

VALID_OPERATORS = {'+', '-', '/', '*', '**', '%', '//', '<', '>', '<=', '>=', '=='}

class EvaluationService(object):

    def _get_finalized_expression(self, operators, operands):

        # I.e. ['+', '-']
        sorted_operators = sorted(operators, key=attrgetter('rank'))
        # I.e. ['1', '7', '3']
        sorted_operands = sorted(operands, key=attrgetter('rank'))
        final_expression = []
        for index, operand in enumerate(sorted_operands):
            final_expression.append(operand.value)
            if index < len(sorted_operators):
                final_expression.append(sorted_operators[index].value)

        return ' '.join(final_expression)

    def _get_and_validate_arguments_for_expression(self, expression_id):
        operands = Operand.select().where(Operand.expression_id == expression_id).execute()
        operators = Operator.select().where(Operator.expression_id == expression_id).execute()
        operands_valid = self.validate_operands(operands)
        operators_valid = self.validate_operators(operators)
        valid = operands_valid and operators_valid

        return valid, operators, operands

    def get_finalized_expression(self, evaluation_id):
        try:
            evaluation = Evaluation.get_by_id(evaluation_id)
        except DoesNotExist:
            return 'No evaluation found'

        if not evaluation:
            return 'No evaluation found'

        expression_id = evaluation.expression_id
        valid, operators, operands = self._get_and_validate_arguments_for_expression(expression_id)

        if ((len(operators) + 1) != len(operands)) or not valid:
            # Result is just gonna get nothing!
            return 'Invalid evaluation'

        final_expression = self._get_finalized_expression(operators, operands)
        return final_expression


    def evaluate_expression(self, evaluation_id):
        try:
            evaluation = Evaluation.get_by_id(evaluation_id)
        except DoesNotExist:
            return False
        evaluation.status = Evaluation.EVALUATING
        evaluation.save()

        if not evaluation:
            return False

        expression_id = evaluation.expression_id
        result_id = evaluation.result_id

        result = Result.get_by_id(result_id)

        valid, operators, operands = self._get_and_validate_arguments_for_expression(expression_id)

        if ((len(operators) + 1) != len(operands)) or not valid:
            evaluation.status = Evaluation.ERRORED
            evaluation.save()
            # Result is just gonna get nothing!
            return False

        final_expression = self._get_finalized_expression(operators, operands)

        # final_expression should be a list of interleaved operands and operators
        # I.e. ['1', '+', '7', '-', '3']

        result_value = eval(final_expression)
        result.value = result_value
        result.save()
        evaluation.status = Evaluation.FINISHED
        evaluation.save()

        return True


    def validate_operators(self, operators):
        return all([operator.value in VALID_OPERATORS for operator in operators])

    def validate_operands(self, operands):
        for operand in operands:
            try:
                int(operand.value)
            except Exception:
                try:
                    float(operand.value)
                except Exception:
                    return False

        return True
from operator import attrgetter

from swagger_server.models.evaluation import Evaluation
from swagger_server.models.operand import Operand
from swagger_server.models.operator import Operator
from swagger_server.models.result import Result

from peewee import *

VALID_OPERANDS = {'+', '-', '/', '*', '**', '%', '//'}

class EvaluationService(object):

    def __init__(self, input_checked=True):
        self.input_checked = input_checked

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

        operands = Operand.get(Operand.expression_id == expression_id)
        operators = Operator.get(Operator.expression_id == expression_id)
        operands_valid = self.validate_operands(operands)
        operators_valid = self.validate_operators(operators)
        valid = operands_valid and operators_valid
        if ((len(operators) + 1) != len(operands)) or not valid:
            evaluation.status = Evaluation.ERRORED
            evaluation.save()
            # Result is just gonna get nothing!
            return False

        # I.e. ['+', '-']
        sorted_operators = sorted(operators, key=attrgetter('rank'))
        # I.e. ['1', '7', '3']
        sorted_operands = sorted(operands, key=attrgetter('rank'))
        final_expression = []
        for index, operand in enumerate(sorted_operands):
            final_expression.append(operand)
            if index < len(sorted_operators):
                final_expression.append(sorted_operators[index])

        # final_expression should be a list of interleaved operands and operators
        # I.e. ['1', '+', '7', '-', '3']

        result_value = eval('{}'.format(' '.join(final_expression)))
        result.value = result_value
        result.save()
        evaluation.status = Evaluation.FINISHED
        evaluation.save()

        return True


    def validate_operands(self, operands):
        return all([operand in VALID_OPERANDS for operand in operands])


    def validate_operators(self, operators):
        for operator in operators:
            try:
                int(operator)
            except Exception:
                try:
                    float(operator)
                except Exception:
                    return False

        return True
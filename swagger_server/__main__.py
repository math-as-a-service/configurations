#!/usr/bin/env python3

import flask

from swagger_server.controllers.expression_controller import add_expression, get_expression
from swagger_server.controllers.evaluation_controller import add_evaluation, get_evaluation
from swagger_server.controllers.operand_controller import add_operand, delete_operand, get_operand, put_operand
from swagger_server.controllers.operator_controller import add_operator, delete_operator, get_operator, put_operator
from swagger_server.controllers.result_controller import get_result

app = flask.Flask(__name__)


@app.route('/expression', methods=['POST'])
def post_expression_view():
    return add_expression()


@app.route('/expression/<int:expression_id>', methods=['GET'])
def get_expression_view(expression_id):
    return get_expression(expression_id)


@app.route('/evaluation', methods=['POST'])
def post_evaluation_view():
    return add_evaluation()


@app.route('/evaluation/<int:evaluation_id>', methods=['GET'])
def get_evaluation_view(evaluation_id):
    return get_evaluation(evaluation_id)


@app.route('/operand', methods=['POST'])
def add_operand_view():
    return add_operand()


@app.route('/operand/<int:id>', methods=['DELETE'])
def delete_operand_view():
    return delete_operand()


@app.route('/operand/<int:id>', methods=['GET'])
def get_operand_view():
    return get_operand()


@app.route('/operand/<int:id>', methods=['PUT'])
def put_operand_view():
    return put_operand()


@app.route('/operator', methods=['POST'])
def add_operator_view():
    return add_operator()


@app.route('/operator/<int:id>', methods=['DELETE'])
def delete_operator_view():
    return delete_operator()


@app.route('/operator/<int:id>', methods=['GET'])
def get_operator_view():
    return get_operator()


@app.route('/operator/<int:id>', methods=['PUT'])
def put_operator_view():
    return put_operator()


@app.route('/result/<int:id>', methods=['GET'])
def get_result_view(id):
    return get_result(id)

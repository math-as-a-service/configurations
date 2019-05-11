#!/usr/bin/env python3

import flask
from flask import request

from swagger_server.controllers.expression_controller import add_expression, delete_expression, get_expression, \
    put_expression
from swagger_server.controllers.evaluation_controller import add_evaluation, get_evaluation
from swagger_server.controllers.operand_controller import add_operand, delete_operand, get_operand, put_operand
from swagger_server.controllers.operator_controller import add_operator, delete_operator, get_operator, put_operator
from swagger_server.controllers.result_controller import get_result
from swagger_server.util import ValidationError, jsonify_validation_error
from swagger_server.database.utils import create_database, create_table

app = flask.Flask(__name__)
setup_cli = flask.cli.AppGroup('setup')

#
# ROUTES!
# ------------------------------------------------------------------------------


@app.route('/expression', methods=['POST'])
def post_expression_view():
    try:
        return add_expression(), 200
    except ValidationError as exc:
        return jsonify_validation_error(exc)


@app.route('/expression/<int:expression_id>', methods=['DELETE'])
def delete_expression_view(expression_id):
    try:
        return delete_expression(expression_id)
    except ValidationError as exc:
        return jsonify_validation_error(exc)


@app.route('/expression/<int:expression_id>', methods=['GET'])
def get_expression_view(expression_id):
    try:
        return get_expression(expression_id)
    except ValidationError as exc:
        return jsonify_validation_error(exc)


@app.route('/expression/<int:expression_id>', methods=['PUT'])
def put_expression_view(expression_id):
    try:
        return put_expression(expression_id)
    except ValidationError as exc:
        return jsonify_validation_error(exc)


@app.route('/evaluation', methods=['POST'])
def post_evaluation_view():
    try:
        post_body = request.get_json()
        return add_evaluation(post_body), 200
    except ValidationError as exc:
        return jsonify_validation_error(exc)


@app.route('/evaluation/<int:evaluation_id>', methods=['GET'])
def get_evaluation_view(evaluation_id):
    return get_evaluation(evaluation_id)


@app.route('/operand', methods=['POST'])
def add_operand_view():
    return add_operand()


@app.route('/operand/<int:id>', methods=['DELETE'])
def delete_operand_view(id):
    return delete_operand(id)


@app.route('/operand/<int:id>', methods=['GET'])
def get_operand_view(id):
    return get_operand(id)


@app.route('/operand/<int:id>', methods=['PUT'])
def put_operand_view(id):
    return put_operand(id)


@app.route('/operator', methods=['POST'])
def add_operator_view():
    return add_operator()


@app.route('/operator/<int:id>', methods=['DELETE'])
def delete_operator_view(id):
    return delete_operator(id)


@app.route('/operator/<int:id>', methods=['GET'])
def get_operator_view(id):
    return get_operator(id)


@app.route('/operator/<int:id>', methods=['PUT'])
def put_operator_view(id):
    return put_operator(id)

@app.route('/result/<int:id>', methods=['GET'])
def get_result_view(id):
    return get_result(id)

#
# COMMANDS!
# ------------------------------------------------------------------------------

@setup_cli.command()
def database():
    create_database()
    create_table()

app.cli.add_command(setup_cli)

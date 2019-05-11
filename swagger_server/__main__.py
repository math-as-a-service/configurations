#!/usr/bin/env python3

import flask

from swagger_server.controllers.expression_controller import add_expression, get_expression
from swagger_server.controllers.evaluation_controller import add_evaluation, get_evaluation
from swagger_server.controllers.operand_controller import add_operand, delete_operand, get_operand, put_operand
from swagger_server.controllers.operator_controller import add_operator, delete_operator, get_operator, put_operator
from swagger_server.controllers.result_controller import get_result
from swagger_server.database.utils import create_database, create_table

app = flask.Flask(__name__)
setup_cli = flask.cli.AppGroup('setup')

#
# ROUTES!
# ------------------------------------------------------------------------------

@app.route('/expression', methods=['POST'])
def post_expression_view():
    return add_expression()

@app.route('/expression/<int:expression_id>', methods=['GET'])
def get_expression_view(expression_id):
    return get_expression(expression_id)


@app.route('/evaluation', methods=['POST'])
def post_evaluation_view():
    post_body = request.POST

    return add_evaluation(post_body)


@app.route('/evaluation/<int:evaluation_id>', methods=['GET'])
def get_evaluation_view(evaluation_id):
    return get_evaluation(evaluation_id)


@app.route('/operand', methods=['POST'])
def add_operand_view():
    try:
        post_body = request.get_json()
        return add_operand(post_body), 200
    except ValidationError as exc:
        return jsonify_validation_error(exc)


@app.route('/operand/<int:id>', methods=['DELETE'])
def delete_operand_view(id):
    try:
        return delete_operand(id), 200
    except ValidationError as exc:
        return jsonify_validation_error(exc)
    return delete_operand(id)


@app.route('/operand/<int:id>', methods=['GET'])
def get_operand_view(id):
    try:
        return get_operand(id), 200
    except ValidationError as exc:
        return jsonify_validation_error(exc)
    return get_operand(id)


@app.route('/operand/<int:id>', methods=['PUT'])
def put_operand_view(id):
    try:
        post_body = request.get_json()
        return put_operand(id, post_body), 200
    except ValidationError as exc:
        return jsonify_validation_error(exc)
    return put_operand(id)


@app.route('/operator', methods=['POST'])
def add_operator_view():
    try:
        post_body = request.get_json()
        return add_operator(post_body), 200
    except ValidationError as exc:
        return jsonify_validation_error(exc)


@app.route('/operator/<int:id>', methods=['DELETE'])
def delete_operator_view(id):
    try:
        return delete_operator(id), 200
    except ValidationError as exc:
        return jsonify_validation_error(exc)


@app.route('/operator/<int:id>', methods=['GET'])
def get_operator_view(id):
    try:
        return get_operator(id), 200
    except ValidationError as exc:
        return jsonify_validation_error(exc)


@app.route('/operator/<int:id>', methods=['PUT'])
def put_operator_view(id):
    try:
        post_body = request.get_json()
        return put_operator(id, post_body), 200
    except ValidationError as exc:
        return jsonify_validation_error(exc)

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

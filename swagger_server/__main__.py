#!/usr/bin/env python3

import flask
from flask import request

from swagger_server.controllers.expression_controller import add_expression, delete_expression, get_expression, \
    put_expression
from swagger_server.controllers.evaluation_controller import add_evaluation, get_evaluation, get_evaluation_finalized_expression
from swagger_server.controllers.operand_controller import add_operand, delete_operand, get_operand, put_operand
from swagger_server.controllers.operator_controller import add_operator, delete_operator, get_operator, put_operator
from swagger_server.controllers.result_controller import get_result
from swagger_server.util import ValidationError, jsonify_validation_error
from swagger_server.database.utils import create_database, create_table
from swagger_server.util import ValidationError

app = flask.Flask(__name__)
setup_cli = flask.cli.AppGroup('setup')

#
# ROUTES!
# ------------------------------------------------------------------------------

#
# EXPRESSIONS!
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
        return delete_expression(expression_id), 200
    except ValidationError as exc:
        return jsonify_validation_error(exc)


@app.route('/expression/<int:expression_id>', methods=['GET'])
def get_expression_view(expression_id):
    try:
        return get_expression(expression_id), 200
    except ValidationError as exc:
        return jsonify_validation_error(exc)


@app.route('/expression/<int:expression_id>', methods=['PUT'])
def put_expression_view(expression_id):
    try:
        return put_expression(expression_id), 200
    except ValidationError as exc:
        return jsonify_validation_error(exc)

#
# EVALUATION!
# ------------------------------------------------------------------------------

@app.route('/evaluation', methods=['POST'])
def post_evaluation_view():
    try:
        post_body = request.get_json()
        return add_evaluation(post_body), 200
    except ValidationError as exc:
        return jsonify_validation_error(exc)


@app.route('/evaluation/<int:evaluation_id>', methods=['GET'])
def get_evaluation_view(evaluation_id):
    try:
        return get_evaluation(evaluation_id)
    except ValidationError as exc:
        return jsonify_validation_error(exc)

@app.route('/evaluation/<int:evaluation_id>/view', methods=['GET'])
def get_evaluation_finalized_expression_view(evaluation_id):
    try:
        return get_evaluation_finalized_expression(evaluation_id)
    except ValidationError as exc:
        return jsonify_validation_error(exc)

#
# OPERAND!
# ------------------------------------------------------------------------------

@app.route('/operand', methods=['POST'])
def add_operand_view():
    """
    Requires a json in this format:
    {
        "expression_id": 1,
         "rank": 2,
         "value": "3",
         "type": 4
    }
    """
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

@app.route('/operand/<int:id>', methods=['GET'])
def get_operand_view(id):
    try:
        return get_operand(id), 200
    except ValidationError as exc:
        return jsonify_validation_error(exc)


@app.route('/operand/<int:id>', methods=['PUT'])
def put_operand_view(id):
    try:
        post_body = request.get_json()
        return put_operand(id, post_body), 200
    except ValidationError as exc:
        return jsonify_validation_error(exc)

#
# OPERATOR!
# ------------------------------------------------------------------------------

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

#
# RESULT!
# ------------------------------------------------------------------------------

@app.route('/result/<int:result_id>', methods=['GET'])
def get_result_view(result_id):
    if not result_id:
        return jsonify_validation_error(
            ValidationError(400, 'An evaluation result ID is required!')
        )

    try:
        return get_result(result_id)
    except ValidationError as exc:
        return jsonify_validation_error(exc)

#
# COMMANDS!
# ------------------------------------------------------------------------------

@setup_cli.command()
def database():
    create_database()
    create_table()

app.cli.add_command(setup_cli)

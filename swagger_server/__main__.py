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

def get_handler_for_object_type(object_type, http_method):
    # TODO: Is this terrible? It's enough metaprogramming such that IDEs won't be able to pick up that imports are used.
    if http_method == 'POST':
        lookup_method = 'add'
    else:
        lookup_method = http_method.lower()
    return globals()['{}_{}'.format(lookup_method, object_type)]

@app.route('/<object_type>', methods=['POST'])
def post_view_handler(object_type):
    handler = get_handler_for_object_type(object_type, 'POST')
    # Expression is special - might be a better way to tackle this.
    if object_type == 'expression':
        try:
            return handler(), 200
        except ValidationError as exc:
            return jsonify_validation_error(exc)
    else:
        try:
            post_body = request.get_json()
            return handler(post_body), 200
        except ValidationError as exc:
            return jsonify_validation_error(exc)


@app.route('/<object_type>/<int:object_id>', methods=['GET', 'DELETE'])
def get_and_delete_view_handler(object_type, object_id):
    handler = get_handler_for_object_type(object_type, request.method)
    try:
        return handler(object_id), 200
    except ValidationError as exc:
        return jsonify_validation_error(exc)

@app.route('/<object_type>/<int:object_id>', methods=['PUT'])
def put_view_handler(object_type, object_id):
    handler = get_handler_for_object_type(object_type, 'PUT')
    try:
        post_body = request.get_json()
        return handler(object_id, post_body), 200
    except ValidationError as exc:
        return jsonify_validation_error(exc)

@app.route('/evaluation/<int:evaluation_id>/view', methods=['GET'])
def get_evaluation_finalized_expression_view(evaluation_id):
    try:
        return get_evaluation_finalized_expression(evaluation_id)
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

#!/usr/bin/env python3

import flask

from swagger_server.controllers.expression_controller import add_expression, get_expression
from swagger_server.controllers.evaluation_controller import add_evaluation, get_evaluation
from swagger_server.controllers.result_controller import get_result

app = flask.Flask(__name__)


@app.route('/expression', methods=['POST'])
def post_expression_view():
    return add_expression()


@app.route('/expression', methods=['GET'])
def get_expression_view():
    expression_id = flask.request.json['expression_id']
    return get_expression(expression_id)


@app.route('/evaluation', methods=['POST'])
def post_evaluation_view():
    return add_evaluation()


@app.route('/evaluation', methods=['GET'])
def get_evaluation_view():
    evaluation_id = flask.request.json['evaluation_id']
    return get_evaluation(evaluation_id)


@app.route('/result', methods=['GET'])
def get_result_view():
    return get_result()

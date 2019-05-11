#!/usr/bin/env python3

from flask import Flask

from swagger_server.controllers.expression_controller import add_expression, get_expression
from swagger_server.controllers.operand_controller import add_operand, delete_operand, get_operand, put_operand
from swagger_server.controllers.operator_controller import add_operator, delete_operator, get_operator, put_operator

app = Flask(__name__)

@app.route('/expression', methods=['POST'])
def post_expression_view():
    return add_expression()

@app.route('/expression', methods=['GET'])
def get_expression_view():
    return get_expression()

@app.route('/operand', methods=['POST'])
def add_operand_view():
    return add_operand()

@app.route('/operand', methods=['DELETE'])
def delete_operand_view():
    return delete_operand()

@app.route('/operand', methods=['GET'])
def get_operand_view():
    return get_operand()

@app.route('/operand', methods=['PUT'])
def put_operand_view():
    return put_operand()

@app.route('/operator', methods=['POST'])
def add_operator_view():
    return add_operator()

@app.route('/operator', methods=['DELETE'])
def delete_operator_view():
    return delete_operator()

@app.route('/operator', methods=['GET'])
def get_operator_view():
    return get_operator()

@app.route('/operator', methods=['PUT'])
def put_operator_view():
    return put_operator()



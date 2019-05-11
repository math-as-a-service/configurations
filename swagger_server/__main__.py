#!/usr/bin/env python3

from flask import Flask

from swagger_server.controllers.expression_controller import add_expression

app = Flask(__name__)

@app.route('/expression', methods=['POST'])
def post_expression_view():
    return add_expression()

@app.route('/expression', methods=['GET'])
def get_expression_view():
    return get_expression()

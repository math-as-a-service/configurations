#!/usr/bin/env python3

import pymysql

from swagger_server.models.evaluation import Evaluation
from swagger_server.models.evaluation_status import EvaluationStatus
from swagger_server.models.expression import Expression
from swagger_server.models.operand import Operand
from swagger_server.models.operator import Operator
from swagger_server.models.result import Result
from swagger_server.models.value_type import ValueType


MODEL_CONSTRUCTORS = [
    Evaluation,
    EvaluationStatus,
    Expression,
    Operand,
    Operator,
    Result,
    ValueType,
]

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
)

def create_table():
    # http://docs.peewee-orm.com/en/2.10.2/peewee/models.html?highlight=create_table#creating-model-tables
    for model in MODEL_CONSTRUCTORS:
        model.create_table()

def create_database():
    with connection.cursor() as cursor:
        cursor.execute('CREATE DATABASE IF NOT EXISTS maas')
        cursor.execute("GRANT ALL ON `maas`.* TO 'maas_user'@'localhost' IDENTIFIED BY 'maas_password'")

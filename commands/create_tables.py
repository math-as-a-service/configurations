#!/usr/bin/env python3

from swagger_server.models import (
    Evaluation, EvaluationStatus, Expression, Operand, Operator, Result, ValueType,
)

MODEL_CONSTRUCTORS = [
    Evaluation,
    EvaluationStatus,
    Expression,
    Operand,
    Operator,
    Result,
    ValueType,
]

# http://docs.peewee-orm.com/en/2.10.2/peewee/models.html?highlight=create_table#creating-model-tables
for model in MODEL_CONSTRUCTORS:
    model.create_table()

# coding: utf-8

from __future__ import absolute_import
from peewee import *

from .expression import Expression
from swagger_server.models.base_model_ import FlaskModel


class Evaluation(FlaskModel):
    id = AutoField()
    expression_id = ForeignKeyField(Expression)
    result_id = IntegerField()
    status = SmallIntegerField()

# coding: utf-8

from __future__ import absolute_import
from peewee import *

from swagger_server.models.base_model_ import FlaskModel
from .expression import Expression


class Operand(FlaskModel):
    id = AutoField()
    expression_id = ForeignKeyField(Expression)
    rank = IntegerField()
    value = CharField()
    type = IntegerField()

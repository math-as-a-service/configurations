# coding: utf-8

from __future__ import absolute_import
from peewee import *

from .expression import Expression
from swagger_server.models.base_model_ import FlaskModel


class Evaluation(FlaskModel):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    STARTING, EVALUATING, FINISHED, ERRORED = range(4)

    id = AutoField()
    expression_id = ForeignKeyField(Expression)
    result_id = IntegerField()
    status = SmallIntegerField()

    def is_complete(self):
        return self.status == self.FINISHED

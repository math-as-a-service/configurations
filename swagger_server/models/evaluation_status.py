# coding: utf-8

from __future__ import absolute_import
from peewee import *

from swagger_server.models.base_model_ import FlaskModel


class EvaluationStatus(FlaskModel):
    id = AutoField()
    label = CharField()

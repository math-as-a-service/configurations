# coding: utf-8

from __future__ import absolute_import
from peewee import *

from swagger_server.models.base_model_ import FlaskModel


class Result(FlaskModel):
    id = AutoField()
    value = CharField()
    type = SmallIntegerField()

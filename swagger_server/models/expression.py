# coding: utf-8

from __future__ import absolute_import
from datetime import datetime  # noqa: F401
from peewee import *

from swagger_server.models.base_model_ import FlaskModel


class Expression(FlaskModel):
    id = AutoField()
    created = DateTimeField(default=datetime.now)
    updated = DateTimeField(default=datetime.now)

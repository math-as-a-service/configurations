import pprint

import six
import typing

from swagger_server import util
from peewee import *

class FlaskModel(Model):

    def api_serialize(self):
        serialized_object = {}
        for field in self._meta.fields:
            suffix = '_id' if self._is_foreign_key(field) else ''
            serialized_object[field] = getattr(self, field + suffix, None)

        return serialized_object

    def _is_foreign_key(self, field):
        return issubclass(type(getattr(self, field, None)), FlaskModel)

    class Meta:
        database = MySQLDatabase('maas', user='maas_user', password='maas_password')

# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401


from swagger_server import util

from peewee import *

from swagger_server.models.base_model_ import FlaskModel

from swagger_server.models import Expression

class Operator(Model, FlaskModel):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    id = AutoField()
    expression_id = ForeignKeyField(Expression)
    rank = IntegerField()
    value = CharField()
    type = IntegerField()

    def __init__(self, id: int=None, expression_id: int=None, rank: int=None, value: str=None, type: int=None):  # noqa: E501
        """Operator - a model defined in Swagger

        :param id: The id of this Operator.  # noqa: E501
        :type id: int
        :param expression_id: The expression_id of this Operator.  # noqa: E501
        :type expression_id: int
        :param rank: The rank of this Operator.  # noqa: E501
        :type rank: int
        :param value: The value of this Operator.  # noqa: E501
        :type value: str
        :param type: The type of this Operator.  # noqa: E501
        :type type: int
        """
        self.swagger_types = {
            'id': int,
            'expression_id': int,
            'rank': int,
            'value': str,
            'type': int
        }

        self.attribute_map = {
            'id': 'id',
            'expression_id': 'expression_id',
            'rank': 'rank',
            'value': 'value',
            'type': 'type'
        }

        self._id = id
        self._expression_id = expression_id
        self._rank = rank
        self._value = value
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'Operator':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Operator of this Operator.  # noqa: E501
        :rtype: Operator
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Operator.


        :return: The id of this Operator.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Operator.


        :param id: The id of this Operator.
        :type id: int
        """

        self._id = id

    @property
    def expression_id(self) -> int:
        """Gets the expression_id of this Operator.


        :return: The expression_id of this Operator.
        :rtype: int
        """
        return self._expression_id

    @expression_id.setter
    def expression_id(self, expression_id: int):
        """Sets the expression_id of this Operator.


        :param expression_id: The expression_id of this Operator.
        :type expression_id: int
        """

        self._expression_id = expression_id

    @property
    def rank(self) -> int:
        """Gets the rank of this Operator.


        :return: The rank of this Operator.
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank: int):
        """Sets the rank of this Operator.


        :param rank: The rank of this Operator.
        :type rank: int
        """

        self._rank = rank

    @property
    def value(self) -> str:
        """Gets the value of this Operator.


        :return: The value of this Operator.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """Sets the value of this Operator.


        :param value: The value of this Operator.
        :type value: str
        """

        self._value = value

    @property
    def type(self) -> int:
        """Gets the type of this Operator.


        :return: The type of this Operator.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type: int):
        """Sets the type of this Operator.


        :param type: The type of this Operator.
        :type type: int
        """

        self._type = type

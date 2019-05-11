# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import FlaskModel
from swagger_server import util

from peewee import *

from .expression import Expression

class Operand(Model, FlaskModel):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    id = AutoField()
    expression_id = ForeignKeyField(Expression)
    rank = IntegerField()
    value = CharField()
    type = IntegerField()

    @classmethod
    def from_dict(cls, dikt) -> 'Operand':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Operand of this Operand.  # noqa: E501
        :rtype: Operand
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Operand.


        :return: The id of this Operand.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Operand.


        :param id: The id of this Operand.
        :type id: int
        """

        self._id = id

    @property
    def expression_id(self) -> int:
        """Gets the expression_id of this Operand.


        :return: The expression_id of this Operand.
        :rtype: int
        """
        return self._expression_id

    @expression_id.setter
    def expression_id(self, expression_id: int):
        """Sets the expression_id of this Operand.


        :param expression_id: The expression_id of this Operand.
        :type expression_id: int
        """

        self._expression_id = expression_id

    @property
    def rank(self) -> int:
        """Gets the rank of this Operand.


        :return: The rank of this Operand.
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank: int):
        """Sets the rank of this Operand.


        :param rank: The rank of this Operand.
        :type rank: int
        """

        self._rank = rank

    @property
    def value(self) -> str:
        """Gets the value of this Operand.


        :return: The value of this Operand.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """Sets the value of this Operand.


        :param value: The value of this Operand.
        :type value: str
        """

        self._value = value

    @property
    def type(self) -> int:
        """Gets the type of this Operand.


        :return: The type of this Operand.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type: int):
        """Sets the type of this Operand.


        :param type: The type of this Operand.
        :type type: int
        """

        self._type = type

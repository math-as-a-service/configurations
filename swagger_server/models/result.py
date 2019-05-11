# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401
from peewee import *

from swagger_server.models.base_model_ import FlaskModel
from swagger_server import util


class Result(FlaskModel):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    id = AutoField()
    value = CharField()
    type = SmallIntegerField()

    @classmethod
    def from_dict(cls, dikt) -> 'Result':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Result of this Result.  # noqa: E501
        :rtype: Result
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Result.


        :return: The id of this Result.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Result.


        :param id: The id of this Result.
        :type id: int
        """

        self._id = id

    @property
    def value(self) -> str:
        """Gets the value of this Result.


        :return: The value of this Result.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """Sets the value of this Result.


        :param value: The value of this Result.
        :type value: str
        """

        self._value = value

    @property
    def type(self) -> int:
        """Gets the type of this Result.


        :return: The type of this Result.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type: int):
        """Sets the type of this Result.


        :param type: The type of this Result.
        :type type: int
        """

        self._type = type

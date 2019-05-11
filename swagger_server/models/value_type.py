# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ValueType(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, label: str=None):  # noqa: E501
        """ValueType - a model defined in Swagger

        :param id: The id of this ValueType.  # noqa: E501
        :type id: int
        :param label: The label of this ValueType.  # noqa: E501
        :type label: str
        """
        self.swagger_types = {
            'id': int,
            'label': str
        }

        self.attribute_map = {
            'id': 'id',
            'label': 'label'
        }

        self._id = id
        self._label = label

    @classmethod
    def from_dict(cls, dikt) -> 'ValueType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ValueType of this ValueType.  # noqa: E501
        :rtype: ValueType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this ValueType.


        :return: The id of this ValueType.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this ValueType.


        :param id: The id of this ValueType.
        :type id: int
        """

        self._id = id

    @property
    def label(self) -> str:
        """Gets the label of this ValueType.


        :return: The label of this ValueType.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label: str):
        """Sets the label of this ValueType.


        :param label: The label of this ValueType.
        :type label: str
        """

        self._label = label

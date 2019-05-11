import flask

import peewee

from swagger_server import util
from swagger_server.models.operand import Operand
from swagger_server.util import ValidationError


def add_operand(payload):  # noqa: E501
    """Create an operand

    Creates an operand # noqa: E501


    :rtype: None
    """
    if not payload:
        raise ValidationError(400, 'Couldn\'t parse JSON POST body.')
    if not payload.get('expression_id'):
        raise ValidationError(400, 'No expression_id field specified')
    if not payload.get('rank'):
        raise ValidationError(400, 'No rank field specified')
    if not payload.get('value'):
        raise ValidationError(400, 'No value field specified')
    if not payload.get('type'):
        raise ValidationError(400, 'No type field specified')
    try:
        operand = Operand.create(expression_id=payload.expression_id, rank=payload.rank, value=payload.value, type=payload.type)
    except peewee.IntegrationException as exc:
        raise ValidationError(400, 'Expression not found!')
    return flask.jsonify({'operand_id': operand.id})


def delete_operand(operand_id):  # noqa: E501
    """Delete operand object

    Delete operand object # noqa: E501

    :param operand_id: ID of operand to return
    :type operand_id: int

    :rtype: None
    """
    operand = Operand.delete_by_id(operand_id)
    return flask.jsonify(operand == 1)


def get_operand(operand_id):  # noqa: E501
    """Retrieve operand object

    Retrieve operand object # noqa: E501

    :param operand_id: ID of operand to return
    :type operand_id: int

    :rtype: None
    """
    try:
        operand = Operand.get_by_id(operand_id)
    except Exception as exc:
        raise ValidationError(404, 'Operand not found!')
    return flask.jsonify(operand.api_serialize())


def put_operand(operand_id, payload):  # noqa: E501
    """Update operand object

    Update operand object # noqa: E501

    :param operand_id: ID of operand to return
    :type operand_id: int

    :rtype: None
    """
    if not payload:
        raise ValidationError(400, 'Couldn\'t parse JSON POST body.')
    try:
        operand = Operand.get_by_id(operand_id)
        operand.expression_id = payload['expression_id']
        operand.rank = payload['rank']
        operand.value = payload['value']
        operand.type = payload['type']
        operand.save()
    except peewee.IntegrationException as exc:
        raise ValidationError(400, 'Expression not found!')
    return flask.jsonify(operand.api_serialize())

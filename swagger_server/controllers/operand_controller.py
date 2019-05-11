import flask

from swagger_server import util
from swagger_server.models.evaluation import Operand
from swagger_server.util import ValidationError


def add_operand(payload):  # noqa: E501
    """Create an operand

    Creates an operand # noqa: E501


    :rtype: None
    """
    if not payload:
        raise ValidationError(400, 'Couldn\'t parse JSON POST body.')
    if not payload.get('expression_id'):
        raise ValidationError(400, 'No id field specified')
    try:
        operator = Operand.create(expression_id=payload.expression_id, rank=payload.rank, value=payload.value, type=payload.type)
    except Exception as exc:
        raise ValidationError(400, 'Expression not found!')
    return flask.jsonify({'expression_id': operator.expression_id})


def delete_operand(operand_id):  # noqa: E501
    """Delete operand object

    Delete operand object # noqa: E501

    :param operand_id: ID of operand to return
    :type operand_id: int

    :rtype: None
    """
    try:
        operand = Operand.delete().where(Operand.id == operand_id)
    except Exception as exc:
        raise ValidationError(400, 'Expression not found!')
    return flask.jsonify({'expression_id': operand_id})


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
        raise ValidationError(400, 'Expression not found!')
    return flask.jsonify({'id': operand_id})


def put_operand(operand_id, payload):  # noqa: E501
    """Update operand object

    Update operand object # noqa: E501

    :param operand_id: ID of operand to return
    :type operand_id: int

    :rtype: None
    """
    if not payload:
        raise ValidationError(400, 'Couldn\'t parse JSON POST body.')
    if not payload.get('id'):
        raise ValidationError(400, 'No id field specified')
    try:
        operator = Operand.update(payload).where(id=operand_id).execute()
    except Exception as exc:
        raise ValidationError(400, 'Expression not found!')
    return flask.jsonify({'id': operand_id})

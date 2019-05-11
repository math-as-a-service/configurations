import flask
import peewee

from swagger_server import util
from swagger_server.models.evaluation import Operator
from swagger_server.util import ValidationError


def add_operator(payload):  # noqa: E501
    """Create an operator

    Creates an operator # noqa: E501


    :rtype: None
    """
    if not payload:
        raise ValidationError(400, 'Couldn\'t parse JSON POST body.')
    if not payload.get('expression_id'):
        raise ValidationError(400, 'No id field specified')
    try:
        operator = Operator.create(expression_id=payload.expression_id, rank=payload.rank, value=payload.value, type=payload.type)
    except peewee.IntegrationException as exc:
        raise ValidationError(400, 'Expression not found!')
    return flask.jsonify({'expression_id': operator.id})


def delete_operator(operator_id):  # noqa: E501
    """Delete operator object

    Delete operator object # noqa: E501

    :param operator_id: ID of operator to return
    :type operator_id: int

    :rtype: None
    """
    try:
        operand = Operator.delete().where(Operator.id == operator_id)
    except Exception as exc:
        raise ValidationError(404, 'Operator not found!')
    return flask.jsonify(True)


def get_operator(operator_id):  # noqa: E501
    """Retrieve operator object

    Retrieve operator object # noqa: E501

    :param operator_id: ID of operator to return
    :type operator_id: int

    :rtype: None
    """
    try:
        operator = Operator.get_by_id(operator_id)
    except Exception as exc:
        raise ValidationError(404, 'Operand not found!')
    return flask.jsonify(operator.api_serialize())


def put_operator(operator_id, payload):  # noqa: E501
    """Update operator object

    Update operator object # noqa: E501

    :param operator_id: ID of operator to return
    :type operator_id: int

    :rtype: None
    """
    if not payload:
        raise ValidationError(400, 'Couldn\'t parse JSON POST body.')
    try:
        operator = Operator.get_by_id(operator_id)
        operator.expression_id = payload['expression_id']
        operator.rank = payload['rank']
        operator.value = payload['value']
        operator.type = payload['type']
        operator.save()
    except peewee.IntegrationException as exc:
        raise ValidationError(400, 'Expression not found!')
    return flask.jsonify(operator.api_serialize())

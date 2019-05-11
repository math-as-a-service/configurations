import flask

from swagger_server.models.expression import Expression
from swagger_server.util import ValidationError


def add_expression():  # noqa: E501
    """Create an empty expression

    Creates an empty expression # noqa: E501


    :rtype: None
    """
    try:
        Expression.create()
    except Exception as exc:
        raise ValidationError(400, 'Expression was not created')

    return flask.jsonify(True)


def delete_expression(expression_id):  # noqa: E501
    """Delete expression object

    Delete expression object # noqa: E501

    :param expression_id: ID of expression to return
    :type expression_id: int

    :rtype: None
    """
    row = Expression.get_or_none(Expression.id == expression_id)
    result = row.delete_instance() if row else 0
    return flask.jsonify({'expression_id': expression_id, 'rows_deleted': result})


def get_expression(expression_id):  # noqa: E501
    """Retrieve expression object

    Retrieve expression object # noqa: E501

    :param expression_id: ID of expression to return
    :type expression_id: int

    :rtype: None
    """
    return 'do some magic!'


def put_expression(expression_id):  # noqa: E501
    """Update expression object

    Update expression object # noqa: E501

    :param expression_id: ID of expression to return
    :type expression_id: int

    :rtype: None
    """
    return 'do some magic!'

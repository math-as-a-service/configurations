import datetime
import flask
from peewee import DoesNotExist
from swagger_server.models.expression import Expression
from swagger_server.util import ValidationError


def add_expression():
    """
    Create an empty expression
    """
    try:
        result = Expression.create()
    except Exception as exc:
        raise ValidationError(400, 'Expression was not created')

    return flask.jsonify(result.api_serialize())


def delete_expression(expression_id):
    """
    Delete expression object - will not throw exception if invalid expression_id is passed
    """
    result = Expression.delete_by_id(expression_id)
    return flask.jsonify({'expression_id': expression_id, 'rows_deleted': result})


def get_expression(expression_id):
    """
    Retrieve expression object - will throw exception if invalid expression_id is passed
    """
    try:
        result = Expression.get_by_id(expression_id)
    except DoesNotExist:
        raise ValidationError(404, 'Expression id ({}) not found.'.format(expression_id))

    return flask.jsonify(result.api_serialize())


def put_expression(expression_id):
    """
    Update expression object
    """
    try:
        row = Expression.get_by_id(expression_id)
    except DoesNotExist:
        raise ValidationError(404, 'Expression id ({}) not found.'.format(expression_id))

    row.updated = datetime.datetime.now()
    row.save()

    return flask.jsonify(row.api_serialize())

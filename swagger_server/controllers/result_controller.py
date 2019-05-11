from swagger_server.models.result import Result
from swagger_server.util import ValidationError
from peewee import DoesNotExist
import flask


def get_result(result_id):
    """Get the finished result of an evaluation

    :rtype: None
    """
    try:
        result = Result.get_by_id(result_id)
    except DoesNotExist:
        raise ValidationError(404, 'Result at ID ({}) not found.'.found(result_id))

    return flask.jsonify(result.api_serialize())

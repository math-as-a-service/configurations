from swagger_server.models.result import Result
from swagger_server.models.evaluation import Evaluation
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
        raise ValidationError(404, 'Result at ID ({}) not found.'.format(result_id))

    try:
        evaluation = Evaluation.get(Evaluation.result_id == result.id)
    except DoesNotExist:
        raise ValidationError(404, 'Evaluation for Result at ID ({}) not found.'.format(result.id))

    if not evaluation.is_complete():
        # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/425
        raise ValidationError(425, 'Evaluation for Result at ID ({}) not found.'.format(result.id))

    return flask.jsonify(result.api_serialize())

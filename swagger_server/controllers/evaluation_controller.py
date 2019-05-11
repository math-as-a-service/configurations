import flask

from swagger_server.models.evaluation import Evaluation
from swagger_server.models.result import Result
from swagger_server.util import ValidationError
from peewee import IntegrityError, DoesNotExist


def add_evaluation(payload):  # noqa: E501
    """Begin evaluation of an expression

    Begin evaluation of an expression # noqa: E501


    :rtype: None
    """
    if not payload:
        raise ValidationError(400, 'Couldn\'t parse JSON POST body.')
    if not payload.get('expression_id'):
        raise ValidationError(400, 'No expression_id field specified')

    # Work
    result = Result.create(value='', type='')

    try:
        evaluation = Evaluation.create(expression_id=payload.expression_id, status=Evaluation.STARTING, result_id=result.id)
    except IntegrityError as exc:
        raise ValidationError(400, 'Expression not found!')

    return flask.jsonify({'evaluation_id' : evaluation.id})


def get_evaluation(evaluation_id):  # noqa: E501
    """Poll for result of an evaluation

    Poll for result of an evaluation # noqa: E501

    :param evaluation_id: ID of evaluation to return
    :type evaluation_id: int

    :rtype: None
    """

    try:
        evaluation = Evaluation.get_by_id(evaluation_id)
    except DoesNotExist:
        raise ValidationError(404, 'Evaluation ID ({}) not found.'.format(evaluation_id))

    return flask.jsonify(evaluation.api_serialize())

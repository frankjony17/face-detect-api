
from flask import Blueprint, abort, jsonify

error_handler = Blueprint('error_handler', __name__)


error_dict = {
    400: {'detail': 'Bad Request, wrong syntax, '
                    'the request could not be understood by the server.'},
    401: {'detail': 'Bad Request, wrong base64 format.'},
    404: {'detail': 'Bad Request, required parameters missing, parameters '
                    'wasn\'t found.'},
    405: {'detail': 'Bad Request, face not found, a face was not found in the '
                    'image'},
    408: {'detail': 'Bad Request, required value is invalid, the value of the '
                    'cropped parameter must be boolean (bool)'},
}


def raise_error(code):
    if code > 200:
        abort(code)


def response(code):
    """Return response message according to request type of error.
    Args:
        code (int): Code of error.
    Returns:
        dict or None: Message and reason from request type of error.
    """
    return error_dict.get(code, None)


@error_handler.app_errorhandler(400)
def wrong_syntax(error):
    return jsonify(response(400)), 400


@error_handler.app_errorhandler(401)
def no_face(error):
    return jsonify(response(401)), 400


@error_handler.app_errorhandler(404)
def bad_image(error):
    return jsonify(response(404)), 400


@error_handler.app_errorhandler(405)
def face_not_found(error):
    return jsonify(response(405)), 400


@error_handler.app_errorhandler(408)
def bad_number(error):
    return jsonify(response(408)), 400

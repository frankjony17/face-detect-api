import logging

from flask import Blueprint, jsonify, request

from face_detect.service.detector_service import DetectorService
from face_detect.util.api_util import ApiUtil

detection_route = Blueprint('detection_route', __name__)


@detection_route.route("/image/face-detect", methods=['POST'])
def image_detect():
    api_util = ApiUtil()
    service = DetectorService()

    image_np, cropped = api_util.is_valid_request(request)
    faces_detected = service.face_detector(image_np, cropped)
    # Output response.
    output_response = {
        'number_of_faces': len(faces_detected),
        'cropped_faces': cropped,
        'data': faces_detected
    }
    logging.getLogger('face-detect.controller').info('face detector -> OK')
    return jsonify(output_response), 200

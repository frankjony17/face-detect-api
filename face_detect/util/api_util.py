import base64
import binascii

import cv2
import numpy as np

from face_detect.util.response_error import raise_error


class ApiUtil:

    @staticmethod
    def to_numpy(encoded):
        """Convert base64 to numpy.
        Args:
            encoded (str): Base64 encoded string to decode.
        Returns:
            'np.ndarray: An ndimentional array of the input image.
        Raises:
            ValueError: Wrong base64 image.
        """
        nparr = np.frombuffer(base64.b64decode(encoded), np.uint8)
        try:
            np_res = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        except cv2.error:
            raise ValueError('No correct base64 value.')
        return np_res

    @staticmethod
    def is_base64(str_b64):
        """Check if str represents base64 format.
        Args:
            str_b64 (str): String containing base64 code.
        Returns:
            bool: True if input is base64 encoded, raise ValueError otherwise.
        Raises:
            ValueError: Wrong base64 input.
        """
        try:
            base64.b64decode(str_b64)
        except binascii.Error:
            raise ValueError('No correct base64 value.')
        return True

    def is_valid_request(self, request):
        """Check if the request has the valid parameters and values.
        Args:
            request (Request): Object of the request.
        Returns:
            vector: (np.ndarray) an n dimensional array of the 64 image.
        """
        if not request.is_json:
            raise_error(400)
        result = request.get_json()
        # The request contains the correct parameters?
        if not all(key in result for key in ['image', 'cropped']):
            raise_error(404)
        # Contains a boolean value?
        if isinstance(result['cropped'], bool) is False:
            raise_error(408)
        # str represents base64?
        image_np = self.__is_64image(result)  # return an numpy array.
        # ---
        return image_np, result['cropped']

    def __is_64image(self, result):
        """Check if the image is base64 valid.
        Args:
            result (dic): Dictionary with the requisition data.
        Returns:
            np.ndarray: An n dimensional array of the 64 image.
        """
        image_np = result['image']
        try:
            self.is_base64(image_np)
            image_np = self.to_numpy(image_np)
        except ValueError:
            raise_error(401)
        # Is valid numpy?
        if image_np is None:
            raise_error(401)
        return image_np

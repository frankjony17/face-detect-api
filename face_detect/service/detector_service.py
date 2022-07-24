
import base64
from io import BytesIO

import dlib
from PIL import Image

from face_detect.util.response_error import raise_error


class DetectorService:

    def __init__(self):
        self.detector = dlib.get_frontal_face_detector()

    def face_detector(self, image_np, cropped):
        """Face detector using HOG filter.
        Args:
            image_np (obj): numpy.ndarray 64 image.
            cropped (boolean): Determine if the faces found in the image
            should be returned.
        Returns:
            list: Bounding boxes of each face.
        """
        faces = None
        # Number of times it should up sample.
        number_of_times_to_up_sample = 0
        try:
            faces = self.detector(image_np, number_of_times_to_up_sample)
        except TypeError:
            raise_error(401)
        return self.get_box_from_faces(faces, image_np, cropped)

    def get_box_from_faces(self, faces, image_np, cropped):
        """Bounding boxes of each face.
        Args:
            faces (dlib.rectangle): Bounding boxes from faces.
            image_np (obj): numpy.ndarray 64 image.
            cropped (boolean): Determine if the faces found in the image
             should be returned.
        Returns:
            list: Bounding boxes and base64 cropped face.
        """
        bounding_boxes_and_base64_face = []
        for box in faces:
            bounding_box = {
                'left': box.left(),
                'top': box.top(),
                'right': box.right(),
                'bottom': box.bottom()
            }
            if cropped:  # Return cropped face in base 64 string.
                bounding_box['cropped_face'] = \
                    self.get_base64_from_bounding_box(box, image_np)
            bounding_boxes_and_base64_face.append(bounding_box)

        return bounding_boxes_and_base64_face

    @staticmethod
    def get_base64_from_bounding_box(box, image_np):
        """Get base 64 of the face found.
        Args:
            box (dlib.rectangle): Bounding boxes from face.
            image_np (obj): numpy.ndarray 64 image.
        Returns:
            str: Base64 cropped face.
        """
        buff = BytesIO()
        cropped_face = image_np[box.top():box.bottom(), box.left():box.right()]
        pil_img = Image.fromarray(cropped_face)
        pil_img.save(buff, "PNG")
        new_image_64 = base64.b64encode(buff.getvalue()).decode("utf-8")
        return new_image_64

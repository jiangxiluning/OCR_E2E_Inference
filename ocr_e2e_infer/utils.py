#   ______                                           __
#  /      \                                         /  |
# /$$$$$$  | __   __   __   ______   _______        $$ |       __    __
# $$ |  $$ |/  | /  | /  | /      \ /       \       $$ |      /  |  /  |
# $$ |  $$ |$$ | $$ | $$ |/$$$$$$  |$$$$$$$  |      $$ |      $$ |  $$ |
# $$ |  $$ |$$ | $$ | $$ |$$    $$ |$$ |  $$ |      $$ |      $$ |  $$ |
# $$ \__$$ |$$ \_$$ \_$$ |$$$$$$$$/ $$ |  $$ |      $$ |_____ $$ \__$$ |
# $$    $$/ $$   $$   $$/ $$       |$$ |  $$ |      $$       |$$    $$/
#  $$$$$$/   $$$$$/$$$$/   $$$$$$$/ $$/   $$/       $$$$$$$$/  $$$$$$/
#
# @Time : 2019/11/7 21:53
# @Author : Lu Ning 
# @File : utils.py
# @Email: jiangxiluning@gmail.com
# @Description: say something informative
import numpy as np
import cv2
import base64

from . import errors

def crop_patch(image: np.ndarray, box: np.ndarray) -> np.ndarray:
    """

    Args:
        image (np.ndarray): image
        box (np.ndarray): oriented rectangle, len(box) = 9

    Returns:
        patch (np.ndarray): cropped patch

    """
    box = box.reshape(4,2)
    center, size, angle = cv2.minAreaRect(box)

    width, height = size

    if angle < -45.:
        angle += 90.0
        width, height = height, width
        size = (width, height)

    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (image.shape[0], image.shape[1]), cv2.INTER_CUBIC)
    cropped = cv2.getRectSubPix(rotated, size, center)

    return cropped


def read_image_from_base64(image: bytes) -> np.ndarray:
    """

    Args:
        image (bytes): base64 bytestring

    Returns:
        image (np.ndarray): opencv image

    Raises:
        ImageReadingError

    """
    try:
        nparr = np.frombuffer(base64.b64decode(image), np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        return img
    except Exception:
        raise errors.ImageReadingError('Base64 bytestring decoding failed!')

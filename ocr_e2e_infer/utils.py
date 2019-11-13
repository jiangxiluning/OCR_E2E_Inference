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

    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (image.shape[0], image.shape[1]), cv2.INTER_CUBIC)
    cropped = cv2.getRectSubPix(rotated, size, center)

    return cropped




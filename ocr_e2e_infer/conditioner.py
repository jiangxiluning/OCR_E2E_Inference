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
# @Time : 2019/11/7 21:54
# @Author : Lu Ning 
# @File : conditioner.py
# @Email: jiangxiluning@gmail.com
# @Description: say something informative
from typing import List, Dict
import abc

import numpy as np

from .base import EngineBase


class ConditionerBase(EngineBase, metaclass=abc.ABCMeta):
    def __init__(self, *args, **kwargs):
        """
        filter some images based on some conditions, e.g. quality filtering,
        and set images to invalid

        Args:
            *args:
            **kwargs:
        """
        super().__init__(*args, **kwargs)

    @abc.abstractmethod
    def do(self, image: np.ndarray, **kwargs):
        """

        Args:
            image (np.ndarray): image array

        Raises：
            ImageQualityError
            ImageResolutionError
            ImageDistortionError
            ImageCategoryError

        """
        raise NotImplementedError


class SimpleConditioner(ConditionerBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do(self, image: np.ndarray, **kwargs) -> np.ndarray:
        """

        Args:
            image (np.ndarray): numpy ndarray of images, N * H * W * C

        Returns:
            ret_code (np.ndarray): return code

        """
        self.logger.info('Simple Conditioner')
        return np.zeros(image.shape[0])

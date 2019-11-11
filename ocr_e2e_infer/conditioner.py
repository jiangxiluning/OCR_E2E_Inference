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

import numpy as np
from nptyping import Array

from .base import EngineBase


class ConditionerBase(EngineBase):
    def __init__(self, *args, **kwargs):
        """
        filter some images based on some conditions, e.g. quality filtering,
        and set images to invalid

        Args:
            *args:
            **kwargs:
        """
        super().__init__(*args, **kwargs)

    def do(self, images: Array[int, ...]) -> np.ndarray:
        """

        Args:
            images (Array[int, ...]): numpy ndarray of images, N * H * W * C

        Returns:
            mask (np.ndarray): masked result, ndarray of N np.bool

        """
        raise NotImplementedError


class SimpleConditioner(ConditionerBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do(self, images: Array[int, ...]) -> np.ndarray:
        """

        Args:
            images (Array[int, ...]): numpy ndarray of images, N * H * W * C

        Returns:
            mask (np.ndarray): masked result, ndarray of N np.bool

        """
        self.logger.info('Simple Conditioner')
        return np.array(np.ones(images.shape[0]), dtype = bool)

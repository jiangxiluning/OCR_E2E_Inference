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
# @File : preprocessor.py
# @Email: jiangxiluning@gmail.com
# @Description: say something informative
from typing import Tuple

import numpy as np

from .base import EngineBase


class PreProcessorBase(EngineBase):
    '''
    do some pre-processing here, such as rotate, scale and other image
    transformations.
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do(self, images: np.ndarray, ret_codes: np.ndarray) \
            -> Tuple[np.ndarray, np.ndarray]:
        """


        Args:
            images (np.ndarray): image needs to preprocessed N*H*W*C
            ret_codes (np.ndarray): image mask, shape: (N,)

        Returns:
            images tuple (Tuple[np.ndarray, np.ndarray]): preprocessed images, shape: (N, H, W, C), image return codes, shape: (N,)

        """

        raise NotImplementedError


class SimplePreProcessor(PreProcessorBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do(self, images: np.ndarray, ret_codes: np.ndarray) -> \
            Tuple[np.ndarray, np.ndarray]:
        """
        Simple Preprocessor that return same images and mask

        Args:
            images (np.ndarray): image needs to preprocessed N*H*W*C
            ret_codes (np.ndarray): image mask, shape: (N,)

        Returns:
            images tuple (Tuple[np.ndarray, np.ndarray]): preprocessed images, shape: (N, H, W, C), image return codes, shape: (N,)

        """
        self.logger.info("Simple PreProcessor.")
        return images, ret_codes

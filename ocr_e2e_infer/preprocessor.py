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
import abc

import numpy as np

from .base import EngineBase


class PreProcessorBase(EngineBase, metaclass=abc.ABCMeta):
    '''
    do some pre-processing here, such as rotate, scale and other image
    transformations.
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @abc.abstractmethod
    def do(self, image: np.ndarray, **kwargs) \
            -> np.ndarray:
        """


        Args:
            image (np.ndarray): image needs to preprocessed H*W*C

        Returns:
            image (np.ndarray): preprocessed image

        """

        raise NotImplementedError


class SimplePreProcessor(PreProcessorBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do(self, image: np.ndarray, **kwargs) -> \
            np.ndarray:
        """
        Simple Preprocessor that return same images and mask

        Args:
            image (np.ndarray): image needs to preprocessed H*W*C

        Returns:
            image (np.ndarray): preprocessed image

        """
        self.logger.info("Simple PreProcessor.")
        return image

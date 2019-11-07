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
import numpy

from .base import EngineBase


class PreProcessorBase(EngineBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do(self, image:numpy.ndarray) -> numpy.ndarray:
        '''

        Args:
            image: image needs to preprocessed

        Returns:
            image (numpy.ndarray) preprocessed image

        '''

        raise NotImplementedError


class SimplePreProcessor(PreProcessorBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do(self, image:numpy.ndarray) -> numpy.ndarray:
        '''

        Args:
            image:

        Returns:

        '''
        self.logger.info("Simple PreProcessor.")
        return image

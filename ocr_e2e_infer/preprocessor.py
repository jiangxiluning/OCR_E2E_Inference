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
from typing import List, Dict

import numpy as np

from .base import EngineBase


class PreProcessorBase(EngineBase):
    '''
    do some pre-processing here, such as rotate, scale and other image transformations.
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do(self, images:List[Dict]) -> List[Dict]:
        '''

        Args:
            image: image needs to preprocessed N*H*W*C

        Returns:
            image (numpy.ndarray) preprocessed image

        '''

        raise NotImplementedError

class SimplePreProcessor(PreProcessorBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do(self, images:List[Dict]) -> List[Dict]:
        '''

        Args:
            image:

        Returns:

        '''
        self.logger.info("Simple PreProcessor.")
        return images

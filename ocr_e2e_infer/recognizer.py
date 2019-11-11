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
# @Time : 2019/11/7 15:37 
# @Author : Lu Ning 
# @File : recognizer
# @Email: jiangxiluning@gmail.com
# @Description: say something informative
from typing import List, Tuple

import numpy as np
from nptyping import Array


from .base import EngineBase


class RecoginizerBase(EngineBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do(self, images: Array[int, ...],
           mask: Array[bool, ...],
           boxes: List[Array[float, ..., 9]]) -> List[List[Tuple[str, float]]]:
        """
        Recognize text from text regions
        Args:
            boxes (List[np.ndarray]): list of boxex with confidence
            images: image needs to preprocessed N*H*W*C
            mask: image mask, shape: (N,)

        Returns:
            transcripts (List[List[str]]): transcript and confidence
            corresponding to each region of each image
        """
        raise NotImplementedError

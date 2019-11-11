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
# @Time : 2019/11/7 21:57
# @Author : Lu Ning 
# @File : postprocessor.py
# @Email: jiangxiluning@gmail.com
# @Description: say something informative
from typing import List, Dict, Tuple, Any

from nptyping import Array
import numpy as np

from .base import EngineBase


class PostProcessorBase(EngineBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do(self, images: Array[int, ...],
           mask: Array[bool, ...],
           boxes: List[Array[float, ..., 9]],
           transcripts: List[List[Tuple[str, float]]]) -> List[Dict[str, Any]]:
        """
        structurize images into keywords outputs and refine the results
        according to some rules

        Args:
            transcripts (List[List[str]]): transcript anc confidence corresponding to each region of each image
            boxes (List[np.ndarray]): list of boxex with confidence
            images (Array[int, ...]): image needs to preprocessed N*H*W*C
            mask (Array[bool, ...]): image mask, shape: (N,)

        Returns:
            results (List[Dict[str, Any]): structurized output
        """
        raise NotImplementedError
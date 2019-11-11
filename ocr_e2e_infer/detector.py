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
# @File : detector
# @Email: jiangxiluning@gmail.com
# @Description: say something informative
from typing import List, Dict
from nptyping import Array
from numpy import np

from .base import EngineBase


class DetectorBase(EngineBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do(self, images: Array[int, ...], mask: Array[bool, ...]) -> \
            List[np.ndarray]:
        """
        Detect chars, words or text lines
        Args:
            images: image needs to preprocessed N*H*W*C
            mask: image mask, shape: (N,)

        Returns:
            boxes (List[np.ndarray]): list of boxex with confidence
        """
        raise NotImplementedError

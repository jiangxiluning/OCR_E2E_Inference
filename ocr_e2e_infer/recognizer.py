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
from abc import ABCMeta, abstractmethod

import numpy as np


from .base import EngineBase


class RecoginizerBase(EngineBase, metaclass=ABCMeta):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @abstractmethod
    def do(self, image: np.ndarray, boxes: np.ndarray) -> List[Tuple[str, float]]:
        """
        Recognize text from text regions

        Args:
            image:
            boxes (np.ndarray): list of boxex with confidence

        Returns:
            transcripts (List[Tuple[str, float]]): transcript and confidence corresponding to each region of each image
        """
        raise NotImplementedError

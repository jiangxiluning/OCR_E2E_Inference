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
from typing import List, Dict, Tuple


from abc import ABCMeta, abstractmethod

from numpy import np

from .base import EngineBase


class DetectorBase(EngineBase, metaclass=ABCMeta):

    def __init__(self, *args, **kwargs):
        """

        Args:
            *args:
            **kwargs:
        """
        super().__init__(*args, **kwargs)

    @abstractmethod
    def do(self, image: np.ndarray) -> np.ndarray:
        """
        Detect chars, words or text lines

        Args:
            image (np.ndarray): image needs to preprocessed H*W*C

        Returns:
            boxes (np.ndarray): boxex with confidence
        """
        raise NotImplementedError

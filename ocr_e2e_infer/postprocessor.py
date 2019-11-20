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
import abc

import numpy as np

from .base import EngineBase


class PostProcessorBase(EngineBase, metaclass=abc.ABCMeta):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @abc.abstractmethod
    def do(self, image: np.ndarray,
           boxes: np.ndarray,
           transcripts: List[Tuple[str, float]],
           **kwargs) -> Dict[str, Tuple[Any, float]]:
        """
        structurize images into keywords outputs and refine the results
        according to some rules

        Args:
            transcripts (List[Tuple[str, float]]): transcript anc confidence corresponding to each region of each image
            boxes (np.ndarray): list of boxex with confidence
            image (np.ndarray): image needs to preprocessed N*H*W*C

        Returns:
            results (Dict[str, Tuple[Any, float]]): structurized output
        """
        raise NotImplementedError
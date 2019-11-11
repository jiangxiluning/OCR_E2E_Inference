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
# @Time : 2019/11/7 15:36 
# @Author : Lu Ning 
# @File : engine
# @Email: jiangxiluning@gmail.com
# @Description: say something informative
from typing import List, Dict, Any

import numpy as np
from nptyping import Array

from .base import EngineBase


class OCRE2ESystemBase(EngineBase):
    """
    This is an OCR end to end inferencer
    """

    def __init__(self,
                 detector,
                 recognizer,
                 config,
                 conditioner=None,
                 preprocessor=None,
                 postprocessor=None,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.detector = detector
        self.recognizer = recognizer
        self.config = config
        self.conditioner = conditioner
        self.preprocessor = preprocessor
        self.postprocessor = postprocessor

    def do(self, images: List[Array[int, ...]]) -> List[Dict[str, Any]]:
        """

        Args:
            images (List[Array[int, ...]]): list of images,

        Returns:
            results (List[Dict[str, Any]): structurized output,
            len(images) == len(reuslts)

        """
        raise NotImplementedError


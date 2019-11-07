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
from typing import List
from typing import Tuple

import numpy as np

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

    def infer(self):
        pass


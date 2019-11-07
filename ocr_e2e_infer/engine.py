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

class OCRE2ESystemBase(object):
    """
    This is an OCR end to end inferencer
    """

    def __init__(self):
        """

        """
        pass

    def test(self, aaa: Tuple[str, str]):
        """

        Args:
            aaa (tuple(str,str):
        """
        pass


    def pre_processing(self, images: List[np.ndarray]) -> list:
        """

        Args:
            images (list(numpy)): list of images

        Returns:
            list: images after preprocessing
        """
        pass


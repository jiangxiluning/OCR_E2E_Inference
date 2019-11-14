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
# @Time : 2019/11/14 11:50 
# @Author : Lu Ning 
# @File : e2e.py
# @Email: jiangxiluning@gmail.com
# @Description: say something informative
import abc
from typing import List, Dict, Any

import numpy as np

from .base import EngineBase


class End2EndBase(EngineBase, metaclass=abc.ABCMeta):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @abc.abstractmethod
    def do(self, image: np.ndarray) -> Dict[str, Any]:
        """

        Args:
            image:

        Returns:
            results (Dict[str, Any]):  results {'code': 0, 'reg': list, 'det': list}

        """
        raise NotImplementedError

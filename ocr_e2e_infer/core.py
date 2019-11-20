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
# @Time : 2019/11/12 14:32 
# @Author : Lu Ning 
# @File : core.py
# @Email: jiangxiluning@gmail.com
# @Description: say something informative
from typing import List, Dict, Any

from .detector import DetectorBase
from .recognizer import RecoginizerBase
from .base import EngineBase
from .e2e import End2EndBase
from . import errors

import numpy as np


class Core(EngineBase):

    def __init__(self, detector: DetectorBase = None,
                 recognizer: RecoginizerBase = None,
                 e2e_model: End2EndBase = None,
                 e2e: bool = False,
                 *args, **kwargs):
        """

        Args:
            detector:
            recognizer:
            e2e_model:
            e2e:
        """
        super().__init__(*args, **kwargs)
        self.e2e = e2e

        if self.e2e:
            assert (e2e_model is not None)
            self.e2e_model = e2e_model
        else:
            assert detector
            assert recognizer
            assert isinstance(detector, DetectorBase)
            assert isinstance(recognizer, RecoginizerBase)
            self.detector = detector
            self.recognizer = recognizer

    def do(self, image: np.ndarray, **kwargs) -> Dict[str, Any]:
        """

        Args:
            image (np.ndarray): image

        Returns:
            ocr results

        """
        if self.e2e:
            return self.e2e_model.do(image)
        else:
            det_result = self.detector.do(image)
            reg_result = self.recognizer.do(image, det_result)
            return {'det': det_result, 'reg': reg_result, 'code': 0}



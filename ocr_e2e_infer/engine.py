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
from typing import List, Dict, Any, NoReturn

import numpy as np

from .base import EngineBase
from .detector import DetectorBase
from .conditioner import ConditionerBase
from .preprocessor import PreProcessorBase
from .postprocessor import PostProcessorBase
from .recognizer import RecoginizerBase


class OCRE2ESystemBase(EngineBase):
    """
    This is an OCR end to end inferencer framework
    """

    def __init__(self,
                 detector: DetectorBase,
                 recognizer: RecoginizerBase,
                 config,
                 conditioner: ConditionerBase = None,
                 preprocessor: PreProcessorBase = None,
                 postprocessor: PostProcessorBase = None,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)

        assert isinstance(detector, DetectorBase)
        assert isinstance(recognizer, RecoginizerBase)
        assert isinstance(conditioner, ConditionerBase)
        assert isinstance(preprocessor, PreProcessorBase)
        assert isinstance(postprocessor, PostProcessorBase)

        self.detector = detector
        self.recognizer = recognizer
        self.config = config
        self.conditioner = conditioner
        self.preprocessor = preprocessor
        self.postprocessor = postprocessor

    def do(self, image: np.ndarray) -> Dict[str, Any]:
        """

        Args:
            images (List[Array[int, ...]]): list of images,

        Returns:
            results (List[Dict[str, Any]): structurized output,
            len(images) == len(reuslts)

        """
        #images, mask = self.conditioner.do()

        raise NotImplementedError

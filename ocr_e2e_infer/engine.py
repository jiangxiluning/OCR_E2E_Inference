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
from . import utils
from . import errors


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

    def do(self, image: bytes) -> Dict[str, Any]:
        """

        Args:
            image (bytes): base64 representation of image,

        Returns:
            results (List[Dict[str, Any]): structurized output,
            len(images) == len(reuslts)

        """
        ret = {'code': 0, 'result': ''}
        try:
            img = utils.read_image_from_base64(image)
        except errors.ImageReadingError as e:
            self.logger.exception(e.args)
            ret['code'] = e.code
            return ret

        try:
            self.conditioner.do(img)
        except (errors.ImageQualityError,
                errors.ImageCategoryError,
                errors.ImageDistortionError,
                errors.ImageResolutionError) as e:
            self.logger.exception(e.args)
            self.logger.exception(e.args)
            ret['code'] = e.code
            return ret


        #images, mask = self.conditioner.do()

        raise NotImplementedError

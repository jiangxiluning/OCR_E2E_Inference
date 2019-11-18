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
from .e2e import End2EndBase
from .core import Core
from . import utils
from . import errors


class OCRE2ESystemBase(EngineBase):
    """
    This is an OCR end to end inferencer framework
    """

    def __init__(self,
                 detector: DetectorBase = None,
                 recognizer: RecoginizerBase = None,
                 e2e: bool = False,
                 e2e_model: End2EndBase = None,
                 conditioner: ConditionerBase = None,
                 preprocessor: PreProcessorBase = None,
                 postprocessor: PostProcessorBase = None,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)

        assert isinstance(conditioner, ConditionerBase)
        assert isinstance(preprocessor, PreProcessorBase)
        assert isinstance(postprocessor, PostProcessorBase)

        self.core = Core(detector, recognizer, e2e_model, e2e)
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

        if self.conditioner:
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

        if self.preprocessor:
            try:
                img = self.preprocessor.do(img)
            except errors.ImagePreprocessingError as e:
                self.logger.exception(e.args)
                ret['code'] = e.code
                return ret
        try:
            ocr_ret = self.core.do(img)
        except (errors.InsufficentGPUMemoryError,
                errors.OCRDetectionError,
                errors.OCRRecognitionError,
                errors.OCRE2EError) as e:
            self.logger.exception(e.args)
            ret['code'] = e.code
            return ret

        try:
            ret['result'] = self.postprocessor.do(img,
                                                  boxes=ocr_ret['det'],
                                                  transcripts=ocr_ret['reg'])
        except errors.ImagePostprocessingError as e:
            self.logger.exception(e.args)
            ret['code'] = e.code
            return ret

        return ret






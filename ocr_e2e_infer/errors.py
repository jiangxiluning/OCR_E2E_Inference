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
# @Time : 2019/11/10 23:44 
# @Author : Lu Ning 
# @File : errors.py
# @Email: jiangxiluning@gmail.com
# @Description: say something informative


class InternalError(Exception):
    """
    BaseError or Internal Error, should never use this Error if you can figure
    out the error type
    """
    code = 99999
    pass


class ImageQualityError(Exception):
    """
    Image's quality is too low, often the quality score is judged by some image
    quality evaluation algorithm.
    """
    code = 10001
    pass


class ImageResolutionError(Exception):
    """
    Image's resolution is lower than threshold.
    """
    code = 10002
    pass


class ImageDistortionError(Exception):
    """
    Error due to distortion problem.
    """
    code = 10003
    pass


class ImageCategoryError(Exception):
    """
    Image category is wrong.
    """
    code = 10005
    pass


class ImageReadingError(Exception):
    """
    Image is corrupted and connot be open.
    """
    code = 10006
    pass


class OCRDetectionError(Exception):
    """
    Error occurs in the detection phrase of OCR system
    """
    code = 10008
    pass


class OCRRecognitionError(Exception):
    """
    Error occurs in the Recognition phrase of OCR system
    """
    code = 10009
    pass


class OCRE2EError(Exception):
    """
    Error occurs in the E2E phrase of OCR system.
    """
    code = 10011
    pass


class InsufficentGPUMemoryError(Exception):
    """
    GPU Memory is insufficient.
    """
    code = 10012
    pass


class ImagePreprocessingError(Exception):
    """
    Error occurs in pre-processing, e.g. rotation, scaling, denosing
    """
    code = 10013
    pass


class ImagePostprocessingError(Exception):
    """
    Error occurs in post-processing
    """
    code = 10014
    pass

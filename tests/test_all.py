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
# @Time : 2019/11/7 22:31 
# @Author : Lu Ning 
# @File : test_all.py
# @Email: jiangxiluning@gmail.com
# @Description: say something informative

import pytest
import numpy as np
import cv2
import base64
import sys
import os


from ocr_e2e_infer.base import EngineBase
from ocr_e2e_infer.preprocessor import SimplePreProcessor
from ocr_e2e_infer import utils

class TestAll:

    def test_logger(self):
        class1 = EngineBase()
        class2 = EngineBase()

        class1.logger.info('class1')
        class2.logger.info('class2')
        class1.logger.debug('debug')
        class1.logger.error('error')
        class2.logger.warn('warning')

        assert id(class1.logger) == id(class2.logger)

    def test_preprocessor(self):
        simple = SimplePreProcessor()
        image = np.random.randn(3,3,3)
        np.testing.assert_array_equal(image, simple.do(image))

    def test_image_read(self):
        #print(os.getcwd())
        image_path = 'test.png'

        image_orignal = cv2.imread(image_path, cv2.IMREAD_COLOR)

        with open(image_path, 'rb') as f:
            b = f.read()
        b64 = base64.b64encode(b)

        image_read = utils.read_image_from_base64(b64)
        np.testing.assert_array_equal(image_orignal, image_read)
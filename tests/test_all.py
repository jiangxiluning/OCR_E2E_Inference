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

from ocr_e2e_infer.base import EngineBase
from ocr_e2e_infer.preprocessor import SimplePreProcessor


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
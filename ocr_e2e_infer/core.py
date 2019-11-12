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
from multiprocessing import Process
from multiprocessing import Queue
from typing import Optional

from .detector import DetectorBase
from .recognizer import RecoginizerBase


class Core(object):

    def __init__(self, detector: DetectorBase,
                 recognizer: RecoginizerBase,
                 queue_size: Optional[int]=100):
        assert isinstance(detector, DetectorBase)
        assert isinstance(recognizer, RecoginizerBase)

        self.detector = detector
        self.recognizer = recognizer

        self.queue = Queue(maxsize=queue_size)

        self.reg_process = Process(name='')

    def setup(self):
        pass
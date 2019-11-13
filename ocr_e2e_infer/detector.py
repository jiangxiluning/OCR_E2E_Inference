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
# @Time : 2019/11/7 15:37 
# @Author : Lu Ning 
# @File : detector
# @Email: jiangxiluning@gmail.com
# @Description: say something informative
from typing import List, Dict, Tuple
from multiprocessing import Queue, Process
import time
from abc import ABCMeta

from nptyping import Array
from numpy import np

from .base import EngineBase
from . import errors


class DetectorBase(EngineBase, metaclass=ABCMeta):

    def __init__(self,
                 input_queue: Queue,
                 inner_queue: Queue,
                 batch_size: int = 8,
                 *args, **kwargs):
        """

        Args:
            input_queue:
            inner_queue:
            *args:
            **kwargs:
        """
        super().__init__(*args, **kwargs)

        self.input_queue = input_queue
        self.inner_queue = inner_queue
        self.__process = Process(self.__run,
                                 args=(),
                                 name='Process-Detector',
                                 daemon=True)

        self.batch_size = batch_size
        self.buffer = []

    def do(self, images: np.ndarray, ret_codes: np.ndarray) -> \
            List[np.ndarray]:
        """
        Detect chars, words or text lines

        Args:
            images (np.ndarray): image needs to preprocessed N*H*W*C
            ret_codes (np.ndarray): image mask, shape: (N,)

        Returns:
            boxes (List[np.ndarray]): list of boxex with confidence
        """
        raise NotImplementedError

    def __run(self):

        while True:
            if not self.input_queue.empty():
                data: Tuple[np.ndarray, int] = \
                    self.input_queue.get()

                self.logger.debug('Data is feteched from input queue.')

                self.buffer.append(data)

                if len(self.buffer) == self.batch_size:
                    self.logger.info('Buffer is full. Codes: {}'.format(
                        [d[1] for d in self.buffer]
                    ))

                    images = np.concatenate([d[0] for d in self.buffer])
                    ret_codes = np.array([d[1] for d in self.buffer], dtype=np.int)

                    try:
                        result: List[np.ndarray] = self.do(images, ret_codes)
                        self.logger.info('Detection is finished.')
                    except errors.OCRDetectionError as e:
                        ret_codes = np.array([e.code] * len(ret_codes), dtype=np.int)
                        self.logger.exception(e.args)

                    for _data, _result in zip(data, result):
                        self.inner_queue.put((_data[0], ret_codes, _result))
                    self.logger.info('Enqueue {} results into inner queue'.format(len(result)))
            else:
                self.logger.debug('Input queue is empty, sleep 0.5s.')
                time.sleep(0.5)

    def start(self):
        self.__process.start()
        self.logger.info("Detector is started.")

    def kill(self):
        self.__process.kill()
        self.logger.info("Detector is killed.")

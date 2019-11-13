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
# @File : recognizer
# @Email: jiangxiluning@gmail.com
# @Description: say something informative
from typing import List, Tuple
from multiprocessing import Process, Queue
from abc import ABCMeta
import time

import numpy as np
from nptyping import Array


from .base import EngineBase
from . import utils


class RecoginizerBase(EngineBase, metaclass=ABCMeta):

    def __init__(self,
                 inner_queue: Queue,
                 output_queue: Queue,
                 batch_size: int = 32,
                 *args, **kwargs):
        """

        :param inner_queue:
        :param output_queue:
        :param batch_size:
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)

        self.inner_queue = inner_queue
        self.output_queue = output_queue
        self.batch_size = batch_size
        self.buffer = []
        self.__process = Process(name='Process-Recognizer',
                                 target=self.__run,
                                 args=(),
                                 daemon=True)

    def do(self, images: np.ndarray,
           ret_codes: np.ndarray,
           boxes: List[np.ndarray]) -> List[List[Tuple[str, float]]]:
        """
        Recognize text from text regions

        Args:
            boxes (List[np.ndarray]): list of boxex with confidence
            images (Array[int, ...]): image needs to preprocessed N*H*W*C
            ret_codes (Array[bool, ...]): image mask, shape: (N,)

        Returns:
            transcripts (List[List[Tuple[str, float]]]): transcript and confidence corresponding to each region of each image
        """
        raise NotImplementedError

    def __run(self):
        while True:
            if not self.inner_queue.empty():
                data: Tuple[np.ndarray, int, np.ndarray] = \
                    self.inner_queue.get()

                self.logger.debug('Data is feteched from inner queue.')



                self.buffer.append(data)





                if len(self.buffer) == self.batch_size:
                    self.logger.info('Buffer is full. codes: {}'.format(
                        [d[1] for d in self.buffer]
                    ))

                    images = np.concatenate([d[0] for d in self.buffer])
                    mask = np.array([d[1] for d in self.buffer], dtype=np.bool)
                    boxes = [d[2] for d in self.buffer]

                    result: List[List[Tuple[str, float]]] = self.do(images, mask, boxes)
                    self.logger('Detection is finished.')
                    for _data, _result in zip(data, result):
                        self.inner_queue.put((_data[0], _data[1], _result))
                    self.logger('Enqueue {} results into inner queue'.format(len(result)))
            else:
                self.logger.debug('Input queue is empty, sleep 0.5s.')
                time.sleep(0.5)

    def __patch_generator(self,
                          image: np.ndarray,
                          ret_code: int,
                          rects: np.ndarray):

        N, _ = rects.shape

        for i in range(N):
            box = rects[i]
            yield utils.crop_patch(image, box)


    def start(self):
        self.__process.start()
        self.logger.info("Detector is started.")

    def kill(self):
        self.__process.kill()
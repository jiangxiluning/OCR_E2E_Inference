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
# @Time : 2019/11/7 21:57
# @Author : Lu Ning 
# @File : postprocessor.py
# @Email: jiangxiluning@gmail.com
# @Description: say something informative
from typing import List, Dict

from .base import EngineBase


class PostProcessorBase(EngineBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do(self, images:List[Dict]) -> List[Dict]:
        '''
        structurize images into keywords outputs and do some refinement work
        Args:
            images: images with recognition results
            {'image': ndarray, 'valid':True,
            'det': [[x1,y1,x2,y2, ...,x4,y4], ],
            'reg': ['text', 'text',..., '']}

        Returns:
            {'image': ndarray, 'valid':True,
            'det': [[x1,y1,x2,y2, ...,x4,y4], ],
            'reg': ['text', 'text',..., '',
            'keywords:':
            {
                'xxx': 'xxx',
                ...
            }]}
        '''
        raise NotImplementedError
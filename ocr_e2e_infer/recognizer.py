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
from typing import List, Dict

from .base import EngineBase


class RecoginizerBase(EngineBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do(self, images:List[Dict]) -> List[Dict]:
        '''

        Args:
            images: {'image': ndarray, 'valid':True, 'det': [x1,y1,x2,y2, ...,x4,y4]}

        Returns:
            {'image': ndarray, 'valid':True,
            'det': [[x1,y1,x2,y2, ...,x4,y4], ],
            'reg': ['text', 'text',..., '']}

        '''
        raise NotImplementedError

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
# @Time : 2019/11/7 22:06 
# @Author : Lu Ning 
# @File : base.py
# @Email: jiangxiluning@gmail.com
# @Description: say something informative
import logging


class EngineBase(object):
    logger = None

    def __init__(self, *args, **kwargs):

        if EngineBase.logger is None:
            EngineBase.logger = self.__setup_logger("OCR_End2End_Inference")
        self.logger = EngineBase.logger

    def __setup_logger(self, logger_name: str) -> logging.Logger:
        """
        Get default logger and use default configurations to setup it.

        Args:
            logger_name (str): logger's name
        Returns:
            logger (logging.Logger): logger
        """
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # create formatter
        formatter = logging.Formatter('%(asctime)s %(name)s %(processName)s %(levelname)s: %(message)s')

        # add formatter to ch
        ch.setFormatter(formatter)

        # add ch to logger
        logger.addHandler(ch)

        return logger

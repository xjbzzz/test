#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
日志模块，负责SDK的日志记录
"""

import os
import logging
from logging.handlers import RotatingFileHandler

from cmp_fusioncloud_sdk.constant import LOG_LEVELS, DEFAULT_CONFIG


class Logger:
    """
    日志记录器类
    """
    
    def __init__(self, name="cmp_fusioncloud_sdk", 
                 level=None, 
                 log_file=None, 
                 max_bytes=None, 
                 backup_count=None):
        """
        初始化日志记录器
        
        Args:
            name (str): 日志记录器名称
            level (str): 日志级别
            log_file (str): 日志文件路径
            max_bytes (int): 日志文件最大大小
            backup_count (int): 备份文件数量
        """
        self.name = name
        self.level = level or DEFAULT_CONFIG["log_level"]
        self.log_file = log_file or DEFAULT_CONFIG["log_file"]
        self.max_bytes = max_bytes or DEFAULT_CONFIG["max_log_file_size"]
        self.backup_count = backup_count or DEFAULT_CONFIG["backup_count"]
        
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(LOG_LEVELS.get(self.level, logging.INFO))
        self._setup_handlers()
    
    def _setup_handlers(self):
        """设置日志处理器"""
        # 清除已有的处理器
        if self.logger.handlers:
            self.logger.handlers = []
        
        # 配置控制台输出
        console_handler = logging.StreamHandler()
        console_handler.setLevel(self.logger.level)
        console_format = logging.Formatter(
            '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        )
        console_handler.setFormatter(console_format)
        self.logger.addHandler(console_handler)
        
        # 配置文件输出
        try:
            # 确保日志目录存在
            log_dir = os.path.dirname(self.log_file)
            if log_dir and not os.path.exists(log_dir):
                os.makedirs(log_dir)
                
            file_handler = RotatingFileHandler(
                self.log_file,
                maxBytes=self.max_bytes,
                backupCount=self.backup_count,
                encoding='utf-8'
            )
            file_handler.setLevel(self.logger.level)
            file_format = logging.Formatter(
                '%(asctime)s [%(levelname)s] %(name)s (%(filename)s:%(lineno)d): %(message)s'
            )
            file_handler.setFormatter(file_format)
            self.logger.addHandler(file_handler)
        except Exception as e:
            self.logger.warning(f"无法配置文件日志: {str(e)}")
    
    def debug(self, msg, *args, **kwargs):
        """记录调试信息"""
        self.logger.debug(msg, *args, **kwargs)
    
    def info(self, msg, *args, **kwargs):
        """记录信息"""
        self.logger.info(msg, *args, **kwargs)
    
    def warning(self, msg, *args, **kwargs):
        """记录警告"""
        self.logger.warning(msg, *args, **kwargs)
    
    def error(self, msg, *args, **kwargs):
        """记录错误"""
        self.logger.error(msg, *args, **kwargs)
    
    def critical(self, msg, *args, **kwargs):
        """记录严重错误"""
        self.logger.critical(msg, *args, **kwargs)


# 默认日志记录器
default_logger = Logger()


def get_logger(name=None):
    """
    获取或创建一个日志记录器
    
    Args:
        name (str): 日志记录器名称
    
    Returns:
        Logger: 日志记录器实例
    """
    if not name:
        return default_logger
    
    return Logger(name)
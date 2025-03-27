#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
常量定义模块
"""

# API相关常量
API_VERSION = "v1"
DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3

# 资源类型常量
RESOURCE_TYPES = {
    "VM": "virtual_machine",
    "STORAGE": "block_storage",
    "NETWORK": "network",
    "IMAGE": "image",
    "FLAVOR": "flavor",
    "REGION": "region",
    "ZONE": "zone",
    "VPC": "vpc",
    "SUBNET": "subnet",
    "SECURITY_GROUP": "security_group",
    "OSS": "object_storage"
}

# 状态常量
STATUS = {
    "ACTIVE": "active",
    "BUILDING": "building",
    "ERROR": "error",
    "DELETED": "deleted",
    "PAUSED": "paused",
    "SUSPENDED": "suspended"
}

# 日志级别
LOG_LEVELS = {
    "DEBUG": 10,
    "INFO": 20,
    "WARNING": 30,
    "ERROR": 40,
    "CRITICAL": 50
}

# 默认配置
DEFAULT_CONFIG = {
    "log_level": "INFO",
    "log_file": "cmp_sdk.log",
    "max_log_file_size": 10 * 1024 * 1024,  # 10MB
    "backup_count": 5
}
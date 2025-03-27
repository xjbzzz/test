# CMP Fusion Cloud SDK项目

## 项目介绍

这是一个用于华为云Fusion Cloud平台的SDK封装库。该SDK提供了简化的API调用方式，使开发者能够轻松管理和操作华为云资源。

## 目录结构

- `cmp_fusioncloud_sdk/` - SDK核心代码目录
  - `__init__.py` - 包初始化文件
  - `constant.py` - 常量定义
  - `log.py` - 日志处理
  - `cmp_sdk_base/` - 基础资源管理模块
  - `resource_format/` - 资源格式化模块

## 安装方法

```bash
pip install -r requirements.txt
python setup.py install
```

## 使用示例

```python
from cmp_fusioncloud_sdk import CmpFusionCloudSDK

# 初始化SDK
sdk = CmpFusionCloudSDK(
    endpoint="https://api.example.com",
    username="your_username",
    password="your_password"
)

# 获取云主机列表
vms = sdk.cloud_host.list()
for vm in vms:
    print(f"云主机: {vm.name}, 状态: {vm.status}")
```

## 许可证

私有软件，未经许可不得使用。
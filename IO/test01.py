import platform
import os

# 获取系统信息(跨平台兼容)
system_info = {
    'system': platform.system(),      # 操作系统名称
    'node': platform.node(),          # 计算机名称
    'release': platform.release(),    # 系统版本
    'version': platform.version(),    # 系统详细信息
    'machine': platform.machine(),    # 机器类型
    'processor': platform.processor(), # 处理器信息
    'invalidate_caches': platform.invalidate_caches(),
}

print("系统信息:")
for key, value in system_info.items():
    print(f"{key}: {value}")

print(os.environ.get('PATH'))
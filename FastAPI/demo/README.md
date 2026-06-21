```bash

uv --version

## 如果没有
curl -LsSf https://astral.sh/uv/install.sh | sh

# 创建 .venv 虚拟环境
uv venv


## 启动
uv run uvicorn main:app --reload
```
import test10

print('test11 模块被执行了 ', __name__)

print('test10 模块的name: ', test10.__name__)
print('test10 author : ', test10.__author__)

test10.say()

'''
第三方组件安装
# Linux/macOS
pip3 install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

# Windows cmd/PowerShell
pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple


pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
# 之后再装uv、所有包都会走国内高速
pip3 install uv


uv init
uv add pillow # Pillow 是 Python 中最著名、最强大的图像处理库。

'''
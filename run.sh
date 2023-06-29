###
 # @Author: SpenserCai
 # @Date: 2023-06-29 10:22:22
 # @version: 
 # @LastEditors: SpenserCai
 # @LastEditTime: 2023-06-29 16:07:40
 # @Description: file content
### 

PYTHON_COMMAND=python3.10
# 判断是否存在venv目录，如果不存在则使用命令创建
VENV_PATH=venv
if [ ! -d $VENV_PATH ]; then
    $PYTHON_COMMAND -m venv $VENV_PATH
fi

# 激活虚拟环境
source $VENV_PATH/bin/activate

# 执行代码
$PYTHON_COMMAND OpenCvWebRunner.py
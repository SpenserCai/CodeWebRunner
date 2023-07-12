'''
Author: SpenserCai
Date: 2023-06-29 14:35:43
version: 
LastEditors: SpenserCai
LastEditTime: 2023-07-12 17:00:09
Description: file content
'''
import cv2
import numpy as np

class CodeExecutor:
    def __init__(self, code: str, argvs: dict):
        self.argvs = argvs
        # 将传入的代码插入到 Script 函数中
        script_code = (
            "def Script(" + ", ".join(argvs.keys()) + "):\n" +
            "\n".join(" " + line for line in code.split("\n"))
        )
        local_vars = {}
        # 使用 exec() 函数使 Script 函数在类中生效
        exec(script_code, globals(), local_vars)
        setattr(self, "Script", local_vars["Script"])

    def run(self, argvs: dict = None):
        returnData = {
            "code": 200,
            "msg": "success",
            "data": None
        }
        if argvs is None:
            argvs = self.argvs
        # 统一捕获异常
        result = self.Script(**argvs)
        try:
            # 调用 Script 函数
            result = self.Script(**argvs)
        # 如果出现异常，返回异常信息
        except Exception as e:
            # 打印报错堆栈
            print(e)
            returnData["code"] = -1
            returnData["msg"] = str(e)
            return returnData
        # 判断返回值是否是dict，如果不是，报错
        if not isinstance(result, dict):
            returnData["code"] = -1
            returnData["msg"] = "The return value of the Script function must be a dict"
            return returnData
        returnData["data"] = result
        return returnData
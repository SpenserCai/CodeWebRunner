'''
Author: SpenserCai
Date: 2023-06-29 13:52:38
version: 
LastEditors: SpenserCai
LastEditTime: 2023-07-12 16:49:41
Description: file content
'''
from fastapi import APIRouter
from .request_model import RequestData
from .response_model import ResponseData, RunResponse
from app.Service.CodeRunnerService import CodeExecutor


router = APIRouter()

@router.post("/run", response_model=RunResponse)
def run(input_data: RequestData):
    cExecutor = CodeExecutor(input_data.code, input_data.argv)
    result = cExecutor.run()
    print(result)
    if result["code"] != 200:
        return RunResponse(code=result["code"], msg=result["msg"], data={})
    else:
        return RunResponse(code=200, msg="success", data=result["data"])
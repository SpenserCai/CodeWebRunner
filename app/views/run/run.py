'''
Author: SpenserCai
Date: 2023-06-29 13:52:38
version: 
LastEditors: SpenserCai
LastEditTime: 2023-06-29 17:21:21
Description: file content
'''
from fastapi import APIRouter
from .request_model import RequestData
from .response_model import ResponseData, RunResponse
from app.Service.OpenCvService import CodeExecutor


router = APIRouter()

@router.post("/run", response_model=RunResponse)
async def run_endpoint(input_data: RequestData):
    cExecutor = CodeExecutor(input_data.code, input_data.argv)
    result = cExecutor.run()
    if result["code"] != 200:
        return RunResponse(code=result["code"], msg=result["msg"], data=None)
    else:
        return RunResponse(code=200, msg="success", data=result["data"])
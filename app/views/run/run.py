'''
Author: SpenserCai
Date: 2023-06-29 13:52:38
version: 
LastEditors: SpenserCai
LastEditTime: 2023-06-29 14:19:09
Description: file content
'''
from fastapi import APIRouter
from .request_model import RequestData
from .response_model import ResponseData, RunResponse

router = APIRouter()

@router.post("/run", response_model=RunResponse)
async def run_endpoint(input_data: RequestData):
    # 你的实现逻辑
    result = {"output": "example output"}
    return result
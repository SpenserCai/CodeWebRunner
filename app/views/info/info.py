'''
Author: SpenserCai
Date: 2023-06-29 13:52:38
version: 
LastEditors: SpenserCai
LastEditTime: 2023-07-12 16:58:38
Description: file content
'''
from fastapi import APIRouter
from .request_model import RequestData
from .response_model import ResponseData, RunResponse
from app.Service.CodeRunnerService import CodeExecutor


router = APIRouter()

@router.post("/info", response_model=RunResponse)
def info(input_data: RequestData):
    return RunResponse(code=200, msg="success", data={})
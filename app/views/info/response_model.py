'''
Author: SpenserCai
Date: 2023-06-29 13:53:20
version: 
LastEditors: SpenserCai
LastEditTime: 2023-07-03 11:26:42
Description: file content
'''
from pydantic import BaseModel
from app.views.base_response import BaseResponse

class ResponseData(BaseModel):
    pass

class RunResponse(BaseResponse):
    pass
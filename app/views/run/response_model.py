'''
Author: SpenserCai
Date: 2023-06-29 13:53:20
version: 
LastEditors: SpenserCai
LastEditTime: 2023-06-29 14:18:26
Description: file content
'''
from pydantic import BaseModel
from app.views.base_response import BaseResponse, DataT
from typing import Dict, Any

class ResponseData(BaseModel):
    pass

class RunResponse(BaseResponse[Dict[str,Any]]):
    pass
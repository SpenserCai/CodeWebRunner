'''
Author: SpenserCai
Date: 2023-06-29 14:09:39
version: 
LastEditors: SpenserCai
LastEditTime: 2023-07-03 11:26:00
Description: file content
'''
from pydantic import BaseModel
from typing import Dict

class BaseResponse(BaseModel):
    code: int
    msg: str
    data: Dict
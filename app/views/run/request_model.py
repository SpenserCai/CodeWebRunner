'''
Author: SpenserCai
Date: 2023-06-29 13:53:06
version: 
LastEditors: SpenserCai
LastEditTime: 2023-06-29 17:06:47
Description: file content
'''
from pydantic import BaseModel
from typing import Dict

class RequestData(BaseModel):
    argv: Dict
    code: str
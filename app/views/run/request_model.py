'''
Author: SpenserCai
Date: 2023-06-29 13:53:06
version: 
LastEditors: SpenserCai
LastEditTime: 2023-06-29 14:04:44
Description: file content
'''
from pydantic import BaseModel
from typing import Dict, Any

class RequestData(BaseModel):
    argv: Dict[str, Any]
    code: str
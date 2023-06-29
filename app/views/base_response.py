'''
Author: SpenserCai
Date: 2023-06-29 14:09:39
version: 
LastEditors: SpenserCai
LastEditTime: 2023-06-29 14:10:31
Description: file content
'''
from pydantic import BaseModel
from typing import TypeVar, Generic

DataT = TypeVar("DataT")

class BaseResponse(BaseModel, Generic[DataT]):
    code: int
    msg: str
    data: DataT
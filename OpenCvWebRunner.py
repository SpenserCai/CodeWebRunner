'''
Author: SpenserCai
Date: 2023-06-29 10:26:45
version: 
LastEditors: SpenserCai
LastEditTime: 2023-06-29 16:50:34
Description: file content
'''
import uvicorn
from app.main import create_app

app = create_app()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=18000, reload=False)
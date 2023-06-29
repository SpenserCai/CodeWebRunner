'''
Author: SpenserCai
Date: 2023-06-29 13:39:13
version: 
LastEditors: SpenserCai
LastEditTime: 2023-06-29 16:12:05
Description: file content
'''
import importlib
import pkgutil
from fastapi import FastAPI
from app import views

def create_app():
    app = FastAPI()

    def register_routers():
        package = views
        prefix = package.__name__ + "."
        for _, module_name, _ in pkgutil.walk_packages(path=package.__path__, prefix=prefix):
            module = importlib.import_module(module_name)
            if hasattr(module, 'router'):
                app.include_router(module.router, prefix="/api", tags=[module_name.split(".")[-2]])

    register_routers()

    return app
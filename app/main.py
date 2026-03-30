from fastapi import FastAPI
from app.controller import UserController as UserController

app = FastAPI(title='Embarque-já', version='0.0.1')

app.include_router(UserController.router, prefix='/api/v1')

from fastapi import FastAPI
from controller import UserController
from app.database.session import engine
from app.database.session import Base

app = FastAPI(title='Embarque-já', version='0.0.1')

app.include_router(UserController.router, prefix='/api/v1')
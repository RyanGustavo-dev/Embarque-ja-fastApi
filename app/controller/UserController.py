from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from database.session import get_db
from schemas.UserSchema import UserResponse, UserBase
from service import UserService

router = APIRouter(
    prefix='/users',
    tags=['Users']
)

@router.get('/', response_model=List[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    return UserService.getAllUsers(db)

@router.post('/', response_model=UserResponse, 
    status_code=status.HTTP_201_CREATED)
def post_user(data=UserBase,db: Session = Depends(get_db)):
    return UserService.create_user(db, data)
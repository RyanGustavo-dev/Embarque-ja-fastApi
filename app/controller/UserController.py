from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.database.session import get_db
from app.schemas.UserSchema import UserBase, UserResponse
from app.service import UserService

router = APIRouter(
    prefix='/users',
    tags=['Users']
)

@router.get('/', response_model=List[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    return UserService.getAllUsers(db)

@router.post('/', response_model=UserResponse, 
    status_code=status.HTTP_201_CREATED)
def post_user(data: UserBase, db: Session = Depends(get_db)):
    return UserService.create_user(db, data)

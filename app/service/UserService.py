from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.model.UserModel import UserModel
from app.schemas.UserSchema import UserResponse, UserBase, UserUpdate

def getAllUsers(db: Session) -> UserModel:
    user = db.query(UserModel).all()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Usuario não encontrado'
        )
    return user

def create_user(db:Session , data: UserBase) -> UserModel:
    exist = db.query(UserModel.email == data.email).first()
    if exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Email já cadastrado'
        )
    user = UserModel(
        email=data.email,
        name=data.name,
        telefone=data.telefone,
        url_imagem=data.url_imagem,
        logo_sidebar=data.logo_sidebar,
        biografia=data.biografia
    )
    db.add(user)
    db.commit()
    db.refresh
    return user
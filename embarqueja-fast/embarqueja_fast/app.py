from http import HTTPStatus

from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.orm import Session

from embarqueja_fast.database import get_session
from embarqueja_fast.Models import User
from embarqueja_fast.schema import UserList, UserPublic, UserSchema
from embarqueja_fast.security import (
    create_access_token,
    get_current_user,
    get_password_hash,
    verify_password,
)

app = FastAPI()


@app.post('/users', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema, session=Depends(get_session)):

    dbUser = session.scalar(
        select(User).where(
            (User.name == user.name) | (User.email == user.email)
        )
    )

    if dbUser:
        if dbUser.name == user.name:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Username already exist',
            )
        elif dbUser.email == user.email:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Username already exist',
            )

    newDb = User(
        name=user.name,
        email=user.email,
        password=get_password_hash(user.password),
    )

    session.add(newDb)
    session.commit()
    session.refresh(newDb)

    return newDb


@app.get('/users', status_code=HTTPStatus.OK, response_model=UserList)
def get_all(
    limit: int = 10, skip: int = 0, session: Session = Depends(get_session)
):

    users = session.scalars(select(User).limit(limit).offset(skip))
    return {'users': users}


@app.put(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
@app.delete(
    '/users/{user_id}',
    status_code=HTTPStatus.OK,
    response_model=UserPublic,
    current_user=Depends(get_current_user),
)
def delete_user(user_id: int, session: Session = Depends(get_session)):
    dbUser = session.scalar(select(User).where(User.id == user_id))

    if not dbUser:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    session.delete(dbUser)
    session.commit()

    return {'message': 'User deleted'}


@app.post('/tolken')
def login_for_acess_tolken(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session),
):
    user = session.scalar(select(User).where(User.email == form_data.username))
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=400, detail='Incorrect email or password'
        )

    access_token = create_access_token(data={'sub': user.email})

    return {'access_token': access_token, 'token_type': 'Bearer'}


@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(
    user_id: int,
    user: UserSchema,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    if current_user.id != user_id:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN, detail='Not enough permissions'
        )

    current_user.username = user.name
    current_user.password = get_password_hash(user.password)
    current_user.email = user.email

    session.commit()
    session.refresh(current_user)

    return current_user

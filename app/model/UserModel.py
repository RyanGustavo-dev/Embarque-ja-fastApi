from sqlalchemy import Column, Integer, String, Boolean, DateTime, func, Text
from base.BaseModels import ModelBase


class UserModel(ModelBase):

    __tablename__ = 'users'

    name = Column(String(), nullable=False)
    email = Column(String(), nullable=False)
    telefone = Column(String())
    url_imagem = Column(Text())
    logo_sidebar = Column(Text())
    biografia = Column(Text())

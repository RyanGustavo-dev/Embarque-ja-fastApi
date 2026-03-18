from sqlalchemy import Column, Integer, String,ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.dialects import postgresql
from base.BaseModels import ModelBase


class ClienteModel(ModelBase):
    
    __tablename__ = 'clientes'

    nome = Column(String(), nullable=False)
    rg = Column(String())
    cpf = Column(String(), nullable=False)
    email = Column(String(), unique=True)
    celular = Column(String())
    data_nascimento = Column(Date())

    endereco = relationship("EnderecoModel", back_populates="cliente", uselist=False)
    reserva = relationship("ReservaModel", back_populates="cliente")
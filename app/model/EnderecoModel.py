from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects import postgresql
from model.base.BaseModels import ModelBase

class EnderecoModel(ModelBase):

    __tablename__ = 'enderecos'

    logradouro = Column(String())
    bairro = Column(String())
    cidade = Column(String())
    cep = Column(String())
    regiao = Column(String())
    cliente_id = Column(postgresql.UUID, ForeignKey('public.clientes.id'), unique=True)
    cliente = relationship("ClienteModel", back_populates="endereco")

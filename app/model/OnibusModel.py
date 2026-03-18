from sqlalchemy import Column, Integer, String,ForeignKey,Enum, DECIMAL
from sqlalchemy.orm import relationship
from sqlalchemy.dialects import postgresql
from base.BaseModels import ModelBase
from AssociateTables import ExcursaoOnibusModel
class OnibusModel(ModelBase):

    __tablename__ = 'onibus'

    empresa = Column(String())
    modelo = Column(String())
    total_assentos = Column(Integer())

    excursao_onibus = relationship(ExcursaoOnibusModel, back_populates="onibus")
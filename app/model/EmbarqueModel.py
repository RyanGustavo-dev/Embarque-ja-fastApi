from sqlalchemy import Column, Integer, String,ForeignKey,Enum, TIME
from sqlalchemy.orm import relationship
from sqlalchemy.dialects import postgresql
from app.model.base.BaseModels import ModelBase
from app.model.AssociateTables import ExcursaoEmbarque

class EmbarqueModel(ModelBase):
    __tablename__ = "embarque"

    local_embarque = Column(String())
    horario_embarque = Column(TIME())

    excursao_embarque = relationship(ExcursaoEmbarque, back_populates="embarque")

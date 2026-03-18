from sqlalchemy import Column, Integer, String,ForeignKey,Enum, DECIMAL
from sqlalchemy.orm import relationship
from sqlalchemy.dialects import postgresql
from base.BaseModels import ModelBase, BaseNoId


class ExcursaoOnibusModel(ModelBase):
    __tablename__ = "excursao_onibus"

    onibus_id = Column(postgresql.UUID, ForeignKey("public.onibus.id"))
    excusao_id = Column(postgresql.UUID, ForeignKey("public.excusao.id"))

    onibus = relationship("OnibusModel", back_populates="excursao_onibus")
    excursao = relationship("ExcursaoModel", back_populates="excursao_onibus")

class ExcursaoEmbarque(BaseNoId):

    __tablename__ = "excursao_embarque"

    excusao_id = Column(postgresql.UUID, ForeignKey("public.excusao.id"))
    embarque_id = Column(postgresql.UUID, ForeignKey("public.embarque.id"))

    excursao = relationship("ExcursaoModel", back_populates="excursao_embarque")
    embarque = relationship("EmbarqueModel", back_populates="excursao_embarque")
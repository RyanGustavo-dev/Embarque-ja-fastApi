from sqlalchemy import Column, Integer, String,DECIMAL,Enum, DATE
from sqlalchemy.orm import relationship
from sqlalchemy.dialects import postgresql
from app.model.base.BaseModels import ModelBase
from app.model.enums.StatusViagem import StatusViagem
from app.model.AssociateTables import ExcursaoOnibusModel, ExcursaoEmbarque
class ExcursaoModel(ModelBase):
    __tablename__ = "excursao"

    hotel = Column(String())
    origem = Column(String())
    destino = Column(String())
    data_saida = Column(DATE())
    data_retorno = Column(DATE())
    status_viagem = Column(Enum(StatusViagem))
    preco = Column(DECIMAL(10,2))

    excursao_onibus = relationship(ExcursaoOnibusModel, back_populates="excursao")
    excursao_embarque = relationship(ExcursaoEmbarque, back_populates="excursao")

from sqlalchemy import Column, Integer, String,ForeignKey,Enum, DECIMAL
from sqlalchemy.orm import relationship
from sqlalchemy.dialects import postgresql
from app.model.base.BaseModels import ModelBase
from app.model.enums.StatusAssento import StatusAssento


class ReservaModel(ModelBase):
    __tablename__ = "reservas"

    status_assento = Column(Enum(StatusAssento))
    numero_assento = Column(Integer())
    excursao_onibus_id = Column(postgresql.UUID, ForeignKey('public.excursao_onibus.id'))
    cliente_id = Column(postgresql.UUID, ForeignKey('public.clientes.id'))
    valor_pago = Column(DECIMAL(10, 2))

    cliente = relationship("ClienteModel", back_populates="reserva")

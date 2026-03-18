from sqlalchemy import Column, Integer, String, Boolean, DateTime, func, text
from sqlalchemy.dialects import postgresql
from datetime import datetime
from database.session import Base

class ModelBase(Base):
    __abstract__ = True
    __table_args__ = {"schema":"public"}

    id = Column(
        postgresql.UUID(as_uuid=True),
        server_default=text("uuid_generate_v4()"),
        primary_key=True
    )
    created_at = Column(DateTime(timezone=False),default=datetime.now)
    updated_at = Column(DateTime(timezone=False),default=datetime.now, onupdate=datetime.now)
    deleted_at = Column(DateTime(timezone=False))

class BaseNoId(Base):
    __abstract__ = True
    __table_args__ = {"schema":"public"}

    created_at = Column(DateTime(timezone=False),default=datetime.now)
    updated_at = Column(DateTime(timezone=False),default=datetime.now, onupdate=datetime.now)
    deleted_at = Column(DateTime(timezone=False))
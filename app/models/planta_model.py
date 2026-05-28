
from sqlalchemy import Column, Integer, String
from app.database.connection import Base

class Planta(Base):
    __tablename__ = "plantas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    tipo = Column(String, nullable=False)
    ubicacion = Column(String, nullable=False)
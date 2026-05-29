
from sqlalchemy import Column, Integer, String
from app.database.connection import Base

class Planta(Base):
    __tablename__ = "plantas"

    id = Column(Integer, primary_key=True, index=True)

    nombre = Column(String, nullable=False)

    nombre_cientifico = Column(String, nullable=False)

    color = Column(String, nullable=False)

    descripcion = Column(String, nullable=False)

    url_img = Column(String, nullable=False)
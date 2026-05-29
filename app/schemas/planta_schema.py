
from pydantic import BaseModel

class PlantaBase(BaseModel):
    nombre: str
    nombre_cientifico: str
    color: str
    descripcion: str
    url_img: str

class PlantaCreate(PlantaBase):
    pass

class PlantaResponse(PlantaBase):
    id: int

    class Config:
        from_attributes = True
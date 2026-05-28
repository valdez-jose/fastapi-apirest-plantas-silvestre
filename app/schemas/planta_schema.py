
from pydantic import BaseModel

class PlantaBase(BaseModel):
    nombre: str
    tipo: str
    ubicacion: str

class PlantaCreate(PlantaBase):
    pass

class PlantaResponse(PlantaBase):
    id: int

    class Config:
        from_attributes = True
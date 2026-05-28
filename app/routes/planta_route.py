
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import SessionLocal
from app.schemas.planta_schema import (
    PlantaCreate,
    PlantaResponse
)

from app.services.planta_service import (
    obtener_plantas,
    crear_planta
)

router = APIRouter(
    prefix="/plantas",
    tags=["Plantas"]
)

# conexión DB
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

# GET
@router.get("/", response_model=list[PlantaResponse])
def listar_plantas(db: Session = Depends(get_db)):
    return obtener_plantas(db)

# POST
@router.post("/", response_model=PlantaResponse)
def agregar_planta(
    planta: PlantaCreate,
    db: Session = Depends(get_db)
):
    return crear_planta(db, planta)
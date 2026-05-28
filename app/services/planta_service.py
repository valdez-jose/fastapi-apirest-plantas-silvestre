
from sqlalchemy.orm import Session
from app.models.planta_model import Planta

def obtener_plantas(db: Session):
    return db.query(Planta).all()

def crear_planta(db: Session, datos):
    nueva_planta = Planta(
        nombre=datos.nombre,
        tipo=datos.tipo,
        ubicacion=datos.ubicacion
    )

    db.add(nueva_planta)
    db.commit()
    db.refresh(nueva_planta)

    return nueva_planta
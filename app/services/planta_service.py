
from sqlalchemy.orm import Session
from app.models.planta_model import Planta

def obtener_plantas(db: Session):
    return db.query(Planta).all()

# crear planta por datos
def crear_planta(db: Session, datos):

    nueva_planta = Planta(
        nombre=datos.nombre,
        nombre_cientifico=datos.nombre_cientifico,
        color=datos.color,
        descripcion=datos.descripcion,
        url_img=datos.url_img
    )

    db.add(nueva_planta)
    db.commit()
    db.refresh(nueva_planta)

    return nueva_planta

# eliminar planta por id
def eliminar_planta(db: Session, planta_id: int):

    planta = db.query(Planta).filter(
        Planta.id == planta_id
    ).first()

    if planta:

        db.delete(planta)
        db.commit()

        return {
            "mensaje": "Planta eliminada"
        }

    return {
        "mensaje": "Planta no encontrada"
    }

    # actualizar planta por id
def actualizar_planta(
    db: Session,
    planta_id: int,
    datos
):

    planta = db.query(Planta).filter(
        Planta.id == planta_id
    ).first()

    if planta:

        planta.nombre = datos.nombre
        planta.nombre_cientifico = datos.nombre_cientifico
        planta.color = datos.color
        planta.descripcion = datos.descripcion
        planta.url_img = datos.url_img

        db.commit()
        db.refresh(planta)

        return planta

    return {
        "mensaje": "Planta no encontrada"
    } 
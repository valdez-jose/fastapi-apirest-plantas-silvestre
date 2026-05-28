
from fastapi import FastAPI

from app.database.connection import engine
from app.models.planta_model import Planta
from app.routes.planta_route import router as planta_router
from app.database.connection import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Plantas Silvestres",
    version="1.0.0"
)

app.include_router(planta_router)

@app.get("/")
def home():
    return {
        "mensaje": "API de Plantas Silvestres"
    }


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.connection import engine
from app.models.planta_model import Planta
from app.routes.planta_route import router as planta_router
from app.database.connection import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Plantas Silvestres",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(planta_router)

@app.get("/")
def home():
    return {
        "mensaje": "API de Plantas Silvestres"
    }
    
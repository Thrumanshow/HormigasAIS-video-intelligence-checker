# backend/api.py

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

# Simulación de análisis IA de XOXO
def analizar_video_por_enlace(url: str) -> str:
    # Lógica de ejemplo simulada:
    if "deepfake" in url.lower():
        return "IA"
    else:
        return random.choice(["real", "IA"])  # Aquí irá el análisis real

# Definimos modelo de entrada
class VideoLink(BaseModel):
    url: str

# Inicializamos la app
app = FastAPI()

# Permitir solicitudes desde el frontend local o GitHub Pages
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Reemplaza por tu dominio en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analizar")
async def analizar_video(link: VideoLink):
    resultado = analizar_video_por_enlace(link.url)

    if resultado == "real":
        mensaje = "💡 Este video parece real. Actores y escenas naturales detectadas."
        color = "verde"
    else:
        mensaje = "💡 Este video muestra señales de haber sido generado por IA."
        color = "azul"

    return {
        "estado": resultado,
        "mensaje": mensaje,
        "color": color
      }

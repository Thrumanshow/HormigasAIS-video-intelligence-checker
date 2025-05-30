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

# from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://thrumanshow.github.io"],  # Reemplaza con tu dominio de frontend
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
# Esto es opcional en FastAPI, pero útil para desarrollo local
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)

# api.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

# Simulación básica de detección IA
def analizar_video_por_enlace(url: str) -> str:
    if "deepfake" in url.lower():
        return "IA"
    else:
        return random.choice(["real", "IA"])

# Modelo de datos
class VideoLink(BaseModel):
    url: str

# Inicializar app
app = FastAPI()

# CORS para permitir peticiones del frontend en GitHub Pages
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://thrumanshow.github.io"],  # Cambia si usás otro dominio
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

# Para desarrollo local
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)

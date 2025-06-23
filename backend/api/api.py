from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

app = FastAPI()

# Habilitar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://thrumanshow.github.io"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo de entrada
class VideoRequest(BaseModel):
    url: str

# Análisis simulado
@app.post("/analyze")
def analyze_video(req: VideoRequest):
    url = req.url

    # Lógica verosímil simple (placeholder)
    if "tiktok" in url or "shorts" in url:
        signal = "blue"  # IA generada
    elif "youtube" in url:
        signal = random.choice(["green", "blue"])
    else:
        signal = "green"

    return {"signal": signal}

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import datetime
import os
from adapter.core import XOXOCore  # Asegúrate de que este módulo exista

app = FastAPI()
core = XOXOCore()

class VideoAnalysis(BaseModel):
    video_id: str
    url: str
    mode: str
    robot_id: str

@app.get("/")
def read_root():
    return {
        "status": "ok",
        "agent": "XOXO",
        "ecosystem": "HormigasAIS",
        "mode": "LBH-M2M",
        "service": "video-intelligence-checker"
    }

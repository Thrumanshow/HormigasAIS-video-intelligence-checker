from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import datetime
import os

# Importamos tu nuevo motor LBH
from adapter.core import XOXOCore

app = FastAPI()
core = XOXOCore()

class VideoAnalysis(BaseModel):
    video_id: str
    url: str
    mode: str
    robot_id: str

@app.get("/")
def read_root():
    return {"status": "ok", "service": "HormigasAIS-LBH-Active"}

@app.post("/analyze")
async def analyze_video(data: VideoAnalysis):
    # 1. Generar el frame LBH usando el Adaptador
    lbh_frame = core.send_command({"video_id": data.video_id, "action": "analyze"})
    
    # 2. Guardar en la Caja Negra (logs_binarios)
    log_path = f"logs_binarios/{data.video_id}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.lbh"
    with open(log_path, "w") as f:
        f.write(lbh_frame)
    
    return {
        "signal": "green",
        "lbh_id": data.video_id,
        "log_saved": True
    }

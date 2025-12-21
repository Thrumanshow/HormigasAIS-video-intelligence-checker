from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import datetime
import os
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

@app.post("/analizar")
async def analizar_video(data: VideoAnalysis):
    try:
        # El motor procesa los datos y genera el binario .lbh
        resultado = core.send_command(data.dict())
        return {"status": "success", "data": resultado}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

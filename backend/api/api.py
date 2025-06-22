from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from center.logic import analyze_video
import uvicorn

app = FastAPI(
    title="XOXO Video Intelligence API",
    description="Microservicio de análisis de video para el ecosistema HormigasAIS.",
    version="0.1.0"
)

class VideoInput(BaseModel):
    url: str

@app.post("/analyze/")
async def analyze(input_data: VideoInput):
    try:
        result = analyze_video(input_data.url)
        return {"status": "success", "signal": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "XOXO AI backend está activo"}

# Solo se usa para pruebas locales
if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)

from fastapi import FastAPI

app = FastAPI(
    title="XOXO Backend API",
    version="0.1.0",
    description="Módulo de inteligencia backend del proyecto HormigasAIS"
)

@app.get("/")
async def root():
    return {"message": "¡XOXO backend en funcionamiento!"}

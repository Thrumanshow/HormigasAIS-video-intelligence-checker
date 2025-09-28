import os
import subprocess
import sys
import asyncio
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse

# ------------------------------
# 1️⃣ Ir al directorio backend
# ------------------------------
backend_dir = os.path.join(os.path.dirname(__file__))
os.chdir(backend_dir)
print(f"Ejecutando desde: {backend_dir}")

# ------------------------------
# 2️⃣ Instalar dependencias
# ------------------------------
req_file = "requirements.txt"

if os.path.exists(req_file):
    print(f"Instalando dependencias desde {req_file}...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", req_file])
    except subprocess.CalledProcessError:
        print("ERROR: No se pudieron instalar las dependencias")
        sys.exit(1)
else:
    print(f"ERROR: No se encontró {req_file}. Verifica el nombre y la ubicación.")
    sys.exit(1)

# ------------------------------
# 3️⃣ Leer variables de entorno desde .env
# ------------------------------
try:
    from dotenv import load_dotenv
    load_dotenv()
    print("Variables de entorno cargadas desde .env")
except ImportError:
    print("⚠️ No se encontró python-dotenv, continuando sin variables de entorno.")

# ------------------------------
# 4️⃣ Configurar FastAPI y funciones asíncronas
# ------------------------------
app = FastAPI()

async def analizar_video(video_id: str):
    print(f"[{asyncio.get_event_loop().time()}] Inicio del análisis: {video_id}")
    await asyncio.sleep(5)  # Simula análisis pesado
    print(f"[{asyncio.get_event_loop().time()}] Análisis terminado: {video_id}")
    return {"resultado": "Video validado", "video_id": video_id}

@app.get("/analizar/")
async def endpoint_analizar(videos: list[str] = Query(..., description="Lista de IDs de videos a analizar")):
    """
    Endpoint que recibe una lista de videos y los procesa en paralelo.
    Ejemplo: /analizar/?videos=video1&videos=video2
    """
    # Crear tareas para todos los videos
    tareas = [analizar_video(video_id) for video_id in videos]

    # Ejecutar todas las tareas en paralelo
    resultados = await asyncio.gather(*tareas)

    return JSONResponse(content={"resultados": resultados})

# ------------------------------
# 5️⃣ Levantar servidor Uvicorn
# ------------------------------
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    host = "0.0.0.0"

    print(f"Iniciando FastAPI en http://{host}:{port} ...")
    try:
        subprocess.check_call([
            sys.executable,
            "-m",
            "uvicorn",
            "run_backend:app",  # Apunta a este mismo archivo
            "--host",
            host,
            "--port",
            str(port),
            "--reload"
        ])
    except subprocess.CalledProcessError:
        print("❌ Error al iniciar el backend. Revisa si el puerto ya está en uso.")

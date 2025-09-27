import os
import subprocess
import sys

# ------------------------------
# 1️⃣ Instalar dependencias
# ------------------------------
req_file = "requirements.txt"

if os.path.exists(req_file):
    print(f"Instalando dependencias desde {req_file}...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", req_file])
else:
    print(f"ERROR: No se encontró {req_file}. Verifica el nombre y la ubicación.")
    sys.exit(1)

# ------------------------------
# 2️⃣ Leer variables de entorno desde .env
# ------------------------------
from dotenv import load_dotenv
load_dotenv()
print("Variables de entorno cargadas desde .env")

# ------------------------------
# 3️⃣ Ejecutar FastAPI
# ------------------------------
port = os.getenv("PORT", "8000")  # Si Render usa $PORT, lo tomará automáticamente
host = "0.0.0.0"

print(f"Iniciando FastAPI en http://{host}:{port} ...")
subprocess.check_call([
    sys.executable,
    "-m",
    "uvicorn",
    "api:app",
    "--host",
    host,
    "--port",
    port
])

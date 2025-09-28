import os
import subprocess
import sys

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
# 4️⃣ Configuración de FastAPI
# ------------------------------
port = os.getenv("PORT", "8000")
host = "0.0.0.0"

print(f"Iniciando FastAPI en http://{host}:{port} ...")

# ------------------------------
# 5️⃣ Levantar servidor Uvicorn
# ------------------------------
try:
    subprocess.check_call([
        sys.executable,
        "-m",
        "uvicorn",
        "api.api:app",   # <- ajustado a tu estructura backend/api/api.py
        "--host",
        host,
        "--port",
        port,
        "--reload"
    ])
except subprocess.CalledProcessError:
    print("❌ Error al iniciar el backend. Revisa si el puerto ya está en uso.")

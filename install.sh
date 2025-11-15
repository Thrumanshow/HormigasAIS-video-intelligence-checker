#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "=== HormigasAIS Installation ==="

###############################
# 1. Actualizar e instalar dependencias
###############################

pkg update -y
pkg upgrade -y

pkg install -y python git nodejs termux-services cloudflared

echo "[1/6] Dependencias instaladas."

###############################
# 2. Crear entorno virtual
###############################

cd backend

if [ ! -d "venv" ]; then
    python -m venv venv
    echo "[2/6] Entorno virtual creado."
else
    echo "[2/6] Entorno virtual ya existía."
fi

source venv/bin/activate

###############################
# 3. Instalar dependencias Python
###############################

pip install --upgrade pip
pip install -r requirements.txt

echo "[3/6] Requirements instalados."

###############################
# 4. Configurar servicios
###############################

cd ..
mkdir -p ~/.termux-services/hormigasais
mkdir -p ~/.termux-services/hormigasais-tunnel

# Servicio backend FastAPI
cat > ~/.termux-services/hormigasais/run << 'EOF'
#!/data/data/com.termux/files/usr/bin/sh
cd ~/HormigasAIS-video-intelligence-checker/backend
source venv/bin/activate
exec uvicorn main:app --host 0.0.0.0 --port 8000
EOF

chmod +x ~/.termux-services/hormigasais/run

# Servicio Cloudflare Tunnel
cat > ~/.termux-services/hormigasais-tunnel/run << 'EOF'
#!/data/data/com.termux/files/usr/bin/sh
exec cloudflared tunnel --url http://localhost:8000
EOF

chmod +x ~/.termux-services/hormigasais-tunnel/run

echo "[4/6] Servicios configurados."

###############################
# 5. Activar servicios
###############################

sv-enable hormigasais
sv-enable hormigasais-tunnel

echo "[5/6] Servicios activados."

###############################
# 6. Mostrar URL del túnel
###############################

sleep 4
echo "[6/6] Buscando URL del túnel..."
cloudflared tunnel list

echo "=== Instalación completa ==="

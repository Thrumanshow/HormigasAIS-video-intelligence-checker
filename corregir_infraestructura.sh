#!/usr/bin/env bash
# ============================================
# PROTOCOLO DE RESILIENCIA LBH - 2026
# Acción: Sincronizar Reloj y Abrir Puerto 8081
# ============================================

echo "🌍 Configurando Zona Horaria de la Colonia (El Salvador -> UTC)..."
# Ajuste de zona horaria para Termux
ln -sf /usr/share/zoneinfo/America/El_Salvador /data/data/com.termux/files/usr/etc/localtime

echo "🔌 Limpiando bloqueos en puerto 8081..."
# Matar procesos que quedaron colgados para liberar el socket
fuser -k 8081/tcp 2>/dev/null || pkill -f "python3 -m http.server 8081"

echo "🚀 Levantando Servidor Nodo-Escuela..."
cd ~/HormigasAIS-video-intelligence-checker/HormigasAIS-Nodo-Escuela
# Ejecución en segundo plano con salida a log de auditoría
nohup python3 -m http.server 8081 > server_status.log 2>&1 &

sleep 2
if ss -ltnp | grep -q 8081; then
    echo "✅ Puerto 8081 ACTIVADO y escuchando."
else
    echo "⚠️ El puerto sigue cerrado. Intentando método alternativo (0.0.0.0)..."
    python3 -m http.server --bind 0.0.0.0 8081 > server_status.log 2>&1 &
fi

echo "🕒 TIEMPO ACTUALIZADO:"
date
date -u

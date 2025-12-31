#!/bin/bash
# Script: enjambre_total_final.sh | Protocolo de Autocuración PTCC
# Fundador: Cristhiam Hernández | San Miguel, El Salvador

# --- CONFIGURACIÓN DE RUTAS ---
BACKUP_DIR="xoxo-lbh-adapter-BACKUP-2025-12-31"
ACTIVE_DIR="xoxo-lbh-adapter"
LOG_DIR="$ACTIVE_DIR/logs"
LOG_FILE="$LOG_DIR/enjambre_total.log"
EVOLUCION_FILE="$ACTIVE_DIR/Evolución-enjambre.md"
TIMESTAMP_UTC=$(date -u +"%Y%m%dT%H%M%SZ")

echo "🧪 [${TIMESTAMP_UTC}] Iniciando Protocolo de Autocuración..."

# 1. LIMPIEZA DE PROCESOS
pkill -9 python3 2>/dev/null
sleep 1

# 2. RESTAURACIÓN SOBERANA
if [ -d "$BACKUP_DIR" ]; then
    echo "🗑️ Eliminando versión activa inconsistente..."
    rm -rf "$ACTIVE_DIR"
    echo "📂 Restaurando desde ADN Limpio ($BACKUP_DIR)..."
    cp -r "$BACKUP_DIR" "$ACTIVE_DIR"
    
    # IMPORTANTE: Crear directorios de logs DESPUÉS de restaurar
    mkdir -p "$LOG_DIR"
    echo "✅ Estructura de logs reconstruida."
else
    echo "❌ ERROR CRÍTICO: No se encontró la Cámara de Criogenia ($BACKUP_DIR)"
    exit 1
fi

# 3. REINICIO DE SERVICIOS
echo "🏗️ Levantando sectores 8080 y 8081..."
cd "$ACTIVE_DIR"
nohup python3 -m http.server 8080 > /dev/null 2>&1 &
nohup python3 -m http.server 8081 > /dev/null 2>&1 &
sleep 3

# 4. VALIDACIÓN HTTP Y MEMORIA
if curl -s -I "localhost:8081" | grep -q "200 OK"; then
    echo "✅ Sector 8081: SOBERANO (HTTP 200 OK)"
    echo -e "\n### 🚀 Autocuración Exitosa: $TIMESTAMP_UTC\n- Nodo restaurado y validado vía HTTP." >> "Evolución-enjambre.md"
    echo "🎯 Memoria de la colonia actualizada en Evolución-enjambre.md"
else
    echo "⚠️ Error: El puerto 8081 no respondió tras la restauración."
fi

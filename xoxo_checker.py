#!/usr/bin/env python3
# xoxo_checker.py
import json
import os

print("🔹 INICIALIZANDO NÚCLEO XOXO")
print("✔ Cargando módulos registrados...")

modules_registry_path = "modules/modules_registry.json"
if os.path.exists(modules_registry_path):
    with open(modules_registry_path) as f:
        registry = json.load(f)
    print(f"✔ Módulos cargados: {[m['module'] for m in registry]}")
else:
    print("✖ No hay módulos registrados aún")

print("🔹 NÚCLEO XOXO LISTO - MODO GOVERNED / BLOCKED")

# adapter/core.py
import sys
import os

# Importaciones locales directas para evitar círculos
from .json_lbh import json_to_lbh, lbh_to_json

# Definición de la clase base si no existe externamente
class XOXOAdapter:
    def __init__(self, broker="localhost", robot_id="robot_default"):
        self.broker = broker
        self.robot_id = robot_id
        print(f"📡 Adapter inicializado para {robot_id} en {broker}")
    
    def loop_start(self): print("🔄 Loop iniciado")
    def loop_stop(self): print("🛑 Loop detenido")
    def publish_act(self, **kwargs): print(f"📤 Publicando: {kwargs}")

class XOXOCore:
    def __init__(self, broker="localhost", robot_id="robot_default"):
        self.adapter = XOXOAdapter(broker=broker, robot_id=robot_id)

    def start(self):
        self.adapter.loop_start()

    def stop(self):
        self.adapter.loop_stop()

    def send_command(self, payload: dict):
        lbh_frame = json_to_lbh(payload)
        self.adapter.publish_act(**payload)
        return lbh_frame

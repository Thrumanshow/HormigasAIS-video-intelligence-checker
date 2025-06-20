# backend/core/logic.py

from datetime import datetime

def analyze_video_link(video_url: str) -> dict:
    """
    Simula el análisis de un enlace de video.
    En producción, esta función será reemplazada por IA real.
    """
    # Simulación básica:
    result = {
        "video_url": video_url,
        "timestamp": datetime.utcnow().isoformat(),
        "status": "checked",
        "authenticity": "real" if "youtube" in video_url else "synthetic",
        "signal": "green" if "youtube" in video_url else "blue",
    }
    return result

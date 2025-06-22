def analyze_video(video_url: str) -> str:
    """
    Simula el análisis de un video y devuelve una señal de autenticidad.
    """

    # Lógica simplificada: usa palabras clave para inferir resultado
    if "ai" in video_url.lower() or "fake" in video_url.lower():
        return "azul"  # Probabilidad alta de manipulación por IA
    else:
        return "verde"  # Alta probabilidad de ser real

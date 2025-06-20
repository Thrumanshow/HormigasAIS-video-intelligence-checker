def analyze_video(video_url: str) -> str:
    """
    Lógica simulada para detectar si el video es real o generado por IA.
    """
    if "ai" in video_url.lower() or "deepfake" in video_url.lower():
        return "Azul"  # Probabilidad alta de ser generado por IA
    return "Verde"  # Probabilidad alta de ser real

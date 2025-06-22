# logic.py
# Lógica de evaluación de autenticidad del video

def evaluate_video(video_url: str) -> str:
    """
    Simula el análisis de un video y retorna su autenticidad.
    Retorna: 'real' o 'ai-generated'
    """
    if "deepfake" in video_url.lower():
        return "ai-generated"
    return "real"

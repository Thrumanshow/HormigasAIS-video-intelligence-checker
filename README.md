# 🧠 HormigasAIS Video Intelligence Checker

Un filtro digital creado por y para la comunidad **HormigasAIS**, con el propósito de detectar la autenticidad de los videos en línea y combatir la desinformación generada por contenidos sintéticos.

---

## 🌐 ¿Qué es esto?

Este proyecto es una herramienta web **minimalista** que permite a cualquier usuario pegar el enlace de un video (por ejemplo, de YouTube) y recibir una **señal visual** sobre su autenticidad:

- 💡 **Verde**: Video con alta probabilidad de ser real (actores reales, escenas naturales).
- 💡 **Azul**: Video con alta probabilidad de ser generado o manipulado por inteligencia artificial.

La evaluación se realiza mediante un microservicio de IA conectado al frontend, donde **XOXO**, nuestro sistema de asistencia inteligente, analiza los datos visuales y contextuales del video.

---

## 🧱 Estructura del proyecto

```bash
HormigasAIS-video-intelligence-checker/
├── index.html             # Interfaz pública y minimalista
├── README.md              # Este archivo
└── backend/               # Lógica del análisis con IA (XOXO)
    ├── api.py             # API inicial con FastAPI
    └── requirements.txt   # Dependencias del backend
---

 🚀 Cómo ejecutar el proyecto localmente 

1. Clona el repositorio 

git clone https://github.com/Thrumanshow/HormigasAIS-video-intelligence-checker.git cd HormigasAIS-video-intelligence-checker 

2. Ejecuta el backend 

Instala dependencias y ejecuta la API: 

cd backend pip install -r requirements.txt uvicorn api:app --reload 

La API estará corriendo en http://127.0.0.1:8000. 

3. Abre el frontend 

Abre el archivo index.html en tu navegador favorito (por ahora, no necesita servidor web). 

🛠️ Tecnologías utilizadas 

• HTML/CSS para la interfaz de usuario 

• FastAPI como framework para el backend 

• Python 3.9+ como lenguaje base 

• (Próximamente) integración con servicios de análisis visual por IA (OpenAI, DeepAI, u otros) 

📬 ¿Cómo colaborar? 

¡Las puertas del hormiguero están abiertas! 

• Sugiere mejoras abriendo un Issue 

• Envía un Pull Request con nuevas funciones o ideas 

• Comparte el proyecto y su propósito en tus redes 

🧠 Visión futura 

• Integración con APIs avanzadas de detección de deepfakes 

• Registro de estadísticas sobre tipos de videos 

• Versión extendida para verificar metadatos, thumbnails y subtítulos 

• Extensión para navegadores 

• Traducción a varios idiomas 

✨ Créditos 

Creado con inteligencia colaborativa por
Cristhiam Quiñonez – HormigasAIS
Inspirado en la frase: "La mente curiosa y la colaboración humana."

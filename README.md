# 🧠 HormigasAIS Video Intelligence Checker

Un filtro digital creado por y para la comunidad **HormigasAIS**, con el propósito de detectar la autenticidad de los videos en línea y combatir la desinformación generada por contenidos sintéticos.

---

## 🌐 ¿Qué es esto?

Este proyecto es una herramienta web **minimalista** que permite a cualquier usuario pegar el enlace de un video (por ejemplo, de YouTube) y recibir una **señal visual** sobre su autenticidad:

- 💡 **Verde**: Video con alta probabilidad de ser real (actores reales, escenas naturales).
- 💡 **Azul**: Video con alta probabilidad de haber sido generado o manipulado por inteligencia artificial.

La evaluación se realiza mediante un microservicio de IA llamado **XOXO**, que analiza datos visuales y contextuales del video en tiempo real. Todo esto corre sobre una arquitectura distribuida alojada en **Render**.

---

## 🧱 Estructura del proyecto

```bash
HormigasAIS-video-intelligence-checker/
├── index.html               # Interfaz pública y minimalista
├── README.md                # Este archivo
└── backend/                 # Lógica del análisis con IA (XOXO)
    ├── api.py               # API con FastAPI
    └── requirements.txt     # Dependencias del backend
---

## 🚀 Entorno en producción (Render) 

Los servicios desplegados actualmente son: 

1. 🧠 Backend IA - FastAPI 

• URL: https://hormigasais-video-intelligence-backend.onrender.com 

• Puerto: 8000 

• Framework: FastAPI 

• Región: Oregon 

---- 

## 2. ⚙️ Automatización Inteligente - n8n 

• URL: https://n8n-automation-xoxo.onrender.com 

• Función: Automatiza procesos conectados a GitHub y flujos IA de validación. 

• Docker: Sí, autoalojado con configuración personalizada. 

---- 

## 3. 🧩 Webhook GitHub Action 

• URL: https://webhook-github-action.onrender.com 

• Propósito: Escucha eventos en GitHub y los canaliza a flujos de n8n y backend. 

• Node.js Runtime 

--- 

## 🚀 Cómo ejecutar el proyecto localmente 

• Clona el repositorio: 

git clone https://github.com/Thrumanshow/HormigasAIS-video-intelligence-checker.git cd HormigasAIS-video-intelligence-checker 

• Ejecuta el backend: 

cd backend pip install -r requirements.txt uvicorn api:app --reload 

La API estará corriendo en: http://127.0.0.1:8000 

• Abre el frontend: 

Solo abre el archivo index.html en tu navegador. No necesita servidor para funcionar localmente. 

---- 

## 🛠️ Tecnologías utilizadas 

• HTML/CSS para la interfaz de usuario 

• FastAPI como framework para el backend 

• Python 3.9+ 

• Render.com para el despliegue 

• Docker (para n8n) 

• GitHub Actions + Webhook personalizado 

--- 

## 📬 ¿Cómo colaborar? 

¡Las puertas del hormiguero están abiertas! 

• Sugiere mejoras abriendo un Issue 

• Envía un Pull Request con nuevas funciones o ideas 

• Comparte el proyecto y su propósito en tus redes 

--- 

## 🧠 Visión futura 

• Integración con APIs de detección de deepfakes (OpenAI, DeepAI, etc.) 

• Registro y análisis estadístico de tipos de videos 

• Verificación de metadatos, thumbnails y subtítulos 

• Extensiones para navegadores 

• Traducción a varios idiomas 

• Integración con LenPT (HormigasAIS Language) 

--- 

✨ Créditos 

Creado con inteligencia colaborativa por:
Cristhiam Quiñonez – HormigasAIS
Inspirado en la frase: 

"La mente curiosa y la colaboración humana."

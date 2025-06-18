# 🧠 HormigasAIS Video Intelligence Checker

Un filtro digital creado por y para la comunidad **HormigasAIS**, con el propósito de detectar la autenticidad de los videos en línea y combatir la desinformación generada por contenidos sintéticos.

---

## 🌐 ¿Qué es esto?

Este proyecto es una herramienta web **minimalista** que permite a cualquier usuario pegar el enlace de un video (por ejemplo, de YouTube) y recibir una **señal visual** sobre su autenticidad:

- 💡 **Verde**: Video con alta probabilidad de ser real (actores reales, escenas naturales).
- 💡 **Azul**: Video con alta probabilidad de haber sido generado o manipulado por inteligencia artificial.

La evaluación se realiza mediante un microservicio de IA llamado **XOXO**, que analiza datos visuales y contextuales del video en tiempo real. Todo esto corre sobre una arquitectura distribuida desplegada en **Render**.

---

## 🧱 Estructura del proyecto

---

## 🚀 Servicios desplegados en producción (Render)

### 1. 🧠 `xoxo-ai-backend` (IA Backend)

- URL: https://xoxo-ai-backend.onrender.com
- Tipo: Web Service (Python)
- Puerto: 8000
- Framework: FastAPI
- Función: Analiza datos de videos y entrega señales de autenticidad.
- Región: Oregon

---

### 2. ⚙️ `n8n-automation-xoxo` (Automatización inteligente)

- URL: https://n8n-automation-xoxo.onrender.com
- Tipo: Web Service (Docker)
- Plataforma: n8n autoalojado
- Función: Orquestación de flujos inteligentes con eventos de GitHub y resultados IA.

---

### 3. 🧩 `webhook-github-action` (Escucha GitHub)

- URL: https://webhook-github-action.onrender.com
- Tipo: Web Service (Node.js)
- Función: Escucha cambios en GitHub y dispara eventos hacia n8n o FastAPI.
- Plan: Starter

---

## ⚙️ Ejecución local

```bash
# 1. Clona el repositorio
git clone https://github.com/Thrumanshow/HormigasAIS-video-intelligence-checker.git
cd HormigasAIS-video-intelligence-checker

# 2. Ejecuta el backend
cd backend
pip install -r requirements.txt
uvicorn api:app --reload

---

¿Te gustaría que lo subamos con un mensaje de commit tipo:  
`docs: actualización estratégica del README para Render v1.0`?

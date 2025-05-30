# 🧠 HormigasAIS Video Intelligence Checker

> Un filtro digital creado por y para la comunidad HormigasAIS, con el propósito de detectar la autenticidad de los videos en línea y combatir la desinformación generada por contenidos sintéticos.

---

## 🌐 ¿Qué es esto?

Este proyecto es una herramienta web minimalista que permite a cualquier usuario pegar el enlace de un video (por ejemplo de YouTube) y recibir una **señal visual** sobre su autenticidad:

- 💡 **Verde**: Video con alta probabilidad de ser real (actores reales, escenas naturales).
- 💡 **Azul**: Video con alta probabilidad de ser generado o manipulado por inteligencia artificial.

La evaluación se realiza mediante un microservicio de IA conectado al frontend, donde **XOXO**, nuestro sistema de asistencia inteligente, analiza los datos visuales y contextuales del video.

---

## 🧱 Estructura del proyecto

```bash
├── index.html          # Interfaz pública y minimalista
├── README.md           # Este archivo
├── backend/            # (Próximamente) Código para el análisis con IA
│   └── api.py          # API con Flask/FastAPI para procesar el enlace

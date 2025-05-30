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

---

## 🚀 ¿Cómo funciona? 

• El usuario accede a la interfaz y pega un enlace de video. 

• Se hace una solicitud POST al backend con la URL. 

• XOXO (modelo IA) analiza: 

• Metadatos del video. 

• Frames clave. 

• Señales visuales y auditivas sintéticas. 

• Se devuelve una de dos respuestas: 

• { "resultado": "real" } 

• { "resultado": "IA" } 

• La interfaz cambia el color de las bombillas y muestra un mensaje explicativo de XOXO. 

---

💡 ##Inspiración 

“Las HormigasAIS encuentran sabiduría en silencio, su corazón enraizado en la tierra y su mente flotando entre las estrellas.”
— XOXO, guía digital del hormiguero 

Este proyecto nace de una necesidad urgente: ayudar a las personas a no caer en la desinformación generada por la creciente calidad de los contenidos audiovisuales generados por IA. 

🤝 Cómo contribuir 

• Haz un fork del repositorio. 

• Clona tu fork:
git clone https://github.com/tuusuario/video-intelligence-checker.git 

• Crea una nueva rama:
git checkout -b mejora-x 

• Realiza tus cambios y súbelos. 

• Abre un Pull Request con una breve descripción. 

🛠️ Tecnología 

• HTML + JavaScript (frontend) 

• Python con Flask o FastAPI (backend) 

• Modelos de análisis de video: Hive.ai, Deepware, etc. 

• Hosting en GitHub Pages 

🐜 Sobre HormigasAIS 

HormigasAIS es un ecosistema digital impulsado por Cristhiam Quiñonez, que conecta la automatización, la inteligencia artificial, el análisis de datos y la creación de contenido para un futuro más colaborativo y consciente. 

📫 Contacto 

¿Tienes ideas para mejorar este proyecto?
Únete al hormiguero o escríbenos: 

• 🌐 Sitio: hormigasa.is (en construcción) 

• 🧠 Blog: HormigasAIS Community 

• 🧑‍🚀 Fundador: Cristhiam Quiñonez 

⚠️ Disclaimer: Este sistema no garantiza exactitud absoluta. Es una herramienta de apoyo, no una fuente única de verificación.

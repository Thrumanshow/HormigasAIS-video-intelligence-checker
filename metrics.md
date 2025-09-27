
# HormigasAIS Video Intelligence Checker - Métricas de Desempeño 

Este documento resume las métricas de rendimiento y operativas del servicio **HormigasAIS Video Intelligence Checker**, incluyendo información relevante para usuarios, sponsors y stakeholders técnicos. 

--- 

## 📊 Tabla de Métricas 

| Métrica                     | Descripción detallada                                                                 | Valor / Resultado |
|-------------------------------|--------------------------------------------------------------------------------------|-----------------|
| Tiempo de respuesta del backend | Incluye desde la recepción del video hasta la entrega de señal visual. Depende de la calidad y tamaño del video. | 1.2 s           |
| Precisión de detección AI      | Exactitud de XOXO en detectar videos manipulados. Valores reportados para videos de alta resolución (HD). | 95%             |
| Usuarios simultáneos soportados| Número de sesiones concurrentes sin degradación significativa del servicio.          | 50              |
| Tamaño promedio del video      | Video analizado promedio en la prueba de benchmark.                                  | 25 MB           |
| Uso de CPU backend             | Promedio de utilización de CPU durante carga normal.                                  | 40%             |
| Costo promedio por análisis    | Estimación de gasto por cada análisis de video considerando infraestructura actual.   | $0.05 / análisis|
| Consumo promedio de RAM        | Memoria utilizada por usuario durante la ejecución del análisis.                      | 150 MB          | 

--- 

## 📈 Gráficas de Desempeño 

- **Tiempo de respuesta vs Tamaño del video**  
  ![Gráfica Tiempo de Respuesta](./assets/tiempo_respuesta.png) 

- **Precisión de AI por tipo de video**  
  ![Gráfica Precisión](./assets/precision_ai.png) 

- **Uso de recursos (CPU/RAM) durante carga normal**  
  ![Gráfica Recursos](./assets/uso_recursos.png) 

> 🔹 Las gráficas son estáticas y representan los promedios del servicio durante pruebas controladas.  

--- 

## 🎬 Demo Visual para Sponsors 

- **Mira cómo funciona **HormigasAIS Video Intelligence Checker** en acción**
[![Demo HormigasAIS Video Intelligence Checker](https://img.youtube.com/vi/UzNPHj1PUXo/hqdefault.jpg)](https://youtube.com/shorts/UzNPHj1PUXo?feature=shared)

--- 

## 📝 Notas Adicionales 

- Los valores reportados son promedios calculados sobre un conjunto de **videos variados** (SD a HD).  
- Precisión de AI puede variar ligeramente según el tipo de contenido y resolución del video.  
- Costos operativos estimados basados en la infraestructura actual (Render + n8n + backend FastAPI).  
- Este documento sirve como referencia técnica y comercial para la evaluación del servicio. 

--- 

**Autor:** Cristhiam Quiñonez | HormigasAIS  
**Fecha:** 27 de septiembre de 2025

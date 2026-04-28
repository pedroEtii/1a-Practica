🚀 Tech News Sentiment Pipeline

Este proyecto es un pipeline de datos de extremo a extremo que extrae noticias sobre tecnología, las procesa, las almacena en SQL y analiza el sentimiento del mercado mediante IA.

## 🛠️ Tecnologías utilizadas
- **Lenguaje:** Python 3.12
- **Datos:** NewsAPI
- **Almacenamiento:** SQLite (SQL)
- **IA/ML:** TextBlob (NLP)
- **Arquitectura:** Pipeline orquestado

## 📈 Estructura del Proyecto
1. `extractor.py`: Ingesta de datos crudos.
2. `transformador.py`: Limpieza y filtrado.
3. `cargador_sql.py`: Persistencia en base de datos.
4. `sentimiento.py`: Análisis de sentimiento con IA.
5. `main_pipeline.py`: Orquestador central.

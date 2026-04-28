import json

def transformar_datos():
    print("🧹 Iniciando limpieza de datos...")
    
    # 1. Leer el archivo crudo
    try:
        with open('noticias_raw.json', 'r', encoding='utf-8') as f:
            articulos = json.load(f)
    except FileNotFoundError:
        print("❌ No se encontró el archivo noticias_raw.json. Ejecuta primero el extractor.")
        return

    noticias_limpias = []

    # 2. Proceso de transformación
    for art in articulos:
        # Solo guardamos si tiene descripción (importante para MLOps)
        if art.get('description') and art.get('title'):
            dato_limpio = {
                "titulo": art['title'],
                "fuente": art['source']['name'],
                "resumen": art['description'],
                "fecha": art['publishedAt'][:10] # Solo queremos el año-mes-día
            }
            noticias_limpias.append(dato_limpio)

    # 3. Guardar el resultado procesado
    with open('noticias_procesadas.json', 'w', encoding='utf-8') as f:
        json.dump(noticias_limpias, f, ensure_ascii=False, indent=4)
    
    print(f"✅ Limpieza completada. Pasamos de {len(articulos)} a {len(noticias_limpias)} noticias válidas.")
    print("💾 Archivo 'noticias_procesadas.json' creado.")

if __name__ == "__main__":
    transformar_datos()
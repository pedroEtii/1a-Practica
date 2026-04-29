import json
import os
import sys  # Importante para avisar al orquestador del error

def transformar_datos():
    print("🧹 Iniciando limpieza de datos...")
    
    # --- INICIO DE LA PARTE NUEVA / ROBUSTA ---
    # 1. Comprobamos si el archivo existe físicamente
    if not os.path.exists('noticias_raw.json'):
        print("❌ ERROR: El archivo noticias_raw.json no existe.")
        sys.exit(1) # Esto le dice al main_pipeline: "¡Para! Algo salió mal"

    # 2. Intentamos leer el archivo con seguridad
    try:
        with open('noticias_raw.json', 'r', encoding='utf-8') as f:
            articulos = json.load(f)
            
        if not articulos:
            print("⚠️ El archivo está vacío. No hay noticias para procesar.")
            sys.exit(1)
            
    except json.JSONDecodeError:
        print("❌ ERROR: El archivo JSON está corrupto.")
        sys.exit(1)

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
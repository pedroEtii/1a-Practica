import os
import requests
import json

# --- CONFIGURACIÓN ---
API_KEY = '468b69a763e442beb0ffdc2260371355'  # <--- Pega aquí tu llave
BUSQUEDA = 'artificial intelligence OR machine learning'

def extraer_noticias():
    url = f'https://newsapi.org/v2/everything?q={BUSQUEDA}&language=es&sortBy=publishedAt&apiKey={API_KEY}'
    
    print(f"🚀 Conectando con la API para buscar: {BUSQUEDA}...")
    respuesta = requests.get(url)
    
    if respuesta.status_code == 200:
        datos = respuesta.json()
        articulos = datos.get('articles', [])
        
        print(f"✅ ¡Éxito! Se han encontrado {len(articulos)} noticias recientes.\n")
        
        # Mostramos las 3 primeras para probar
        for i, noticia in enumerate(articulos[:3], 1):
            print(f"{i}. TITULO: {noticia['title']}")
            print(f"   FUENTE: {noticia['source']['name']}")
            print(f"   LINK: {noticia['url']}\n")
            
        # Guardamos todo en un JSON (Esto es ingeniería de datos básica: almacenamiento crudo)
        with open('noticias_raw.json', 'w', encoding='utf-8') as f:
            json.dump(articulos, f, ensure_ascii=False, indent=4)
        print("💾 Datos guardados en 'noticias_raw.json'")
        
    else:
        print(f"❌ Error: {respuesta.status_code}")

if __name__ == "__main__":
    extraer_noticias()
import sqlite3
from textblob import TextBlob

def analizar_sentimiento_mercado():
    print("🧠 La IA está analizando el sentimiento de tus noticias...")
    
    conexion = sqlite3.connect('tecnologia.db')
    cursor = conexion.cursor()
    
    # Sacamos los títulos de nuestra tabla SQL
    cursor.execute("SELECT titulo FROM noticias")
    filas = cursor.fetchall()
    
    positivas = 0
    negativas = 0
    total = len(filas)

    print(f"📊 Analizando {total} noticias...\n")

    for fila in filas:
        titulo = fila[0]
        # La IA analiza el texto (Nota: TextBlob funciona mejor en inglés, 
        # pero para este ejemplo detectará palabras clave globales)
        analisis = TextBlob(titulo)
        
        # Clasificamos
        if analisis.sentiment.polarity > 0:
            positivas += 1
        elif analisis.sentiment.polarity < 0:
            negativas += 1
            
    conexion.close()

    # Resultados finales
    print("--- RESULTADOS DEL ANALISTA IA ---")
    print(f"✅ Noticias Positivas: {positivas}")
    print(f"❌ Noticias Negativas: {negativas}")
    print(f"😐 Noticias Neutras: {total - (positivas + negativas)}")
    
    if positivas > negativas:
        print("\n🚀 CONCLUSIÓN: El mercado tech está OPTIMISTA hoy.")
    else:
        print("\n📉 CONCLUSIÓN: Hay CAUTELA o pesimismo en el sector.")

if __name__ == "__main__":
    analizar_sentimiento_mercado()
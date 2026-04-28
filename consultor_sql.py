import sqlite3

def consultar_noticias(palabra_clave):
    print(f"🔍 Buscando noticias sobre: '{palabra_clave}'...")
    
    # 1. Conectar a la base de datos
    conexion = sqlite3.connect('tecnologia.db')
    cursor = conexion.cursor()
    
    # 2. La consulta SQL (Query)
    # Buscamos en el título o en el resumen usando el operador LIKE
    query = "SELECT titulo, fuente FROM noticias WHERE titulo LIKE ? OR resumen LIKE ?"
    busqueda = f"%{palabra_clave}%"
    
    cursor.execute(query, (busqueda, busqueda))
    
    # 3. Obtener resultados
    resultados = cursor.fetchall()
    
    if resultados:
        print(f"✨ Se han encontrado {len(resultados)} noticias relacionadas:\n")
        for i, fila in enumerate(resultados, 1):
            print(f"{i}. [{fila[1]}] - {fila[0]}")
    else:
        print(f"🤷 No se encontró nada con la palabra '{palabra_clave}'.")
    
    conexion.close()

if __name__ == "__main__":
    # Prueba a cambiar 'OpenAI' por 'Google', 'Nvidia' o 'IA'
    tema = input("¿Qué tema quieres buscar en tu base de datos? ")
    consultar_noticias(tema)
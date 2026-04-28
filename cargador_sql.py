import json
import sqlite3

def cargar_en_sql():
    print("🗄️ Iniciando carga en base de datos SQL...")
    
    # 1. Conectar a la base de datos (se creará el archivo 'tecnologia.db')
    conexion = sqlite3.connect('tecnologia.db')
    cursor = conexion.cursor()
    
    # 2. Crear la tabla si no existe (Definir el "esquema")
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS noticias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            fuente TEXT,
            resumen TEXT,
            fecha TEXT
        )
    ''')
    
    # 3. Leer los datos limpios que generamos antes
    with open('noticias_procesadas.json', 'r', encoding='utf-8') as f:
        noticias = json.load(f)
    
    # 4. Insertar los datos en la tabla
    for n in noticias:
        cursor.execute('''
            INSERT INTO noticias (titulo, fuente, resumen, fecha)
            VALUES (?, ?, ?, ?)
        ''', (n['titulo'], n['fuente'], n['resumen'], n['fecha']))
    
    # 5. Guardar cambios y cerrar
    conexion.commit()
    conexion.close()
    
    print(f"✅ ¡Hecho! Se han insertado {len(noticias)} filas en 'tecnologia.db'.")

if __name__ == "__main__":
    cargar_en_sql()
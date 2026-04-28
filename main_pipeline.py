import subprocess
import time

def ejecutar_paso(nombre_paso, comando):
    print(f"\n--- 🏁 INICIANDO: {nombre_paso} ---")
    try:
        # Ejecutamos el script y esperamos a que termine
        resultado = subprocess.run(["python", comando], check=True)
        if resultado.returncode == 0:
            print(f"✅ {nombre_paso} completado con éxito.")
            return True
    except subprocess.CalledProcessError:
        print(f"❌ ERROR CRÍTICO en {nombre_paso}. El pipeline se ha detenido.")
        return False

def iniciar_sistema():
    print("🚀 INICIANDO PIPELINE AUTOMATIZADO DE NOTICIAS TECH 2026")
    print("==========================================================")
    inicio_total = time.time()

    # Definimos el flujo de trabajo (Workflow)
    pasos = [
        ("Extracción de Datos Crudos", "extractor.py"),
        ("Transformación y Limpieza", "transformador.py"),
        ("Carga en Base de Datos SQL", "cargador_sql.py"),
        ("Análisis de IA (Sentimiento)", "sentimiento.py")
    ]

    for nombre, script in pasos:
        exito = ejecutar_paso(nombre, script)
        if not exito:
            break
        time.sleep(1) # Una pequeña pausa para que sea legible en consola

    fin_total = time.time()
    print("\n==========================================================")
    print(f"🏆 PIPELINE FINALIZADO en {round(fin_total - inicio_total, 2)} segundos.")

if __name__ == "__main__":
    iniciar_sistema()
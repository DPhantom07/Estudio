import sys

def inicializar_pipeline(reporte_id: str, anio_str: str) -> None:
    """
    Simula el inicio de un flujo de limpieza de datos basado en parámetros de red.
    
    Argumentos:
        reporte_id (str): Identificador único del reporte analítico.
        anio_str (str): Año de recolección de datos (entra como texto).
    """
    # Convertimos el año a entero para realizar validaciones cronológicas
    anio_fiscal: int = int(anio_str)
    
    print("--- PIPELINE DE DATOS INICIALIZADO ---")
    print(f"Procesando Reporte: {reporte_id}")
    print(f"Año de Operación: {anio_fiscal} | Próxima Auditoría: {anio_fiscal + 1}")

if __name__ == "__main__":
    try:
        # Capturamos el ID del reporte y el Año desde la terminal
        id_ingresado: str = sys.argv[1]
        anio_ingresado: str = sys.argv[2]
        
        inicializar_pipeline(id_ingresado, anio_ingresado)
        
    except IndexError:
        print("[ERROR] Faltan parámetros. Formato requerido: <ID_REPORTE> <AÑO>")
    except ValueError:
        print("[ERROR] El segundo argumento (Año) debe ser un número entero válido.")
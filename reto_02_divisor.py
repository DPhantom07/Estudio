# Reto 02: Divisor de Datos Estructurados
# Objetivo: Leer un archivo CSV y separar sus columnas con .split()

def procesar_usuarios(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            # 1. Limpiar la línea con .strip()
            linea_limpia = linea.strip()
            
            # 2. Mañana romperemos la línea aquí usando .split(",")
            print(linea_limpia)

if __name__ == "__main__":
    archivo_csv = "datos_estructurados.txt"
    print("--- Estructura del Reto 02 Lista ---")
    procesar_usuarios(archivo_csv)
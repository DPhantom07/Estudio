# Reto 02: Divisor de Datos Estructurados
# Objetivo: Leer un archivo CSV y separar sus columnas con .split()

def procesar_usuarios(nombre_archivo):
    #abrir el archivo y leer y darle el alias archivo
    with open(nombre_archivo, "r") as archivo:
        #iterar el numero de linea que tiene archivo y guardar en linea
        for linea in archivo:
            #lista_limpia = linea sin espacios y separando la lista en cada ,
            linea_limpia = linea.strip().split(',')
            #imprime los primeros dos datos de la lista que esta en linea_limpia
            print(f'{linea_limpia[0]}-{linea_limpia[1]}')

if __name__ == "__main__":
    archivo_csv = "datos_estructurados.txt"
    print("--- Estructura del Reto 02 Lista ---")
    procesar_usuarios(archivo_csv)
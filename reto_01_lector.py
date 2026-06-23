# Reto 01: Lector de Datos Basico
# Objetivo: Aprender a leer un archivo de texto y contar sus lineas

def contar_lineas(nombre_del_archivo):
    contador = 0
    #leer el texto
    with open(nombre_del_archivo, 'r') as archivo:
        for linea in archivo:
            contador += 1
            print(linea.strip())
        print(f'Total de lineas en el archivo {contador}')

if __name__ == "__main__":
    archivo = "datos.txt"
    print('---Inicializando programa---')
    contar_lineas(archivo)

    
    
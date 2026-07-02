# Reto 04 Filtro especializado
# El departamento de seguridad del proyecto necesita generar un reporte exclusivo en la terminal.
# Tu mision es disenar un script que lea el archivo de datos, lo valide, pero solo muestre en pantalla a los usuarios de DEVELOPER

#Limpiar informacion
def leer_lineas(nombre_archivo):
    #abrir archivo
    with open(nombre_archivo, 'r') as archivo:
        #intero sobre las lineas
        for linea in archivo:
            #si en linea encuentro ','
            if "," in linea and len(linea.split(',')) >=2 :
                linea_limpia = linea.strip().split(',')
                if linea_limpia[1].lower() == 'developer':
                    #Imprime solo developer
                    print(f'[NUEVO DEV] Nombre: {linea_limpia[0]}')
    

archivo = 'datos_proyectos.txt'
print('procesando datos')
leer_lineas(archivo)

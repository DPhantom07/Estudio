# Reto 03 
# Implementar la lectura del nuevo archivo linea por linea.
# Anadir una capa de seguridad
# Si la linea es correcta imprime ('Usuario [Nombre] | Rol [Rol]')
# Si la linea esta tota, debe imprimir un mensaje de advertencia: "Alerta Registro corrupto ignorado"

def leer_lineas(nombre_archivo):
    #abrir archivo
    with open(nombre_archivo, 'r') as archivo:
        #intero sobre las lineas
        for linea in archivo:
            #si en linea encuentro ','
            if "," in linea:
                linea_limpia = linea.strip().split(',')
                print(f'Usuario {linea_limpia[0]} | Rol {linea_limpia[1]}')
            else:
                print('Alerta Registro corrupto ignorado')
    

archivo = 'datos_corruptos.txt'
print('procesando datos')
leer_lineas(archivo)

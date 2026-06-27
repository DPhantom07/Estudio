# Reto 07 Necesito que tu script me genere automaticamente un archivo llamado reporte_final.txt
#Transforma el codigo del censo para que, en lugar de imprimir los resultados en la terminal, los guarde fisicamente en un archivo nuevo.

def leer_documento(documento):
    roles = {}
    with open(documento, 'r') as archivo:
        for linea in archivo:
            if "," in linea and len(linea.split(',')) >= 3:
                # linea limpia linea_limpia[0]/usuario linea_limpia[1]/rol(key) 
                linea_limpia = linea.strip().split(',')
                if linea_limpia[1] not in roles:
                    #si la clave no esta configurada
                    roles[linea_limpia[1]] = 1
                else:
                    roles[linea_limpia[1]] += 1
    return roles
# Crear archivo
def crear_documento(informacion_limpia):
    with open("Reporte_final.txt", 'w') as archivo:
        # Encabezado
        archivo.write(f"Reporte Oficial de Roles:\n")
        # Iterar en el diccionario para imprimir   
        for rol, cantidad in informacion_limpia.items():
            archivo.write(f'{rol} -> {cantidad}')
            
    

documento = "datos_censo.txt"
leer_documento(documento)
crear_documento(leer_documento)
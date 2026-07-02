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
    for rol, cantidad in roles.items():
        print(f'{rol} {cantidad}')
documento = "datos_censo.txt"
leer_documento(documento)
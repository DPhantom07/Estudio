# Reto 10 Defensivo
# importa el modulo json
# implementa una estructura de errores utilizando try

import json

try:
    with open('save_data_v2.json', 'r') as archivo:
        date = json.load(archivo)

except FileNotFoundError:
    print(f'[ADVERTENCIA] No se encontro el archivo de guardado. configurando perfil predeterminado...')
    perfil_nuevo = {
        'Usuario' : 'Invitado',
        'distancia_maxima' : 0
    }
    print(f'El perfil {perfil_nuevo["Usuario"]} a sido creado exitosamente puede continuar de forma segura')

print(f'[SISTEMA] Motor de juego inicializando correctamente') 
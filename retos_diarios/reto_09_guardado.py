# reto 09
# importar el modulo JSON 
# definir un diccionario llamado save_state que represente la partida
# debe contener exactamente estas llaves y tipos de datos:
# jugador : tu nombre o un nickname (cadena de texto)
# distancia_maxima : un record de metros recorridos (numero enteros)
# monedas_recolectadas : cantidad de monedas (numero entero)
# dificultad : el modo de juego (cadena)

import json

save_stage = {
    'jugador' : 'DPhantom11',
    'distancia_maxima' : 500,
    'monedas_recolectadas' : 100,
    'dificultad' : "Dificil"

}

with open('save_state.json', 'w') as save_state_fisico:
    json.dump(save_stage, save_state_fisico, indent=4)
    #json.dump(diccionario, alias del documento, indet=4) 
print(f'[Sistema] Partida guardada exitosamente')



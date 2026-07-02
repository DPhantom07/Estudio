# Reto 11
# Programar un componente aislado llamado "validador de umbral de obstaculos"
# para la telemetria de tu juego.
# obstaculos (string) velocidad de spawn (float)

import sys

def validar_umbral_obstaculos(obstaculo: str, velocidad_spawn: str) -> None:
    print(f"---Validador de Umbral de Obstaculos---")
    velocidad: float = float(velocidad_spawn)
    print(f'{obstaculo} confirmado, se configuro a la velocidad {velocidad}')

if __name__ == "__main__":
    try:
        obstaculo = sys.argv[1]
        velocidad_spawn = sys.argv[2]
        validar_umbral_obstaculos(obstaculo, velocidad_spawn)
        
    except IndexError:
        print('[ERROR] debes ingreasr los argumentos: obstaculos y velocidad')
    except ValueError:
        print('[ERROR] la velocidad de spawn debe ser un número flotante')
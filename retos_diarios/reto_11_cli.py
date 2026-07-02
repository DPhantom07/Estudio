import sys

def validar_umbral_obstaculos(obstaculo: str, velocidad_spawn: str) -> None:
    """
    Valida y configura la velocidad de aparición de un obstáculo en la telemetría.

    Argumentos:
        obstaculo (str): Nombre del objeto peligroso (ej. 'planta').
        velocidad_spawn (str): Velocidad en formato texto directo de la terminal.
    """
    print("---Validador de Umbral de Obstaculos---")
    # Convertimos el string de la terminal a flotante para cálculos de física
    velocidad: float = float(velocidad_spawn)
    print(f'{obstaculo} confirmado, se configuró a la velocidad {velocidad}')

if __name__ == "__main__":
    try:
        # sys.argv[1] y [2] capturan los parámetros externos obligatorios
        obstaculo = sys.argv[1]
        velocidad_spawn = sys.argv[2]
        validar_umbral_obstaculos(obstaculo, velocidad_spawn)
        
    except IndexError:
        print('[ERROR] Debes ingresar los argumentos: obstaculo y velocidad')
    except ValueError:
        print('[ERROR] La velocidad de spawn debe ser un número flotante')
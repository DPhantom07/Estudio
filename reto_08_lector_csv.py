# Reto 08 lector csv

# Importar modulo csv
import csv

def lector_archivo(archivo):
    with open(archivo, 'r') as documento:
        lector = csv.DictReader(documento)
        for fila in lector:
           velocidad_base = fila['velocidad_base']
           if int(velocidad_base) > 100:
               print(f'[Alerta Fisica] El obstaculo {fila['obstaculo']} requiere colicion dinamica {velocidad_base}')

#fila[0] obtaculo
#fila[1] velocidad base
#fila[2] frecuencia

archivo = "obstaculos_runner.csv"
lector_archivo(archivo)
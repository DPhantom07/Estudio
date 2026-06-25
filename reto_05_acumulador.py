# Reto 05 Contador de horas
# El lider tecnico del proyecto necesita saber cuantas horas totales de desarrollo se han invertido en el proyecto sumando los 
# tiempos de todos los usuarios

def leer_documento(documento):
    contador_horas = 0
    with open(documento, 'r') as archivo:
        for linea in archivo:
            if "," in linea and len(linea.split(',')) >= 3:
                linea_limpia = linea.strip().split(',')
                contador_horas += int(linea_limpia[2])
    print(f'Total de horas: {contador_horas}')

                
            
       

    

documento = "datos_proyectos.txt"
leer_documento(documento)
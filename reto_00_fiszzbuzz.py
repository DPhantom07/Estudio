for numero in range(1, 101):
    #variable de salida
    salida = ""
    if numero % 3 == 0:
        salida += 'Fizz'
    if numero % 5 == 0:
        salida += 'Buzz'
    if  salida == '':
        print(numero)
    else:
        print(salida)
    
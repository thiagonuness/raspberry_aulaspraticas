#Aula pratica 2
#Tratamento de excecoes

import time

#Programa Principal

while 1:
    print("Programa para realizar uma divisao")
    
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))

    try:
        resultado = valor1/valor2
        print("O resultado da divisao ", + resultado)

    except ZeroDivisionError:
        print("ATENCAO: o divisor nao pode ser 0, tente novamente")
    

    time.sleep(2)
    

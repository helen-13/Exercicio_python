# Faça um programa, com uma função que necessite de três
# argumentos, e que forneça a soma desses três argumentos.

def soma(numero1,numero2,numero3):
    calculo = numero1 + numero2 + numero3
    print(f'Os valores somados dará: {calculo}')

numero1 = int(input('Entre com um numero: '))
numero2 = int(input('Entre com um numero: '))
numero3 = int(input('Entre com um numero: '))
soma(numero1,numero2,numero3)
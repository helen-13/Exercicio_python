# Desenvolva um programa que solicite ao usuário os comprimentos dos três
# lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno.
# equilátero: todos os lados com o mesmo valor isósceles: dois lados com o mesmo valor
# escaleno: todos os lados com medidas distintas.

# Solicitar ao usuário os comprimentos dos três lados do triângulo
lado1 = float(input('Digite o comprimento do primeiro lado: '))
lado2 = float(input('Digite o comprimento do segundo lado: '))
lado3 = float(input('Digite o comprimento do terceiro lado: '))

# Verificar se os lados formam um triângulo válido
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    # Classificar o triângulo
    if lado1 == lado2 == lado3:
        print('O triângulo é equilátero.')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('O triângulo é isósceles.')
    else:
        print('O triângulo é escaleno.')
else:
    print('Os comprimentos fornecidos não formam um triângulo válido.')

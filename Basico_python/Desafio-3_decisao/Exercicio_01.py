#Faça um Programa que peça dois números e imprima o maior deles.

# Função para comparar dois números e imprimir o maior
def comparar(numero_1, numero_2):
    if numero_1 > numero_2:
        print(f'O número {numero_1} é maior que o {numero_2}.')
    elif numero_2 > numero_1:
        print(f'O número {numero_2} é maior que o {numero_1}.')
    else:
        print('Os dois números são iguais.')

# Solicitar ao usuário dois números
numero_1 = int(input('Entre com o primeiro número: '))
numero_2 = int(input('Entre com o segundo número: '))

# Chamar a função para comparar os números
comparar(numero_1, numero_2)

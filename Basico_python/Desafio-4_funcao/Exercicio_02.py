#Reverso do número. Faça uma função que retorne o reverso de um
# número inteiro informado. Por exemplo: 127-> 721.

def reverso(numero):
    reversao = str(numero)[::-1]
    print(f'O número invertirdo é: {reversao}')

numero = int(input('Escreva um número que será invertido: '))

reverso(numero)
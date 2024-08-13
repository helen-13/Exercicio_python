#Crie uma função chamada contar_vogais que recebe uma string
#como parâmetro. Implemente a lógica para contar o número de vogais
# na string e retorne o total de vogais. Solicite ao usuário para inserir uma
# frase e utilize a função para contar as vogais.
def contar_vogais(frase):
    vogais = ['a','e','i','o','u']
    contador = 0
    for letra in frase.lower():
        if letra in vogais:
            contador += 1
    return contador
frase = input('Entre com uma frase: ')
contar_vogais(frase)
total_de_vogais = contar_vogais(frase)
print(f'A frase que você digitou tem: {total_de_vogais} vogais')
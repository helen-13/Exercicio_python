# Faça um programa que lê três números inteiros e os mostra em ordem crescente

# Função para ordenar três números inteiros em ordem crescente
def ordena_crescente(numero1, numero2, numero3):
    numeros = [numero1, numero2, numero3]
    numeros.sort()  # Ordena a lista em ordem crescente
    return numeros

# Solicitar três números inteiros ao usuário
numero1 = int(input('Insira o primeiro número: '))
numero2 = int(input('Insira o segundo número: '))
numero3 = int(input('Insira o terceiro número: '))

# Obter a lista de números ordenada
numeros_ordenados = ordena_crescente(numero1, numero2, numero3)

# Exibir os números em ordem crescente
print("Números em ordem crescente:", numeros_ordenados)

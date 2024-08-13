#O programa deve calcular e apresentar a quantidade de números pares e
#  ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário
#  informar o valor zero. Certifique-se de incluir validações para garantir que
#  apenas números positivos sejam considerados na contagem e cálculos.

# Inicializar contadores de pares e ímpares
cont_pares = 0
cont_impares = 0

# Loop para leitura de números
while True:
    # Solicitar um número ao usuário
    numero = int(input('Digite um número positivo (0 para sair): '))
    
    # Encerrar o loop se o número for zero
    if numero == 0:
        break

    # Validar se o número é positivo
    if numero > 0:
        # Verificar se o número é par ou ímpar
        if numero % 2 == 0:
            cont_pares += 1
        else:
            cont_impares += 1
    else:
        print("Número inválido. Por favor, insira um número positivo.")

# Exibir os resultados
print(f"Quantidade de números pares: {cont_pares}")
print(f"Quantidade de números ímpares: {cont_impares}")

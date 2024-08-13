#Escreva um script que pergunta ao usuário se ele deseja converter
# uma temperatura de grau Celsius para Fahrenheit ou vice-versa.
# Para cada opção, crie uma função.
# Extra: Crie uma terceira, que é um menu para o usuário escolher a
# opção desejada, onde esse menu chama a função de conversão correta.

def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(f'A temperatura é: {fahrenheit:.2f} °F')

def fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    print(f'A temperatura é: {celsius:.2f} °C')

def menu():
    print("Escolha uma opção de conversão:")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    opcao = input("Digite o número da opção desejada: ")

    if opcao == '1':
        celsius = float(input("Entre com a temperatura em graus Celsius: "))
        celsius_para_fahrenheit(celsius)
    elif opcao == '2':
        fahrenheit = float(input("Entre com a temperatura em graus Fahrenheit: "))
        fahrenheit_para_celsius(fahrenheit)
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")

# Chamada do menu
menu()

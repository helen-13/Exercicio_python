# Desenvolver um programa que solicite a idade do usuário e identifique se
# ele é uma criança, um adolescente, adulto ou idoso.

import datetime

def obter_ano_nascimento():
    while True:
        try:
            ano = int(input('Entre com o ano do seu nascimento (entre 1900 e o ano atual): '))
            ano_atual = datetime.datetime.now().year
            if 1900 <= ano <= ano_atual:
                return ano
            else:
                print(f'Por favor, insira um ano v\u00e1lido entre 1900 e {ano_atual}.')
        except ValueError:
            print('Entrada inv\u00e1lida. Por favor, insira um n\u00famero inteiro para o ano.')

def calcular_idade(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade

# Programa principal
ano_nascimento = obter_ano_nascimento()
idade = calcular_idade(ano_nascimento)

print(f'Voc\u00ea tem {idade} anos de idade.')

# Adicionar uma mensagem personalizada com base na idade
if idade < 18:
    print('Voc\u00ea \u00e9 menor de idade.')
elif 18 <= idade < 60:
    print('Voc\u00ea \u00e9 um adulto.')
else:
    print('Voc\u00ea \u00e9 um idoso.')

print('Programa conclu\u00eddo.')
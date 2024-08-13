#Crie um programa que leia quanto dinheiro uma pessoa tem na
# carteira, e calcule quanto poderia comprar de cada moeda estrangeira.
# Considere a tabela de conversão abaixo:
# Dólar Americano: R$ 4,91
# Peso Argentino: R$ 0,02
# Dólar Australiano: R$ 3,18
# Dólar Canadense: R$ 3,64
# Franco Suiço: R$ 0,42
# Euro: R$ 5,36
# Libra esterlina: R$ 6,21

def transformacao_moeda(valor):
    dolar_americano = valor/4.91
    peso_argentino = valor/0.02
    dolar_australiano = valor/3.18
    dolar_canadense = valor/3.64
    franco_suico= valor/0.42
    euro = valor/5.36
    libra = valor/6.21
    
    print(f'O valor em real tranformado em: Dólar Americano:{dolar_americano:.2f}, Peso Argentino:{peso_argentino:.2f},  Dólar Australiano:{dolar_australiano:.2f}, Dólar Canadense: {dolar_canadense:.2f}, Franco Suiço: {franco_suico:.2f}, Euro: {euro:.2f}, Libra: {libra:.2f}')

valor = float(input('Entre com o valor em reais: '))

transformacao_moeda(valor)
# Faça um programa que peça uma nota, entre zero e dez. Mostre uma
# mensagem caso o valor seja inválido e continue pedindo até que o usuário
# informe um valor válido.

a= int(input('Primeira bimestre:'))
while a>10:
    a=int(input('você errou'))
b= int(input('Segunda bimestre:'))
while b>10:
    b = int(input('você errou'))
c= int(input('Terceira bimestre:'))
while c>10:
    c = int(input('você errou'))
d= int(input('Quarto bimestre:'))
while d>10:
    d = int(input('você errou'))
media = (a + b + c + d)/ 4
print('media: {}' .format(media))
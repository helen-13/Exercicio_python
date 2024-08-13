#Implemente um programa que classifique um aluno com base em sua
#  pontuação em um exame. O programa deverá solicitar uma nota de 0 a 10.
# Se a pontuação for maior ou igual a 7, o aluno é aprovado; caso contrário, é reprovado.

# Solicitar a nota do aluno
nota_prova = int(input('Digite a nota do exame (0 a 10): '))

# Verificar se a nota está dentro do intervalo válido
while nota_prova < 0 or nota_prova > 10:
    nota_prova = int(input('Nota inválida. Digite uma nota entre 0 e 10: '))

# Classificar o aluno com base na nota
if nota_prova >= 7:
    print('Aprovado!')
else:
    print('Reprovado.')

'''Escreva um programa que, dado um valor inteiro de reais, determine a
quantidade de cada tipo de nota necessária para totalizar esse valor, de
modo a minimizar a quantidade de cédulas a serem emitidas por um
caixa eletrônico. Considere que existem apenas 4 tipos de notas: R$50,
R$10, R$5 e R$1.
Digite o valor inteiro de reais: 72
Notas de 50: 1
Notas de 10: 2
Notas de 5: 0
Notas de 1: 2'''

valor = int(input('Digite o valor inteiro de reais: '))

notas_50 = valor // 50
valor %= 50

notas_10 = valor // 10
valor %= 10

notas_5 = valor // 5
valor %= 5

notas_1 = valor // 1
valor %= 1

print('Notas de 50:',notas_50)
print('Notas de 10:',notas_10)
print('Notas de 5:',notas_5)
print('Notas de 1:',notas_1)
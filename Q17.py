'''Faça um programa que receba dois números, e imprima o maior deles
ou diga se eles são iguais.'''

n1 = float(input('Informe o número: '))
n2 = float(input('Informe outro número: '))

if n1 > n2:
    print(f'O número {n1} e maior')
elif n2 > n1:
    print(f'O número {n2} e maior')
else:
    print('São iguais')
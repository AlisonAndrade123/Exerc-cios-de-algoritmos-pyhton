'''Faça um programa que calcule a tabuada. Receba um valor do usuário e
imprima a tabuada deste número.'''

valor = int(input('Digite um valor: '))
print('-- TABUADA --')
for c in range(1,11):
    resultado = valor * c
    print(f'{valor} x {c} = {resultado}')
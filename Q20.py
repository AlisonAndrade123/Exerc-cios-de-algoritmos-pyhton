'''Faça um Programa que leia um número e exiba o mês correspondente
do ano. (1-Janeiro, 2- Fevereiro, etc.), se digitar outro valor deve aparecer valor
inválido.'''

num = int(input('Informe um número: '))

if num == 1:
    print('Janeiro')
elif num == 2:
    print('Fevereiro')
elif num == 3:
    print('Março')
elif num == 4:
    print('Abril')
elif num == 5:
    print('Maio')
elif num == 6:
    print('Junho')
elif num == 7:
    print('Julho')
elif num == 8:
    print('Agosto')
elif num == 9:
    print('Setembro')
elif num == 10:
    print('Outubro')
elif num == 11:
    print('Novembro')
elif num == 12:
    print('Dezembro')
else:
    print('Inválido')
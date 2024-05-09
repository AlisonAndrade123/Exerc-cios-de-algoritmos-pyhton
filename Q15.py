'''Faça um programa que receba dados de um funcionário, tais como:
Nome, quantidade de horas trabalhadas, valor por hora trabalhada e
calcule o salário desse funcionário. O salário deve ser exibido na tela
indicando o quanto aquele funcionário receberá.'''

nome = input('Digite seu nome: ')
horas_trabalhadas = float(input('Informe as horas trabalhadas: '))
valor_hora_trabalhada = float(input('Informe o valor: '))

salario = horas_trabalhadas * valor_hora_trabalhada

print(f'O funcionário {nome} receberá um salário de R${salario:.2f}')
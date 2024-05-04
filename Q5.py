'''Uma empresa quer dar um bônus de Natal (em dezembro, claro) para seus
empregados que será 60% do cálculo médio do salário de trabalho.
Considerando que todos na empresa ganhem um mesmo valor de salário,
elabore um programa que receba a entrada do salário e imprima o valor do
bônus de Natal e o valor a ser depositado na conta de cada empregado em
dezembro.'''

salario = float(input('informe o salário: '))
bonus = (salario * 60) / 100
valor_total = salario + bonus
print(f'O bonûs é igual: {bonus}')
print(f'Valor a ser depositado é igual: {valor_total}')
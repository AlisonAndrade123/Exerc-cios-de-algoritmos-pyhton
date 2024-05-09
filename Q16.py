'''Faça um programa que receba os dados de um(a) vendedor(a), tais
como:
Nome, salário fixo e o total de vendas efetuadas (em dinheiro). Sabendo
que este vendedor ganha 15% de comissão sobre suas
vendas efetuadas, exiba na tela o salário total que o vendedor(a) recebeu

(salário+comissão). Mostre na tela o quanto de comissão o(a)
vendedor(a) recebeu.'''

nome = input('Digite seu nome: ')
salario_fixo = float(input('Informe o seu salário: '))
vendas_dinheiro = float(input('Informe o valor das vendas em dinheiro: '))

comissao = (vendas_dinheiro * 15) / 100

salario_total = salario_fixo + comissao

print(f'O vendedor {nome} tem um salário total de {salario_total:.2f}')
print(f'A commisão foi de {comissao}')
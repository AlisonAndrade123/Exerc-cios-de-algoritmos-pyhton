'''Faça um programa que receba a idade que o usuário faz esse ano e
diga o ano de nascimento dele.'''

from datetime import date
atual = date.today().year
idade = int(input('Digite sua idade: '))
ano_nascimento = atual - idade
print(ano_nascimento)
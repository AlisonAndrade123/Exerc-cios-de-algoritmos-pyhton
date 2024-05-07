'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e
mostre:
o o produto do dobro do primeiro com metade do segundo.
o a soma do triplo do primeiro com o terceiro.
o o terceiro elevado ao cubo.'''

n1 = int(input('Informe o valor: '))
n2 = int(input('Informe o valor: '))
n3 = float(input('Informe o valor: '))

produto = (n1 * 2) * (n2 / 2)
print(f'O valor do é igual: {produto}')

soma = n1 * 3 + n3 
print(f'O valor do é igual: {soma}')

potencia = n3 ** 3
print(f'O valor do é igual: {potencia:.1f}')






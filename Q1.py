'''Escreva um programa que efetue a apresentação do valor da conversão em
real (R$) de um valor lido em dólar (US$). O algoritmo deverá solicitar ao
usuário o valor da cotação do dólar e também a quantidade de dólares que ele
deseja converter em real.'''

cotacao_dolar = float(input('Valor da cotação: '))
valor_dolar = float(input('Valor para converter: '))
valor_real = valor_dolar * cotacao_dolar
print('O valor em real é: R$', valor_real)
'''Escreva um programa que calcule com quantos litros de gasolina é preciso
abastecer um veículo, dada a distância que se deseja percorrer e a quantidade
de quilômetros que o veículo faz por litro.'''

distancia = float(input('Informe a distancia: '))
quilometros_litro = float(input('Informe a quantidade de quilômetros o véiculo faz por litro: '))
litros_gasolina = distancia / quilometros_litro
print("Para percorrer", distancia, "quilômetros, serão necessários", litros_gasolina, "litros de gasolina.")
'''Escreva um programa que leia uma temperatura em graus Celsius e a
apresente convertida em graus Fahrenheit. A fórmula de conversão é: F =
(9*C+160) / 5, sendo F a temperatura em Fahrenheit e C a temperatura em
Celsius.'''

graus_celsius = float(input('Informe a temperatura em graus celcius: '))
graus_fahrenheit = (9 * graus_celsius + 160) / 5
print(f'A temperatura convertida de celcius para fahrenheit é igual: {graus_fahrenheit}')
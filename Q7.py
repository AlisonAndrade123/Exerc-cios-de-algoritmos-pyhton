'''Agora, faça um programa que receba os valores de x, y e z do usuário e
mostre o resultado da expressão da questão anterior.'''

x = float(input('Informe o valor de x: '))
y = float(input('Informe o valor de y: '))
z = float(input('Informe o valor de z: '))

resultado = x * y < z / x or x / y < z * x and z * y < x

print(resultado)
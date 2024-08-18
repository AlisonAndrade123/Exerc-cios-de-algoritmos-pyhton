#Um número par é um número inteiro que pode ser escrito na forma 2n e n é inteiro. Escreva uma função que receba um inteiro e retorne se ele é par ou não. Em seguida escreva um programa que leia números inteiros e indique se é par ou não, usando a função. O programa deve ser encerrado quando a entrada for -1.

def ParImpar(num):
    if num % 2 != 1:
        return f'PAR'
    elif num % 2 != 0:
        return f'IMPAR'
    
n = int(input())
while n != -1:
    print(ParImpar(n))
    n = int(input())
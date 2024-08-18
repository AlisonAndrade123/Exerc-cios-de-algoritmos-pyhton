#Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos. Exemplo: 120 é triangular, pois 4 × 5 × 6 = 120. Crie uma função que indica se um número é triangular ou não. Em seguida escreva um programa que leia números inteiros e indique se é triangular ou não, usando a função. O programa deve ser encerrado quando a entrada for -1.

def triangular(n):
    i = 1
    while i * (i + 1) * (i + 2) <= n:
        if i * (i + 1) * (i + 2) == n:
            return f'É TRIANGULAR'
        i += 1
    return f'NÃO É TRIANGULAR'

num = int(input())
while num != -1:
    print(triangular(num))
    num = int(input())
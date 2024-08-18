#Número primo é um número natural que tem apenas dois divisores diferentes, o 1 e ele mesmo. Por definição, 1 não é primo. Crie uma função que indica se um número é primo ou não. Em seguida escreva um programa que leia números inteiros e indique se é primo ou não, usando a função. O programa deve ser encerrado quando a entrada for -1.

def primo(num):
    if num <= 1:
        return f'NÃO É PRIMO'
    if num <= 3:
        return f'É PRIMO'
    if num % 2 == 0 or num % 3 == 0:
        return f'NÃO É PRIMO'
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return f'NÃO É PRIMO'
        i += 6
    return f'É PRIMO'

n = int(input())
while n != -1:
    print(primo(n))
    n = int(input()) 
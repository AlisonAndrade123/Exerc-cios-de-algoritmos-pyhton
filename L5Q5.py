#A função fatorial é defina da seguinte forma: n! = n × (n − 1)!. Escreva uma função que receba um número inteiro e retorne o seu fatorial. Em seguida escreva um programa que leia um inteiro e, usando a função, calcule e escreva o seu fatorial.

def fatorial(num):
    i = 1
    for j in range(num, 0, -1):
        i *= j
    return i

n = int(input())
print(fatorial(n))
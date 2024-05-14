'''Faça um programa que leia três números e mostre-os em ordem decrescente.'''

n1, n2, n3 = map(int, input('Informe os valores: ').split())

if n1 > n2 > n3:
    print(n1)
    print(n2)
    print(n3)
elif n1 > n3 > n2:
    print(n1)
    print(n3)
    print(n2)
elif n2 > n1 > n3:
    print(n2)
    print(n1)
    print(n3)
elif n2 > n3 > n1:
    print(n2)
    print(n3)
    print(n1)
elif n3 > n1 > n2:
    print(n3)
    print(n1)
    print(n2)
elif n3 > n2 > n1:
    print(n3)
    print(n2)
    print(n1)
#Escreva um algoritmo que repetitivamente leia dois números, limite inferior e limite superior, e em seguida faça uma chamada a uma função que receba estes limites e imprima o intervalo delimitado pelos limites. O algoritmo deve ser interrompido quando as entradasforem 0 (zero).

def num(li, ls):
    for i in range(li, ls+1):
        print(i)
        
n1 = int(input())
n2 = int(input())

while n1 != 0 or n2 != 0:
    num(n1, n2)
    n1 = int(input())
    n2 = int(input())
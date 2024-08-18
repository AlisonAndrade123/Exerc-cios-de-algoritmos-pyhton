#A série de Fibonacci tem 1 como primeiro e segundo elemento. A partir daí, a série segue definindo o próximo valor como a soma dos dois anteriores. Por exemplo, o terceiro elemento da série é 2 e o quarto é 3. Os oito primeiros elementos são 1, 1, 2, 3, 5, 8, 13 e 21. Escreva uma função que receba um número inteiro, i, e retorne o i-ésimo elemento da série. Em seguida escreva um programa que leia números inteiros e indique os i-ésimos números da série, usando a função. O programa deve ser encerrado quando a entrada for -1.

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    
    anterior = 1
    corrente = 1
    for i in range(n-2):
        proximo = anterior + corrente
        anterior = corrente
        corrente = proximo
    return corrente

num = int(input())
while num != -1:
    print(fibonacci(num))
    num = int(input())
#Escreva um algoritmo que leia dois números, limite inferior e limite superior, imprima o quadrado, x², de todos os números de limite inferior a limite superior e, em seguida, imprima a soma dos números impressos. Por exemplo, se o usuário digitar 2 como limite inferior e 5 como limite superior, deve imprimir 4, 9, 16 e 25 e a soma 54. Armazene os valores que serão impressos em uma lista e, para realizar a soma, crie uma função.

def soma(lista):
    return sum(lista)

limite_inferior = int(input("Digite o limite inferior: "))
limite_superior = int(input("Digite o limite superior: "))

lista_quadrados = []

for num in range(limite_inferior, limite_superior + 1):
    quadrado = num ** 2
    lista_quadrados.append(quadrado)
    print(f"{quadrado}")

print(f"Soma dos quadrados: {soma(lista_quadrados)}")
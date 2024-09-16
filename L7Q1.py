# Escreva um algoritmo que leia 30 numeros inteiros e os armazene em uma lista. Escreva as funções maior, menor e soma. Elas devem receber a lista e retornar o respectivo valor. Por fim, faça chamadas as funções e imprima os retornos.

lista = []

def maior(lista):
    return max(lista)

def menor(lista):
    return min(lista)

def soma(lista):
    return sum(lista)

for i in range(30):
    numero = int(input(f"Digite o {i+1}º número: "))
    lista.append(numero)

print(f"Maior valor: {maior(lista)}")
print(f"Menor valor: {menor(lista)}")
print(f"Soma dos valores: {soma(lista)}")
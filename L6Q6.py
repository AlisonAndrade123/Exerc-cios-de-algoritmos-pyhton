# Escreva um algoritmo que leia 10 números e os escreva em ordem decrescente.

numeros = []

for i in range(10):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

numeros.sort(reverse=True)

print("Números em ordem decrescente:")
for numero in numeros:
    print(numero)

print(numeros)
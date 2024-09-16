# Escreva um algoritmo que leia 10 nomes e os escreva em ordem alfabética.

nomes = []

for i in range(10):
    nome = input(f"Digite o {i+1}º nome: ")
    nomes.append(nome)

nomes.sort()

print("Nomes em ordem alfabética:")
for nome in nomes:
    print(nome)

print(nomes)
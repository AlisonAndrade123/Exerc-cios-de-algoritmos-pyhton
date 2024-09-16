# Escreva um algoritmo que leia uma matriz 2 x 2. Em seguida, deve calcular e imprimir o determinante.

def calcular_determinante(matriz):
    # Extrai os elementos da matriz
    a = matriz[0][0]
    b = matriz[0][1]
    c = matriz[1][0]
    d = matriz[1][1]
    
    # Calcula o determinante
    determinante = a * d - b * c
    return determinante

##############################
##### Programa Principal #####
##############################

## Entrada da matriz 2x2
matriz = []
print("Digite os elementos da matriz 2x2 linha por linha:")
for i in range(2):
    linha = list(map(int, input(f"Linha {i + 1}: ").split()))
    if len(linha) != 2:
        print("Número de colunas incorreto. Tente novamente.")
        linha = list(map(int, input(f"Linha {i + 1}: ").split()))
    matriz.append(linha)

# Cálculo do determinante
determinante = calcular_determinante(matriz)

# Saída
print(f"O determinante da matriz é: {determinante}")

# Escreva um algoritmo que leia 2 matrizes,  calcule e escreva o produto delas. O  algoritmo deve permitir matrizes de diversas dimensões e deve validar se é possível calcular.

def produtoMatrizes(m1, m2):
    resultante = []
    
    # Percorre as linhas da primeira matriz
    for i in range(len(m1)):
        linhaR = []
        # Percorre as colunas da segunda matriz
        for j in range(len(m2[0])):
            soma = 0
            # Percorre os elementos correspondentes para multiplicar
            for k in range(len(m2)):
                soma += m1[i][k] * m2[k][j]
            linhaR.append(soma)
        resultante.append(linhaR)
    
    return resultante


##############################
##### Programa Principal #####
##############################

## Entrada
linhas1, colunas1 = map(int, input("Digite as dimensões da matriz 1 (exemplo: 2x3): ").split("x"))

matriz1 = []
for i in range(linhas1):
    matriz1.append(list(map(int, input(f"Digite a linha {i+1} da matriz 1: ").split())))

linhas2, colunas2 = map(int, input("Digite as dimensões da matriz 2 (exemplo: 3x2): ").split("x"))

matriz2 = []
for i in range(linhas2):
    matriz2.append(list(map(int, input(f"Digite a linha {i+1} da matriz 2: ").split())))

## Verifica se é possível multiplicar as matrizes
if colunas1 != linhas2:
    print("Erro: Não é possível multiplicar as matrizes. O número de colunas da matriz 1 deve ser igual ao número de linhas da matriz 2.")
else:
    ## Processamento
    resultado = produtoMatrizes(matriz1, matriz2)

    ## Saída
    print("Resultado da multiplicação:")
    for linha in resultado:
        print(" ".join(map(str, linha)))

# Escreva um algoritmo que leia as 4 médias bimestrais para cada um dos 40 alunos de uma turma. Em seguida, deve se calcular e imprimir a média anual de cada aluno e a média anual da turma. Mantenha as m ́edias todas em uma lista, estrutura que deve ser criada ao longo da entrada. Crie métodos, a sua escolha, para usar durante o processamento dos dados.

import random

def media_anual_aluno(medias_bimestrais):
    return sum(medias_bimestrais) / len(medias_bimestrais)

def media_anual_turma(medias_anuais):
    return sum(medias_anuais) / len(medias_anuais)

medias_anuais = []

for aluno in range(1, 41):
    medias_bimestrais = []
    print(f"Notas sorteadas para o aluno {aluno}:")
    
    for bimestre in range(1, 5):
        media = random.randint(0, 10)
        medias_bimestrais.append(media)
        print(f"Média do {bimestre}º bimestre: {media}")
    
    media_anual = media_anual_aluno(medias_bimestrais)
    medias_anuais.append(media_anual)
    print(f"Média anual do aluno {aluno}: {media_anual:.2f}\n")

media_turma = media_anual_turma(medias_anuais)
print(f"Média anual da turma: {media_turma:.2f}")
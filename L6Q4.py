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
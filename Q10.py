'''Um aluno recebe 3 notas, nota das listas, nota do projeto e nota das provas.
Calcule a média pondera dessas notas tal que: nota das listas vale 20%, nota
do projeto vale 30% e nota das provas vale 50%.'''

n1 = float(input('Informe a nota: '))
n2 = float(input('Informe a nota: '))
n3 = float(input('Informe a nota: '))

media = (n1 * 20 + n2 * 30 + n3 * 50) / 100

print('A média ponderada das notas do aluno é:', media)
'''O departamento que controla o índice de poluição do meio ambiente mantém 3
grupos de indústrias que são altamente poluentes do meio ambiente. O índice
de poluição aceitável varia de 0,05 até 0,25. Se o índice sobe acima de 0,25 as
indústrias do 1 o grupo são intimadas a suspenderem suas atividades, se o
índice cresce acima de 0,4 as do 1 o e 2 o grupo são intimadas a suspenderem
suas atividades e se o índice atingir acima de 0,5 todos os 3 grupos devem ser
notiﬁcados a paralisarem suas atividades. Escrever um programa que leia o
índice de poluição medido e imprima quais grupos devem suspender suas
atividades.'''

indice_poluição = float(input("Digite o índice de poluição medido: "))

if indice_poluição > 0.5:
    print("Todos os 3 grupos devem suspender suas atividades.")
elif indice_poluição > 0.4:
    print("Os grupos 1 e 2 devem suspender suas atividades.")
elif indice_poluição > 0.25:
    print("O grupo 1 deve suspender suas atividades.")
else:
    print("Não é necessário suspender as atividades de nenhum grupo.")

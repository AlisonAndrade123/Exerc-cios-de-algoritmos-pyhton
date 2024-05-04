'''Escreva um programa que leia o nome de um aluno e as notas das três provas
que ele obteve no semestre. No final informe o nome do aluno e a sua média
(aritmética). Exemplo de formatação da saída:
Nome do aluno: Alice
Media de Alice é: 8.5'''

nome = input('Nome: ')
n1 = float(input('informe a nota: '))
n2 = float(input('informe a nota: '))
n3 = float(input('informe a nota: '))
media = (n1 + n2 + n3) / 3
print(f'Media de {nome} é: {media} ')
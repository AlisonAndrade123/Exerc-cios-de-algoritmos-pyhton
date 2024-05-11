'''Faça um programa que verifique se uma letra digitada é &quot;F&quot; ou &quot;M&quot;.
Conforme a letra, escrever: F - Feminino, M - Masculino, Sexo Inválido.
Considere que o usuário vai digitar F e M maiúsculo.'''

sexo = input('Qual é o sexo? M/F: ')

if sexo == 'M':
    print('Sexo M - masculino cadastrado')
elif sexo == 'F':
    print('Sexo F - femenino cadastrado')
else:
    print('Sexo Inválido')
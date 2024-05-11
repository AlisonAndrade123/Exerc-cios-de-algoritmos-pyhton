'''Faça um programa que verifique se uma letra digitada é vogal ou
consoante.'''

letra = input('Digite uma letra: ')

if letra in ['A', 'E', 'I', 'O', 'U', 'a', 'e' 'i', 'o', 'u']:
    print('Vogal')
elif letra in ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z','b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']:
    print('Consoante')
else:
    print('Por favor, informe uma letra')
# Escreva um algoritmo que imprima a lista dos 100 primeiros números primos, iniciando do 2. Número primo é um número natural que tem apenas dois divisores diferentes, o 1 e ele mesmo. Por definição, 1 não é primo. Crie e utilize uma função que indica se um número é primo ou não e mantenha os números primos em uma lista. Imprima, ao final, a soma dos 100 números primos impresso. Para isso, crie uma função chamada soma que receba a lista como parâmetro e retorne a soma.

primos = []
numero = 2

def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1): 
        if numero % i == 0:
            return False
    return True

def soma(lista):
    return sum(lista)

while len(primos) < 100:
    if eh_primo(numero):
        primos.append(numero)
    numero += 1

print("Os 100 primeiros números primos são:")
print(primos)

print(f"Soma dos 100 primeiros números primos: {soma(primos)}")
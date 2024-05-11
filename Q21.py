'''Escreva programa que pergunte a distância em km que um passageiro
deseja percorrer e calcule o preço da passagem, cobrando R$ 0,53 por km
para viagens de até 200 km e R$ 0,47 por km para viagens mais longas.'''

distancia = float(input('Digite a distância em KM: '))

if distancia <= 200:
    passagem_preco = distancia * 0.53
    print(f'Viagem curta {passagem_preco}')
else:
    passagem_preco = distancia * 0.47
    print(f'Viagem longa {passagem_preco}')
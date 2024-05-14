'''Faça um programa que peça ao usuário as coordenadas (x e y) de um ponto e
imprima a qual quadrante de um plano cartesiano ele pertence. Quando uma
das coordenadas for zero, colocar os dois quadrantes aos quais ela pertence.
Em caso de (0,0), dizer que está no centro.'''

x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

if x > 0 and y > 0:
    print("O ponto está no primeiro quadrante.")
elif x < 0 and y > 0:
    print("O ponto está no segundo quadrante.")
elif x < 0 and y < 0:
    print("O ponto está no terceiro quadrante.")
elif x > 0 and y < 0:
    print("O ponto está no quarto quadrante.")
elif x == 0 and y != 0:
    print("O ponto está no eixo Y.")
elif y == 0 and x != 0:
    print("O ponto está no eixo X.")
elif x == 0 and y == 0:
    print("O ponto está no centro do plano cartesiano.")
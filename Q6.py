'''Dé o resultado da expressão w para as seguintes entradas (mostre os
cálculos): w = x * y < z / x or x / y < z * x and z * y < x
o X=5, y=10, z=15
o X=40, y=10, z=3
o X=20, y=2, z=13'''

w1 = 5 * 10 < 15 / 5 or 5 / 10 < 15 * 5 and 15 * 10 < 5
print(w1)

w2 = 40 * 10 < 3 / 40 or 40 / 10 < 3 * 40 and 3 * 10 < 40
print(w2)

w3 = 20 * 2 < 13 / 20 or 20 / 10 < 13 * 20 and 13 * 2 < 20
print(w3)


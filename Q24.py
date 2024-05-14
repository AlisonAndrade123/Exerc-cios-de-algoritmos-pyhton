'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os
descontos são do Imposto de Renda, que depende do salário bruto (conforme
tabela abaixo) e do INSS (10%) do Salário Bruto. O Salário Líquido
corresponde ao Salário Bruto menos os descontos. O programa deverá pedir
ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
o Desconto do IR:
o Salário Bruto até R$900,00 (inclusive) - isento
o Salário Bruto até R$1500,00 (inclusive) - desconto de 5%
o Salário Bruto até R$2500,00 (inclusive) - desconto de 10%
o Salário Bruto acima de R$2500,00 - desconto de 20% 

Imprima na tela as informações, dispostas conforme o exemplo abaixo. No
exemplo o valor da hora é 5 e a quantidade de hora é 220.
Salário Bruto: (5 * 220) : R$ 1100,00
(-) IR (5%) : R$ 55,00
(-) INSS ( 10%) : R$ 110,00
Total de descontos : R$ 165,00
Salário Liquido : R$ 935,00'''

valor_hora_trabalhada = float(input('Informe o valor da sua hora trabalhada: '))
quantidade_horas_trabalhadas = float(input('Informe a quantidade de horas trabalhadas: '))

salario_bruto = valor_hora_trabalhada * quantidade_horas_trabalhadas

if salario_bruto <= 900:
    ir_desconto = 0
    inss_desconto = salario_bruto * 10 / 100
    salario_liquido = salario_bruto - inss_desconto

elif salario_bruto > 900 and salario_bruto <= 1500:
    ir_desconto = salario_bruto * 5 / 100
    inss_desconto = salario_bruto * 10 / 100
    salario_liquido = salario_bruto - ir_desconto - inss_desconto

elif salario_bruto > 1500 and salario_bruto <= 2500:
    ir_desconto = salario_bruto * 10 / 100
    inss_desconto = salario_bruto * 10 / 100
    salario_liquido = salario_bruto - ir_desconto - inss_desconto

elif salario_bruto > 2500:
    ir_desconto = salario_bruto * 20 / 100
    inss_desconto = salario_bruto * 10 / 100
    salario_liquido = salario_bruto - ir_desconto - inss_desconto

total_descontos = ir_desconto + inss_desconto

print(f'Salário Bruto: R${salario_bruto:.2f}')
print(f'(-) IR: R${ir_desconto:.2f}')
print(f'(-) INSS: R${inss_desconto:.2f}')
print(f'Total de descontos: R${total_descontos:.2f}')
print(f'Salário Liquido: R${salario_liquido:.2f}')
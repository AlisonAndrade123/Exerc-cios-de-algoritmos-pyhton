'''Uma empresa resolveu dar um aumento de salário aos seus funcionários. Faça
um programa que recebe o salário de um funcionário e gere o reajuste
segundo o seguinte critério, baseado no salário atual:
o salários até R$ 280,00 : aumento de 20%
o salários entre R$ 280,01 e R$ 700,00 : aumento de 15%
o salários entre R$ 700,01 e R$ 1500,00 : aumento de 10%
o salários de R$ 1500,01 em diante : aumento de 5% 
Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.'''

salario = float(input('Informe o salário: R$'))

if salario <= 280:
    aumento = salario * 20 / 100
    percentual = 20
    novo_salario = salario + aumento
elif salario > 280 and salario <= 700:
    aumento = salario * 15 / 100
    percentual = 15
    novo_salario = salario + aumento
elif salario > 700 and salario <= 1500:
    aumento = salario * 10 / 100
    percentual = 10
    novo_salario = salario + aumento
elif salario > 1500:
    aumento = salario * 5 / 100
    percentual = 5
    novo_salario = salario + aumento

print(f'o salário antes do reajuste é: R${salario}')
print(f'o percentual de aumento aplicado foi: {percentual}%')
print(f'o valor do aumento foi: R${aumento}')
print(f'o novo salário, após o aumento é: R${novo_salario}')
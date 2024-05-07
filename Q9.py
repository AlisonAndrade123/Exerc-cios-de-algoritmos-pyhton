'''Faça um programa que peça o tamanho de um arquivo para download (em
MB) e a velocidade de um link de Internet (em MBps), calcule e informe o
tempo aproximado de download do arquivo usando este link em segundos e
em minutos.'''

tamanho_arquivo = float(input('Informe o tamanho do arquivo em MB: '))
link_velocidade = float(input('Informe a velocidade em MBps: '))

tempo_download_segundos = tamanho_arquivo / link_velocidade

print(f'Em segundos: {tempo_download_segundos:.2f}')

tempo_download_minutos = tempo_download_segundos / 60

print(f'Em minutos: {tempo_download_minutos:.2f}')


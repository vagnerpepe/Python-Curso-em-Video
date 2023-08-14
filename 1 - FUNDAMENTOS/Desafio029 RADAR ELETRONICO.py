#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$ 7,00 por cada Km acima do limite.

import os
os.system ('cls' if os.name == 'nt' else 'clear')

velocidade = int(input('Qual sua velocidade em Km/h? '))
acimadolimite = float(7.00*(velocidade-80))

if velocidade >80:
    print('Você foi multado.')
    print('Sua multa vai custar R$ {:.2f}.'.format(acimadolimite))

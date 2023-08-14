#Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

C = float(input('Qual a temperatura em °C: '))
F = ((9*C)/5)+32

print ('A temperatura de {:.2f}°C corresponde a {}°F!'.format(C, F))
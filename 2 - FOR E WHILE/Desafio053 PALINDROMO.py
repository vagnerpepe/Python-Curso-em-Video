import os
os.system ('cls' if os.name == 'nt' else 'clear')

# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Ex: APÓS A SOPA; A SACADA DA CASA; A TORRE DA DERROTA; O LOBO AMA O BOLO; ANOTARAM A DATA DA MARATONA.

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
'''inverso = '''
print('Você digitou a frase {}.'.format(frase))
print('Você digitou a frase {}.'.format(palavras))
print('Você digitou a frase {}.'.format(junto))

'''for letra in range(len(junto)-1, -1, -1):
    inverso = inverso + junto[letra]'''
print(junto, inverso)

if inverso == junto:
    print('Temos um Palíndromo.')
else:
    print('A frase digitada não é um Palíndromo.')
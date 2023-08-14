from os import system, name
system ('cls' if name == 'nt' else 'clear')

# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# Ex:
# escreva('Olá, Mundo!')
# Saída:
# ~~~~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~~~~

def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)

escreva('Vagner Pépe')
escreva('Curso de Python no YouTube')
escreva('Curso em Vídeo')
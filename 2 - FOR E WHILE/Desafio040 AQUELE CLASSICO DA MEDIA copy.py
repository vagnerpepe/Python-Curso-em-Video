# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO 

import os
os.system ('cls' if os.name == 'nt' else 'clear')

n1 = float(input('\033[37mDigite a 1ª nota:\033[m \033[1;34m'))
n2 = float(input('\033[m\033[37mDigite a 2ª nota:\033[m \033[1;34m'))
media = (n1 + n2) / 2

if media < 5.0:
    print('\033[m\033[1;31mTirando {} e {}, a média do aluno é {:.1f}\033[m'.format(n1, n2, media))
    print('\033[m\033[1;31mO aluno está REPROVADO!\033[m')
elif media >= 5.0 and media <= 6.9:
    print('\033[m\033[1;31mTirando {} e {}, a média do aluno é {:.1f}\033[m'.format(n1, n2, media))
    print('\033[m\033[1;31mO aluno está em RECUPERAÇÃO!\033[m')
else:
    print('\033[m\033[1;32mTirando {} e {}, a média do aluno é {:.1f}\033[m'.format(n1, n2, media))
    print('\033[m\033[1;32mO aluno está APROVADO!\033[m')



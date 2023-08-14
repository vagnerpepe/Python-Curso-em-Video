import os
os.system ('cls' if os.name == 'nt' else 'clear')

tempo = int(input('Quantos anos tem seu carro?: '))
if tempo <= 3:
    print('Carro novo.')
else:
    print('Carro velho.')
print ('--Fim--')

tempo = int(input('Quantos anos tem seu carro?: '))
print('Carro novo.' if tempo<=3 else 'Carro velho.')
print('--FIM--')
#-----------------------------------------------------------------------------

nome = str(input('Qual é o seu nome? '))
if nome == 'Vagner':
    print('Que nome lindo você tem!')
else: print('Seu nome é tão normal!')
print('Bom dia {}!'.format(nome))
#-----------------------------------------------------------------------------

n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))
media = (n1+n2)/2
print('Sua média foi boa! Parabéns! {:.1f}.'.format(media))
print('Sua média foi boa! Parabéns!' if media >= 6.5 else 'Sua média foi ruim! Estude mais!')
if media >=6.5:
    print('Sua média foi boa! Parabéns!')
else: print('Sua média foi ruim! Estude mais!')

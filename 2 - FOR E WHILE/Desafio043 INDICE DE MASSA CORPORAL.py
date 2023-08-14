# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do Peso
# Entre 18.5 e 25: Peso Ideal
# Entre 25 até 30: Obesidade
# Acima de 40: Obesidade Mórbida 

import os
os.system ('cls' if os.name == 'nt' else 'clear')

peso = float(input('Informe o seu peso em KG: '))
altura = float(input('Agora a sua altura em centímetros: '))
imc = peso/(altura**2)

print('O seu IMC é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Abaixo do Peso')
elif imc >= 18.5 and imc <= 24.9:
    print('Peso Ideal')
elif imc >= 25 and imc <= 29.9:
    print('Sobrepeso')
elif imc >= 30 and imc <= 34.9:
    print('Obesidade Grau I')
elif imc >= 35 and imc <= 39.9:
    print('Obesidade Grau II')
elif imc >= 40:
    print('Obesidade Grau III ou Mórbida')



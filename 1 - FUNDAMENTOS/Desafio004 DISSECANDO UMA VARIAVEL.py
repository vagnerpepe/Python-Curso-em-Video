#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

var = input('Digite algo: \n')
print(type(var))

if (var.isnumeric()):
    print('É númerico')
elif (var.isalpha()):
    print('É letra')
elif (var.isalnum()):
    print('É alfanumérico')
elif (var.isupper()):
    print('É letra maiúscula')
else: print('É caracter especial')

#Segunda maneira de resolver;

valor = input ('Digite Algo: ')
print ('O tipo primitivo desse valor é', type(valor))
print ('Só tem espaços?', (valor.isspace()))
print ('É um número?', (valor.isnumeric()))
print ('É alfabético?', (valor.isalpha()))
print ('É alfanumérico?', (valor.isalnum()))
print ('Está em maiúsculas?', (valor.isupper()))
print ('Está em minúsculas?', (valor.islower()))
print ('Está capitalizada?', (valor.istitle()))
#Faça um algorítimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o salário desejado: R$ '))

print ('Novo salário com aumento de 15%: R$ {:.2f}'.format(salario+((salario/100)*15)))

#Segunda maneira de resolver:

novosalario = salario+(salario*15/100)

print ('O salário que era de R$ {:.2f}, passou a ser de R$ {:.2f} com 15% de aumento.'.format(salario, novosalario))
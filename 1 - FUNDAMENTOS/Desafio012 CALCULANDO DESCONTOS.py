#Faça um algorítimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Qual o preço do produto? R$ '))
print('Preço com desconto de 5%: R$ {:.2f}'.format(preco-((preco/100)*5)))

#Segunda maneira de resolver:

novopreco = preco-(preco*5/100)

print('O produto que custava R$ {:.2f}, na promoção com desconto de 5% vai custar R$ {:.2f}.'.format(preco, novopreco))
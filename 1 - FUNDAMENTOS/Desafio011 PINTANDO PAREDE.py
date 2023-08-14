#Faça um programa que leia a largura e a altura de uma parede em metros,
#calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

largura = float(input('Qual a largura da parede?: '))
altura = float(input('Qual a altura da parede?: '))
tinta = 2
area = largura*altura

print ('Área = {:.2f} m²'.format(largura*altura))
print ('Quantidade de tinta necessária: {:.1f} litros'.format((largura*altura)/tinta))

#Segunda maneira de resolver:

print ('Sua parede tem a dimensão de {}x{} e sua área é de {:.2f} m².'.format(largura, altura, area))
print ('Para pintar essa parede, você precisará de {:.1f} litros de tinta.'.format((area)/2))



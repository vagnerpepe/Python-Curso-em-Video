import os
os.system('cls' if os.name=='nt'else 'clear')

frase = 'Curso em Vídeo Python'
print(frase[::2])
print('Oi')
print("""tentei fazer um script que retornasse as iniciais do nome usando o comando split. mas não funcionou dessa forma.
Pensei que por ele reorganizasse os indices na cadeia da string.
Imprimiria o resultado a cada posição 0.  O que sugerem?""")
print(frase.count('o'))
print(frase.count('O'))
print(frase.upper().count('O'))
print(len(frase))
print(len(frase.strip()))
print(frase.replace('Python','Android'))
print(frase[0])
print('Curso'in frase)
print(frase.find('Curso'))
print(frase.find('Vídeo'))
print(frase.find('vídeo'))
print(frase.lower().find('vídeo'))
print(frase.split())
dividido = frase.split()
print(dividido)
print(dividido[2][3])
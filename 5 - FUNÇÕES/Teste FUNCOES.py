from os import system, name
system ('cls' if name == 'nt' else 'clear')

def linha():
    print('-' * 30)


linha()
print('     CURSO EM VÍDEO     ')
linha()
print('     APRENDA PYTHON     ')
linha()
print('     VAGNER PÉPE     ')
linha()
#-----------------------------------------------------------------------------
def mensagem(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)


mensagem('SISTEMA DE ALUNOS')
mensagem('VAGNER PÉPE')
#-----------------------------------------------------------------------------
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')
    

soma(4, 5)
soma(a=7, b=2)
soma(b=3, a=1)
#-----------------------------------------------------------------------------
def contador(* num): # (*) significa vários
    print(num) #(2, 1, 7) 
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!') #2 1 7 FIM!
    tam = len(num)
    print(f'Recebi os valores {num} que são ao todo {tam} números') #Recebi os valores (2, 1, 7) que são ao todo 3 números


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
#-----------------------------------------------------------------------------
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1 


valores = [6, 3, 9, 1, 0, 2] #lista
dobra(valores)
print(valores)
#-----------------------------------------------------------------------------
def soma(* valores):
    soma = 0
    for num in valores:
        soma += num
    print(f'Somando os valores {valores} temos {soma}')


soma(5, 2)
soma(2, 9, 4)
#-----------------------------------------------------------------------------
#INTERACTIVE HELP

print(input.__doc__)
help(input)
#-----------------------------------------------------------------------------
#DOCSTRINGS

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    param i: início da contagem
    param f: fim da contagem
    param p: passo da contagem
    return: sem retorno
    Função criada por Vagner Pépe
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM!')


help(contador)
#-----------------------------------------------------------------------------
#PARÂMETROS OPCIONAIS

def somar(a = 0, b = 0, c = 0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    param a: o primeiro valor
    param b: o segundo valor
    param c: o terceiro valor
    Função criada por Vagner Pépe
    """
    s = a + b + c
    print(f'A soma vale {s}')


help(somar)
somar(3, 2, 5)
somar(8, 4)
somar(2)
somar()
#-----------------------------------------------------------------------------
#ESCOPO DE VARIÁVEIS

def teste(): # (Escopo Local)
    x = 8 # Variável Local
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


# Programa Principal (Escopo Global)
n = 2 # Variável Global
print(f'No programa principal, n vale {n}')
teste()

def teste(b): # Escopo Local
    global a #altera o valor global de A
    a = 8
    b += 4
    c = 2
    print(f'A local vale {a}')
    print(f'B local vale {b}')
    print(f'C local vale {c}')


a = 5 #Escopo Global
teste(a)
print(f'A global vale {a}')
#-----------------------------------------------------------------------------
#RETORNANDO VALORES

def somar(a = 0, b = 0, c = 0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Os resultados foram {r1}, {r2} e {r3}.')

def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')

def par(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if (par(num)):
    print('É par!')
else:
    print('Não é par!')
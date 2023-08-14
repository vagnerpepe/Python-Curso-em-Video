from os import system, name
system ('cls' if name == 'nt' else 'clear')

try: # Operação
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except: # Falhou
    print(f'Infelizmente houve um erro :(')
else: # Deu certo
    print(f'O resultado é {r:.1f}')
finally: # Certo / Falha
    print('Volte sempre! Muito obrigado!')
#-----------------------------------------------------------------------------
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')
#-----------------------------------------------------------------------------
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')
def metade(preço = 0, format = False):
    """
    -> Calcula a metade de um determinado preço,
    retornando o resultado com ou sem formatação.
    param preço: preço que ser quer reajustar
    param format: quer a saída formatada ou não?
    return: o valor reajustado, com ou sem formato.
    """
    res = preço / 2
    return res if format is False else moeda(res)


def dobro(preço = 0, format = False):
    """
    -> Calcula o dobro de um determinado preço,
    retornando o resultado com ou sem formatação.
    param preço: preço que ser quer reajustar
    param format: quer a saída formatada ou não?
    return: o valor reajustado, com ou sem formato.
    """
    res = preço * 2
    return res if format is False else moeda(res)


def aumentar(preço = 0, taxa = 0, format = False):
    """
    -> Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    param preço: preço que ser quer reajustar
    param taxa: porcentagem do aumento
    param format: quer a saída formatada ou não?
    return: o valor reajustado, com ou sem formato.
    """
    res = preço + (preço * taxa/100)
    return res if format is False else moeda(res)


def diminuir(preço = 0, taxa = 0, format = False):
    """
    -> Calcula a redução de um determinado preço,
    retornando o resultado com ou sem formatação.
    param preço: preço que ser quer reajustar
    param taxa: porcentagem da redução
    param format: quer a saída formatada ou não?
    return: o valor reajustado, com ou sem formato.
    """
    res = preço - (preço * taxa/100)
    return res if format is False else moeda(res)


def moeda(preço = 0, moeda = 'R$ '):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(preço = 0, taxaAumento = 10, taxaRedução = 5):
    print('-' * 35)
    print('RESUMO DO VALOR'.center(35))
    print('-' * 35)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxaAumento}% de aumento: \t{aumentar(preço, taxaAumento, True)}')
    print(f'{taxaRedução}% de redução: \t{diminuir(preço, taxaRedução, True)}')
    print('-' * 35)
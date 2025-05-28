'''Identificar números que aparecem mais de uma vez e contar. Usar um dicionário para contar as ocorrências e filtrar aqueles com contagem >1'''

def contar_repetidos(lista):
    contagem = {}
    for num in lista:
        contagem[num] = contagem.get(num, 0) + 1
    return {k: v for k, v in contagem.items() if v > 1}

print(contar_repetidos([1, 2, 2, 3, 4, 4, 4])) 
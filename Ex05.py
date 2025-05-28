'''Função que retorna uma nova lista com elementos únicos.'''

def elementos_unicos(lista):
    unicos = []
    for item in lista:
        if item not in unicos:
            unicos.append(item)
    return unicos

print(elementos_unicos([1, 2, 2, 3, 4, 4]))  
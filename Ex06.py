'''Função para verificar se uma lista está ordenada. Comparar cada elemento com o próximo. Se todos estiverem em ordem crescente, retorna True'''

def esta_ordenada(lista):
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            return False
    return True

print(esta_ordenada([1, 2, 3]))  
print(esta_ordenada([3, 2, 1]))  
''' Contar letras em uma frase. Ignorar espaços e diferenciar maiúsculas e minúsculas'''

frase = "Python é divertido"
contagem = {}

for letra in frase.lower():
    if letra != " ":
        contagem[letra] = contagem.get(letra, 0) + 1

print(contagem) 
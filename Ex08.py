''' Dicionário com nomes e listas de notas, calcular média. Iterar sobre cada aluno, somar as notas e dividir por 3'''

alunos = {
    "João": [7, 8, 6],
    "Maria": [9, 10, 9],
}

for nome, notas in alunos.items():
    media = sum(notas) / len(notas)
    print(f"{nome}: {media:.1f}")  
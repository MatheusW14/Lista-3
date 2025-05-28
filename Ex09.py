'''Atualizar estoque de frutas com base em vendas. Suponho que a lista de vendas tem frutas e quantidades vendidas. Para cada venda, subtrair a quantidade do estoque'''

estoque = {"maçã": 50, "banana": 30, "laranja": 40}
vendas = [("maçã", 20), ("banana", 15), ("maçã", 10)]

for fruta, qtd in vendas:
    estoque[fruta] -= qtd

print(estoque) 
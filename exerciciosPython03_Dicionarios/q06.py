# Dicionário com Dicionário
estoque = {
    "arroz": {"preco": 5.89, "quantidade": 10},
    "feijao": {"preco": 7.99, "quantidade": 5}
}

print(estoque["arroz"]["preco"])

estoque["feijao"]["quantidade"] = 3
print(estoque)
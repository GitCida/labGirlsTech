# Desconto por valor
valorCompra = float(input("Digite o preço da compra: "))
precoComDesconto = 0
if valorCompra > 100:
    precoComDesconto = valorCompra - (valorCompra * 0.1)
elif valorCompra <= 100 and valorCompra >= 50:
    precoComDesconto = valorCompra - (valorCompra * 0.05)
else:
    precoComDesconto = valorCompra

print(f'O valor a pagar é: {precoComDesconto:.2f}')
# Desafio final - Caixa eletrônico simples

valorSaque = int(input("Digite o valor que deseja sacar: "))
notasDe100 = 0
notasDe50 = 0
notasDe20 = 0
notasDe10 = 0
dinheiroRestante = 0

while valorSaque != 0:
    if valorSaque >= 100:
        valorSaque -= 100
        notasDe100 += 1
    elif valorSaque < 100 and valorSaque >= 50:
        valorSaque -= 50
        notasDe50 += 1
    elif valorSaque < 50 and valorSaque >= 20:
        valorSaque -= 20
        notasDe20 += 1
    elif valorSaque < 20 and valorSaque >= 10:
        valorSaque -= 10
        notasDe10 += 1
    else:
        dinheiroRestante += valorSaque
        valorSaque -= valorSaque

print(f'\nNotas de R$100: {notasDe100}\nNotas de R$50: {notasDe50}\nNotas de R$20: {notasDe20}\nNotas de R$10: {notasDe10}\n')

if dinheiroRestante != 0:
    print(f'Ainda sobraram {dinheiroRestante} reais para sacar.')
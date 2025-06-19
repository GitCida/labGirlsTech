# Tabuada (for)
numero = int(input("Digite um número para ver sua tabuade de 1 a 10: "))

for x in range(1, 11):
    print(f'{numero} * {x} =  {numero * x}')
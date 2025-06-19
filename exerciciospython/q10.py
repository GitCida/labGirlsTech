# Quantos pares e ímpares?
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))
n5 = int(input("Digite o quinto número: "))

numeroLista = [n1, n2, n3, n4, n5]
numeroPares = 0
numeroImpares = 0 

for x in numeroLista:
    if x % 2 == 0: 
        numeroPares += 1
    else:
        numeroImpares += 1
        
print(f'Numeros pares: {numeroPares} \n Numeros ímpares: {numeroImpares}')
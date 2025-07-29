# Classificador de IMC
peso = float(input("Digite seu peso: "))
altura = float(input("Digite seu altura: "))
IMC = round(peso / (altura**2), 1)

if IMC < 18.5:
    print(f'Seu IMC é {IMC}. Você está abaixo do peso.')
elif IMC >= 18.5 and IMC <= 24.9:
    print(f'Seu IMC é {IMC}. Você está com o peso ideal.')
elif IMC >= 25 and IMC <= 29.9:
    print(f'Seu IMC é {IMC}. Você está com sobrepeso.')
else:
    print(f'Seu IMC é {IMC}. Você está com obesidade.')
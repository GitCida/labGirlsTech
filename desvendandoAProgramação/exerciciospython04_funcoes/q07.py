# Conversor de Temperatura
def converter(celsius):
    return (celsius * 1.8) + 32
    
celsius = (int(input("Digite a temperatura em Celsius: ")))
fahrenheit = converter(celsius)
print(f'A temperatura em Fahrenheit é: {fahrenheit:.1f}')

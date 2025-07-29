# Verificação de Par ou Ímpar
def par_ou_impar(n):
    if n % 2 == 0:
        return "par"
    else:
        return "ímpar"
    
numero = int(input("Digite um número: "))
numeroVerificado = par_ou_impar(numero)
print(f'Esse número é: {numeroVerificado}')

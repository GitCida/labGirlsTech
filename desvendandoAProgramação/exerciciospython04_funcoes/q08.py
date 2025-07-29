# Média de Notas
def media(n1, n2, n3):
    return (n1 + n2+ n3)/3

def situacao(media):
    if media >= 7:
        return "aprovada."
    else:
        return "reprovada."
    
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

mediaAluna = media(n1, n2, n3)
situacaoAluna = situacao(mediaAluna)

print(f'Com a media {mediaAluna:.2f}, você está {situacaoAluna}')
acao = '7'
while acao != '0':
    acao = input('''
----------Biblioteca----------

1 - Cadastrar livros
2 - Listar livros disponíveis
3 - Buscar livro por título
4 - Emprestar livros
5 - Devolver livros
0 - Sair

-------------------------------
Escolha o que deseja realizar: ''')
    if acao == '0':
        break
    elif acao == '1':
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor: ")
        anoPublicacao = int(input("Digite o ano de publicação: "))
        quantidade = int(input("Digite a quantidade: "))
        livros = {
            "titulo": titulo,
            "autor": autor,
            "anoPublicacao": anoPublicacao,
            "quantidade": quantidade,
        }
        
        with open("livros.txt", "a") as arquivo:
            arquivo.write(f'titulo: {titulo}\n')
            arquivo.write(f'autor: {autor}\n')
            arquivo.write(f'anoPublicacao: {anoPublicacao}\n')
            arquivo.write(f'quantidade: {quantidade}\n')
            arquivo.write(f'\n')
            
    elif acao == '2':
        with open("livros.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            for item in linhas:
                print(item.strip())
        

    elif acao == '3':
        break
    elif acao == '4':
        break
    elif acao == '5':
        break
    else:
        print('Você digitou algo inválido, tente novamente. ')
print('Você saiu da biblioteca. ')
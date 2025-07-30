# Criar Agenda Simples
acao = ''
while acao != '0':
    acao = input('''
---Agendamento de contatos---
1 - Cadastrar contato
0 - Sair
-----------------------------
Escolha o que deseja realizar: ''')
    if acao == '0':
        break
    
    elif acao == '1':
        nome = input("Digite o nome: ")
        telefone = int(input("Digite o telefone(Apenas números): "))
        with open("agenda.txt", "a") as agenda:
            agenda.write(f'{nome} --> {telefone}\n')
        
    else:
        print('Você digitou algo inválido, tente novamente. ')
print('Programa encerrado.')

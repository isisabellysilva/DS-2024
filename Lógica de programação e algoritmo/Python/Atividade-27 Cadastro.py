from click import clear

nome_p1= []
email_p1= []
nome_p2= []
email_p2= []

def cadastrar_cadastro():
    nome = input('Digite o nome da pessoa: ')
    email = input('Digite o email da pessoa: ')
    idade = input('Digite a descrição do produto: ')
    sexualidade = input('Digite a quantidade: ')

    nome.append(nome)
    email.append(email)
    idade.append(idade)
    sexualidade.append(sexualidade)

    with open('cadastro.txt', 'a') as arquivo:
        arquivo.write(f'{nome},{email}, {idade}, {sexualidade}\n')

clear()
def mostrar_cadastro():
    print('Nome da pessoa  \t E-mail da pessoa \t Idade  \t Sexualidade ')
    for i in range(0, len(nome)):
        print(f'{nome[i]} \t\t {email[i]} \t\t\t {idade[i]} \t\t {sexualidade[i]}')

def excluir_cadastro():
    opcao = int(input('Qual registro deseja deletar?'))
    nome.pop(opcao)
    email.pop(opcao)
    idade.pop(opcao)
    sexualidade.pop(opcao)

while True:
    clear()

    print("Escolha uma opção")
    print("1 - Para adicionar cadastro")
    print("2 - Para mostrar o cadastro")
    print("3 - Para excluir um cadastro")
    print("4 - Para sair")
    opcao = int(input("O que deseja fazer? "))
    if opcao == 1:
        cadastrar_pessoa()
    elif opcao == 2:
        mostrar_cadastro()
    elif opcao == 3:
        excluir_cadastro()
    elif opcao == 4:
        break
        inf = str(input("Tecle enter para continuar..."))
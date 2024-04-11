from click import clear
def boasvindas(usuario):
    print(f'Seja bem-vinda {usuario}')
boasvindas('Silva')
print(input('Oque deseja fazer hoje?'))
print(f'=====================MENU==============================')
letra = 's'

nome_produto = []
valor_produto = []
descricao_produto = []
quantidade_produto = []

def cadastrar_produto():
    nome = input('Digite o nome do produto: ')
    valor = float(input('Digite o valor do produto: '))
    descricao = input('Digite a descrição do produto: ')
    quantidade = int(input('Digite a quantidade: '))

    nome_produto.append(nome)
    valor_produto.append(valor)
    descricao_produto.append(descricao)
    quantidade_produto.append(quantidade)

    with open('produtos.txt', 'a') as arquivo:
        arquivo.write(f'{nome},{valor}, {descricao}, {quantidade}\n')

clear()
def mostrar_produto():
    print('nome do produto  \t valor do produto \t quantidade  \t descricao do produto ')
    for i in range(0, len(nome_produto)):
        print(f'{nome_produto[i]} \t\t {valor_produto[i]} \t\t\t {quantidade_produto[i]} \t\t {descricao_produto[i]}')

def excluir_produto():
    opcao = int(input('Qual registro deseja deletar?'))
    nome_produto.pop(opcao)
    valor_produto.pop(opcao)
    descricao_produto.pop(opcao)
    quantidade_produto.pop(opcao)

while True:
    clear()

    print("Escolha uma opção")
    print("1 - Para adicionar um produto")
    print("2 - Para mostrar produtos")
    print("3 - Para excluir um produto")
    print("4 - Para sair")
    opcao = int(input("O que deseja fazer? "))
    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        mostrar_produto()
    elif opcao == 3:
        excluir_produto()
    elif opcao == 4:
        break
        inf = str(input("Tecle enter para continuar..."))
# nó:{"valor": dado, "proximo": None}
produto = {}

# achar o cabeça
def valorExiste(listaCabeca, valorEntrada):
    atual = listaCabeca
    while atual is not None:
        if atual["valor"] == valorEntrada:
            return True
        atual = atual["proximo"]
    return False

# 1 - Inserir
# def inserirInicio(listaEntrada, valorEntrada):
#   novoNo = {"valor": valorEntrada, "proximo": listaEntrada}
#   print("Inclusao com sucesso")
def inserirInicio(listaEntrada):
    valor = input("Digite o valor: ")
    if (valorExiste(listaEntrada, valor)):
        print("Código de produto Duplicado")
        return listaEntrada
    novoNo = {"valor": valor, "proximo": listaEntrada}
    print("Produto Inserido")
    return novoNo

# 2 - Inserir no fim
def inserirFim():
    print("Produto incluido no fim com sucesso")

# 3 - Inserir no meio
def inserirMeio():
    print("3-Inserir no meio")

# 4 - Listar
def listar(listaRecebida):
    if listaRecebida is None:
        print("Lista Vazia")
        return
    listaAtual = listaRecebida
    while listaAtual is not None:
        print(listaAtual["valor"], end="->")
        listaAtual = listaAtual["proximo"]

# 5 - Remover Nó
def remover():
    print("5 - Remover Nó")

# 6 - Buscar Nó
def buscar(listaRecebida):
    if listaRecebida is None:
        print("Lista Vazia")
        return
    
    valor = input("Digite o valor que deseja buscar: ")
    atual = listaRecebida
    posicao = 1
    
    while atual is not None:
        if atual["valor"] == valor:
            print(f"Valor encontrado na posição {posicao}")
            return
        atual = atual["proximo"]
        posicao += 1
    
    print("Valor não encontrado na lista") 


#menu
def menu():
    lista = None
    while True:
        print("\n======== Menu do CRUD =======")
        print("1 - Inserir")
        print("2 - Inserir no fim")
        print("3 - Inserir no meio")
        print("4 - Listar")
        print("5 - Remover Nó")
        print("6 - Buscar Nó")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            lista = inserirInicio(lista)
        elif opcao == "2":
            inserirFim()
        elif opcao == "3":
            inserirMeio()
        elif opcao == "4":
            listar(lista)
        elif opcao == "5":
            remover()
        elif opcao == "6":
            buscar(lista)
        elif opcao == "0":
            print("Opção inválida")
        else:
            break
    print("Obrigado por usar o sistema")

print("**Bem vindo ao programa**")
menu()
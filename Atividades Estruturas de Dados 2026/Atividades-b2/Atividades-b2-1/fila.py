-----------------------------------------------------------------------------------------
FATEC-São Caetano do Sul, São Paulo.
Id da Atividade: ED-Atividade-B2-2
Estrutura de Dados
Data: 30/04/2026
Nome: David Lima Alves

Objetivo: Desenvolver uma aplicação que simule o gerenciamento de impressão (SPOOL),
utilizando estruturas de dados do tipo fila dinâmica para organizar documentos de
alunos e administrativos, aplicando regra de prioridade no processamento.
----------------------------------------------------------------------------------------

class No:
    def __init__(self, nome, paginas):
        self.nome = nome
        self.paginas = paginas
        self.proximo = None


class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def esta_vazia(self):
        return self.inicio == None

    def enqueue(self, nome, paginas):
        novo = No(nome, paginas)

        if self.inicio == None:
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.proximo = novo
            self.fim = novo

    def dequeue(self):
        if self.esta_vazia():
            return None

        removido = self.inicio
        self.inicio = self.inicio.proximo

        if self.inicio == None:
            self.fim = None

        return removido

    def tamanho(self):
        cont = 0
        atual = self.inicio

        while atual != None:
            cont += 1
            atual = atual.proximo

        return cont

    def listar(self):
        atual = self.inicio

        while atual != None:
            print(f"Arquivo: {atual.nome} | Páginas: {atual.paginas}")
            atual = atual.proximo

fila_alunos = Fila()
fila_adm = Fila()


def adicionar_aluno():
    nome = input("Nome do arquivo: ")
    paginas = int(input("Qtd de páginas: "))
    fila_alunos.enqueue(nome, paginas)
    print("Documento de aluno adicionado!\n")


def adicionar_adm():
    nome = input("Nome do arquivo: ")
    paginas = int(input("Qtd de páginas: "))
    fila_adm.enqueue(nome, paginas)
    print("Documento ADM adicionado!\n")


def processar():
    if not fila_adm.esta_vazia():
        doc = fila_adm.dequeue()
        print(f"Imprimindo ADM: {doc.nome} ({doc.paginas} páginas)\n")
    elif not fila_alunos.esta_vazia():
        doc = fila_alunos.dequeue()
        print(f"Imprimindo Aluno: {doc.nome} ({doc.paginas} páginas)\n")
    else:
        print("Nenhum documento na fila.\n")


def visualizar():
    print("\n--- FILA ADM ---")
    print("Quantidade:", fila_adm.tamanho())
    fila_adm.listar()

    print("\n--- FILA ALUNOS ---")
    print("Quantidade:", fila_alunos.tamanho())
    fila_alunos.listar()
    print()


def menu():
    while True:
        print("1 - Adicionar Aluno")
        print("2 - Adicionar ADM")
        print("3 - Processar impressão")
        print("4 - Ver filas")
        print("5 - Sair")

        op = input("Escolha: ")

        if op == "1":
            adicionar_aluno()
        elif op == "2":
            adicionar_adm()
        elif op == "3":
            processar()
        elif op == "4":
            visualizar()
        elif op == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida\n")

menu()
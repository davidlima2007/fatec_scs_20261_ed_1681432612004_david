class No:
    def __init__(self, nome_arq, paginas):
        self.nome_arq = nome_arq
        self.paginas = paginas
        self.proximo = None


class Fila:
    def __init__(self, nome):
        self.nome = nome
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def vazia(self):
        return self.inicio is None

    def inserir(self, nome_arq, paginas):
        novo = No(nome_arq, paginas)

        if self.vazia():
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.proximo = novo
            self.fim = novo

        self.tamanho += 1

    def remover(self):
        if self.vazia():
            return None

        removido = self.inicio
        self.inicio = self.inicio.proximo

        if self.inicio is None:
            self.fim = None

        self.tamanho -= 1
        return removido

    def mostrar(self):
        print(f"Fila {self.nome} | Quantidade de documentos: {self.tamanho}")

        atual = self.inicio

        while atual:
            print(f"• Arquivo: {atual.nome_arq} | Páginas: {atual.paginas}")
            atual = atual.proximo

        print()


class impressao:
    def __init__(self):
        self.fila_adm = Fila("Administrativo")
        self.fila_aluno = Fila("Aluno")
        self.fila_geral = Fila("Impressão Geral")

    def adicionar(self, tipo, nome_arq, paginas):
        if tipo == 'ADM':
            self.fila_adm.inserir(nome_arq, paginas)

        elif tipo == 'ALUNO':
            self.fila_aluno.inserir(nome_arq, paginas)

        else:
            print("Categoria de usuário inválida.")

    def reorganizar(self):
        if not self.fila_geral.vazia():
            print("A fila geral deve estar vazia antes da reorganização.")
            return

        while not self.fila_adm.vazia():
            doc = self.fila_adm.remover()
            self.fila_geral.inserir(doc.nome_arq, doc.paginas)

        while not self.fila_aluno.vazia():
            doc = self.fila_aluno.remover()
            self.fila_geral.inserir(doc.nome_arq, doc.paginas)

        print("Organização das filas concluída.\n")

    def imprimir(self):
        if self.fila_geral.vazia():
            print("Nenhum documento disponível para impressão.")
            return

        doc = self.fila_geral.remover()
        print(f"Documento impresso: {doc.nome_arq} ({doc.paginas} páginas)")

    def listar_tudo(self):
        print("========== STATUS DAS FILAS ==========")

        self.fila_adm.mostrar()
        self.fila_aluno.mostrar()
        self.fila_geral.mostrar()
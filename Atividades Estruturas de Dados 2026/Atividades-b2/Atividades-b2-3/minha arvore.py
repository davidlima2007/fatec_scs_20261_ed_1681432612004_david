from collections import deque


class No:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None


class ArvoreBST:
    def __init__(self, raiz=None):
        self.raiz = raiz

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_rec(self.raiz, valor)

    def _inserir_rec(self, no, valor):
        if valor < no.valor:
            if no.esq is None:
                no.esq = No(valor)
            else:
                self._inserir_rec(no.esq, valor)

        elif valor > no.valor:
            if no.dir is None:
                no.dir = No(valor)
            else:
                self._inserir_rec(no.dir, valor)

    def analisar_arvore(self, valor_busca):
        """
        Exibe um diagnóstico geral da árvore
        e um diagnóstico específico do nó pesquisado.
        """

        print("=" * 55)
        print("         DIAGNÓSTICO GERAL DA ÁRVORE")
        print("=" * 55)

        # Verificação da raiz
        if self.raiz is None:
            print("Árvore vazia.")
            return

        print(f"Raiz: {self.raiz.valor} (id={id(self.raiz)})")

        print("\n--- Nós Internos (possuem ao menos 1 filho) ---")
        self.imprimir_nos_internos()

        print("\n--- Nós Externos / Folhas (grau 0) ---")
        self.imprimir_folhas()

        print("\n--- Exibição por Níveis ---")
        self.imprimir_niveis()

        # Diagnóstico do nó pesquisado
        no_alvo = self._buscar(self.raiz, valor_busca)

        print("\n" + "=" * 55)
        print(f"   DIAGNÓSTICO ESPECÍFICO → nó {valor_busca}")
        print("=" * 55)

        if no_alvo is None:
            print(f"Valor {valor_busca} não encontrado na árvore.")
        else:
            grau = self._grau(no_alvo)
            altura = self.calcular_altura(no_alvo)
            profundidade = self.calcular_profundidade(valor_busca)

            print(f"Valor              : {no_alvo.valor}")
            print(f"id/endereço        : {id(no_alvo)}")
            print(f"Grau               : {grau}", end=" ")
            print(f"({'raiz/interno' if grau > 0 else 'folha'})")
            print(f"Altura             : {altura}")
            print(f"Profundidade       : {profundidade}")

            print("\nAncestrais (nó → raiz):")
            self.imprimir_ancestrais(valor_busca)

            print("\nDescendentes:")
            self.imprimir_descendentes(valor_busca)

        print("=" * 55)

    # ------------------------------------------------------------ #

    def imprimir_nos_internos(self):
        """Imprime todos os nós que possuem filhos."""
        internos = []
        self._coletar_internos(self.raiz, internos)

        if internos:
            for no in internos:
                filhos = []

                if no.esq:
                    filhos.append(f"esq={no.esq.valor}")

                if no.dir:
                    filhos.append(f"dir={no.dir.valor}")

                print(f"{no.valor} → filhos: {', '.join(filhos)}")
        else:
            print("(nenhum nó interno)")

    def _coletar_internos(self, no, lista):
        if no is None:
            return

        if no.esq is not None or no.dir is not None:
            lista.append(no)

        self._coletar_internos(no.esq, lista)
        self._coletar_internos(no.dir, lista)

    # ------------------------------------------------------------ #

    def imprimir_folhas(self):
        """Imprime todos os nós folha."""
        folhas = []
        self._coletar_folhas(self.raiz, folhas)

        if folhas:
            print(" | ".join(str(f.valor) for f in folhas))
        else:
            print("(árvore vazia)")

    def _coletar_folhas(self, no, lista):
        if no is None:
            return

        if no.esq is None and no.dir is None:
            lista.append(no)

        self._coletar_folhas(no.esq, lista)
        self._coletar_folhas(no.dir, lista)

    # ------------------------------------------------------------ #

    def imprimir_niveis(self):
        """Usa BFS para exibir os nós por nível."""

        if self.raiz is None:
            return

        fila = deque([(self.raiz, 0)])
        nivel_atual = -1

        while fila:
            no, nivel = fila.popleft()

            if nivel != nivel_atual:
                nivel_atual = nivel
                print(f"\nNível {nivel}: ", end="")

            print(f"{no.valor}(id={id(no)})", end="  ")

            if no.esq:
                fila.append((no.esq, nivel + 1))

            if no.dir:
                fila.append((no.dir, nivel + 1))

        print()

    # ------------------------------------------------------------ #

    def calcular_altura(self, no):
        """Retorna a altura do nó."""
        if no is None:
            return -1

        return 1 + max(
            self.calcular_altura(no.esq),
            self.calcular_altura(no.dir)
        )

    # ------------------------------------------------------------ #

    def calcular_profundidade(self, valor):
        """Retorna a profundidade do nó."""
        return self._prof_rec(self.raiz, valor, 0)

    def _prof_rec(self, no, valor, nivel):
        if no is None:
            return -1

        if no.valor == valor:
            return nivel

        if valor < no.valor:
            return self._prof_rec(no.esq, valor, nivel + 1)

        return self._prof_rec(no.dir, valor, nivel + 1)

    # ------------------------------------------------------------ #

    def imprimir_ancestrais(self, valor):
        """Mostra o caminho do nó até a raiz."""
        caminho = []
        self._coletar_ancestrais(self.raiz, valor, caminho)

        if caminho:
            print(" → ".join(str(v) for v in caminho))
        else:
            print("(nó é a raiz — sem ancestrais)")

    def _coletar_ancestrais(self, no, valor, caminho):
        if no is None:
            return False

        if no.valor == valor:
            return True

        if (
            self._coletar_ancestrais(no.esq, valor, caminho)
            or self._coletar_ancestrais(no.dir, valor, caminho)
        ):
            caminho.append(no.valor)
            return True

        return False

    # ------------------------------------------------------------ #

    def imprimir_descendentes(self, valor):
        """Mostra os descendentes do nó pesquisado."""

        no_alvo = self._buscar(self.raiz, valor)

        if no_alvo is None:
            print(f"Valor {valor} não encontrado.")
            return

        desc = []

        self._coletar_descendentes(no_alvo.esq, desc)
        self._coletar_descendentes(no_alvo.dir, desc)

        if desc:
            print(" | ".join(str(d.valor) for d in desc))
        else:
            print("(nó folha — sem descendentes)")

    def _coletar_descendentes(self, no, lista):
        if no is None:
            return

        lista.append(no)

        self._coletar_descendentes(no.esq, lista)
        self._coletar_descendentes(no.dir, lista)

    # ------------------------------------------------------------ #

    def _buscar(self, no, valor):
        if no is None:
            return None

        if no.valor == valor:
            return no

        if valor < no.valor:
            return self._buscar(no.esq, valor)

        return self._buscar(no.dir, valor)

    def _grau(self, no):
        """Retorna o número de filhos do nó."""
        return (1 if no.esq else 0) + (1 if no.dir else 0)


if __name__ == "__main__":
    arvore = ArvoreBST()

    valores = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]

    for v in valores:
        arvore.inserir(v)

    # Analisar a árvore buscando o nó 30
    arvore.analisar_arvore(30)
"""
------------------------------------------------------------
FATEC - São Caetano do Sul
Disciplina: Estruturas de Dados
Atividade Prática: Manipulação de Dicionários (CRUD)

Data: 14/03/2026
Nome: David Lima Alves

Objetivo:
Implementar as operações fundamentais de um sistema
de cadastro utilizando a estrutura de dados
Dicionário em Python, aplicando conceitos de
abstração e persistência em memória.
------------------------------------------------------------
"""

catalogo = {}


def adicionar_filme(id_filme, titulo, diretor):
    """Insere um novo filme se o ID não existir."""

    if id_filme in catalogo:
        print("Esse ID já existe.")
    else:
        catalogo[id_filme] = {
            "titulo": titulo,
            "diretor": diretor
        }
        print("Filme adicionado com sucesso.")


def buscar_filme(id_filme):
    """Consulta um filme usando o método seguro .get()."""

    filme = catalogo.get(id_filme)

    if filme:
        print(f"ID: {id_filme}")
        print(f"Título: {filme['titulo']}")
        print(f"Diretor: {filme['diretor']}")
    else:
        print("Filme não encontrado.")


def remover_filme(id_filme):
    """Remove um filme do dicionário usando .pop()."""

    removido = catalogo.pop(id_filme, None)

    if removido:
        print("Filme removido com sucesso.")
    else:
        print("ID não encontrado.")


def listar_todos():
    """Itera sobre os itens do dicionário para listagem."""

    if not catalogo:
        print("\nO catálogo está vazio.")
    else:
        print("\n--- Listagem de Filmes ---")

        for id_f, dados in catalogo.items():
            print(f"ID: {id_f} | Título: {dados['titulo']} | Diretor: {dados['diretor']}")


adicionar_filme(1, "Interestelar", "Christopher Nolan")
adicionar_filme(2, "Titanic", "James Cameron")
adicionar_filme(1, "Avatar", "James Cameron")

print()

buscar_filme(1)
print()

buscar_filme(3)
print()

listar_todos()
print()

remover_filme(2)
print()

listar_todos()
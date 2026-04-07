# Atividade B1-4
# Simulador HP12c - Pilha RPN com Menu
# Disciplina: Estruturas de Dados - Fatec SCS
# Autores: Tiago B, David L, Pedro H. Lopes
# Data: 31.03.2026

pilha = [0.0, 0.0, 0.0, 0.0] 
tamanho_pilha = 0

def mostrar_pilha():
    print(f"T: {pilha[3]:.2f} Z: {pilha[2]:.2f} Y: {pilha[1]:.2f} X: {pilha[0]:.2f}")

def empilhar(valor):
    global tamanho_pilha
    pilha[3] = pilha[2] 
    pilha[2] = pilha[1]  
    pilha[1] = pilha[0]  
    pilha[0] = valor     
    tamanho_pilha += 1
    mostrar_pilha()

def operar(op):
    global tamanho_pilha
    if tamanho_pilha < 2:
        print("Erro: faltando itens")
        return
    
    x = pilha[0] 
    y = pilha[1]  
    
    if op == '+':
        resultado = y + x
    elif op == '-':
        resultado = y - x  # Y menos X
    elif op == '*':
        resultado = y * x
    elif op == '/':
        if x == 0.0:
            print("Erro: divisão por zero")
        else:
            resultado = y / x 
    else:
        print("Erro: operador inválido")
        
    pilha[0] = resultado
    
    pilha[1] = pilha[2] 
    pilha[2] = pilha[3] 
    pilha[3] = 0.0 
    
    tamanho_pilha -= 1
    mostrar_pilha()

def avaliar(expressao):
    tokens = expressao.split()
    for token in tokens:
        if token in ['+', '-', '*', '/']:
            operar(token)
        else:
            valor = float(token)  
            empilhar(valor)

    print(f"\nResultado Final: {pilha[0]:.2f}")

def limpar():
    global tamanho_pilha
    pilha[:] = [0.0, 0.0, 0.0, 0.0]
    tamanho_pilha = 0
    print("Pilha limpa")
    mostrar_pilha()

while True:
    print("\nCALCULADORA HP12c")
    print("1 - Resolver expressão RPN")
    print("2 - Mostrar pilha")
    print("3 - Limpar pilha")
    print("0 - Sair")
    opcao = input("Escolha: ")
    
    if opcao == "1":
        expr = input("Expressão RPN: ")
        avaliar(expr)
    elif opcao == "2":
        mostrar_pilha()
    elif opcao == "3":
        limpar()
    elif opcao == "0":
        break
    else:
        print("Opção inválida")
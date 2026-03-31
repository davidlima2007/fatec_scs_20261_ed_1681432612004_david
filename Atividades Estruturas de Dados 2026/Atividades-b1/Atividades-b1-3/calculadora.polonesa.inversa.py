"""----------------------------------------------------------------------------------
FATEC-São Caetano do Sul, São Paulo.
Id da Atividade: ED-Atividade-B1-3
Estrutura de Dados
Data: 31/03/2026
Nome: David Lima Alves

Objetivo: Criar uma aplicação que simule a lógica de funcionamento da calculadora 
financeira HP12c, utilizando o conceito de estrutura de dados do tipo pilha (stack) 
para processar expressões em Notação Polonesa Reversa (RPN).
----------------------------------------------------------------------------------"""

def empilhar(lista, numero):
    lista.pop(0)
    lista.append(numero)

def realizar_operacao(lista, operador):
    valor1 = lista.pop()
    valor2 = lista.pop()
    
    if operador == "+":
        resultado = valor2 + valor1
        print("+")
    elif operador == "-":
        resultado = valor2 - valor1
        print("-")
    elif operador == "*":
        resultado = valor2 * valor1
        print("*")
    elif operador == "/":
        resultado = valor2 / valor1
        print("/")
    else:
        print("Erro: caractere inválido")
        return
    
    topo_aux = lista[0]
    lista.insert(0, topo_aux)
    lista.append(resultado)

def mostrar_lista(lista):
    valor4 = lista[0]
    valor3 = lista[1]
    valor2 = lista[2]
    valor1 = lista[3]
    
    print(f"T: {valor4}")
    print(f"Z: {valor3}")
    print(f"Y: {valor2}")
    print(f"X: {valor1}")
    print("--------")

rpn = input("Digite a expressão RPN: ")
lista = [0, 0, 0, 0]
lista_alg = []

quantidade_elementos = rpn.split()

for i in quantidade_elementos:
    try:
        valor = float(i)
        empilhar(lista, valor)
        lista_alg.append(str(valor))
        mostrar_lista(lista)
    except ValueError:
        if len(lista_alg) < 2:
            print("Erro: operador sem valores suficientes")
            break
        
        realizar_operacao(lista, i)
        
        a = lista_alg.pop()
        b = lista_alg.pop()
        c = "(" + b + " " + i + " " + a + ")"
        lista_alg.append(c)
        
        mostrar_lista(lista)

if len(lista_alg) > 1:
    print("Erro: expressão inválida, faltam operadores")
elif len(quantidade_elementos) < 2:
    print("Erro: expressão incorreta")
else:
    print(f"Expressão infixa: {c}")
    print(f"Resultado final: {lista[3]}")
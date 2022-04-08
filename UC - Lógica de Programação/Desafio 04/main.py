import os
from time import sleep
# Faça um algoritmo/app para ler o código, nome e o preço de 15 produtos, calcular e escrever:
# - o maior preço lido;
# - o menor preço lido;
# - a média aritmética dos preços dos produtos.

nomes = list()
precos = list()


def limpar():
    os.system('cls') or None


def menu():
    limpar()
    print("-=-" * 8)
    print("         Menu")
    print("-=-" * 8)

    print("1 - Cadastrar Produtos \n2 - Estatisticas \n3 - Sair")
    opc = int(input("Opção: "))
    return opc


def cadastraProdutos():
    while (1):
        limpar()
        print("-=-" * 8)
        print("  CADASTRO DE PRODUTOS")
        print("-=-" * 8)

        nome = str(input("Nome do Produto: ")).strip()
        preco = float(input("Preço: R$"))

        nomes.append(nome)
        precos.append(preco)
        print("-" * 24)
        print("Cadastro realizado!")
        print("\n1 - Continuar\n2 - Sair")
        x = int(input("Opção: "))
        if (x == 2):
            break


def exibeEstatisticas():
    menor = quant = maior = soma = 0
    for i in precos:
        if (quant == 0):
            maior = menor = i
        elif (i < menor):
            menor = i
        elif (i > maior):
            maior = i
        quant += 1
        soma += i
    
    media = soma/quant

    print(f"Menor preço: R${menor}")
    print(f"Maior preço: R${maior}")
    print(f"Media: R${media}")
    print(f"Quantidade: {quant} unidades\n")

    print("-=-" * 8) 
    print("Exibindo produtos:")
    for i in range(len(nomes)):
        print("-=-" * 8)       
        print(f'Nome: {nomes[i]}')
        print(f'Preço: {precos[i]}')
    x = input("\nPressione qualquer tecla para voltar ao menu")


while True:
    opcao = menu()
    limpar()

    if opcao == 1:
        cadastraProdutos()
    elif opcao == 2:
        exibeEstatisticas()
    elif opcao == 3:
        break

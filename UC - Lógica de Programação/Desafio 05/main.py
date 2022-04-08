import os
from time import sleep
# A prefeitura de uma cidade deseja fazer uma pesquisa entre seus habitantes. Faça um algoritmos
# para coletar dados sobre o salário e número de filhos de cada habitante e após as leituras, escrever:
# a) Média de salário da população;
# b) Média do número de filhos;
# c) Maior salário dos habitantes;
# d) Percentual de pessoas com salário menor que R$ 150,00.

nomes = []
salarios = []
filhos = []


def limpar():
    os.system('cls') or None


def menu():
    limpar()
    print("-=-" * 8)
    print("         Menu")
    print("-=-" * 8)

    print("1 - Cadastrar Pessoas \n2 - Estatisticas \n3 - Sair")
    opc = int(input("Opção: "))
    return opc


def cadastraPessoas():
    while (1):
        limpar()
        print("-=-" * 8)
        print("   CADASTRO DE PESSOAS")
        print("-=-" * 8)

        nome = str(input("Nome: ")).strip()
        filho = int(input("Quantidade de Filhos: "))
        salario = float(input("Salário: R$"))

        if (salario < 0):
            break

        nomes.append(nome)
        filhos.append(filho)
        salarios.append(salario)
        print("Cadastro realizado!")
        sleep(0.5)


def exibePessoas():
    soma_salarios = quant = quant_filhos = menos_de_150 = maior = 0
    for i in range(len(nomes)):
        soma_salarios += salarios[i]
        quant += 1
        quant_filhos += filhos[i]
        if (salarios[i] < 150):
            menos_de_150 += 1
        if (salarios[i] > maior):
            maior = salarios[i]

    media = soma_salarios / quant
    media_filhos = quant_filhos / quant
    porc = (100 * menos_de_150) / quant

    print(f'Media Salarial: R${media}')
    print(f'Media de filhos: {media_filhos}')
    print(f'Quantidade de Pessoas: {quant}')
    print(f'Maior Salario: {maior}')
    print(f'Percentual de menos de 150 reais: {porc}%')
    print("-=-" * 10)

    print("Exibindo Cadastrados:")
    for i in range(len(nomes)):
        print("-=-" * 10)
        print(f'Nome: {nomes[i]}')
        print(f'Quantidade de Filhos: {filhos[i]}')
        print(f'Salário: R${salarios[i]}')
    x = input("\nPressione qualquer tecla para voltar ao menu")


while True:
    opcao = menu()
    limpar()

    if opcao == 1:
        cadastraPessoas()
    elif opcao == 2:
        exibePessoas()
    elif opcao == 3:
        break
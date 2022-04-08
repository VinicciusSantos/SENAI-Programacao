from time import sleep
import os

nomes = list()
idades = list()
matriculas = list()


def limpar():
    os.system('cls') or None


def menu():
    limpar()
    print("-=-" * 8)
    print("         Menu")
    print("-=-" * 8)

    print("1 - Cadastrar Alunos \n2 - Ver Cadastros \n3 - Sair")
    opc = int(input("Opção: "))
    return opc


def cadastraAlunos():
    print("-=-" * 8)
    print("  CADASTRO DE ALUNOS")
    print("-=-" * 8)

    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    matricula = int(input("Matricula: "))

    nomes.append(nome)
    idades.append(idade)
    matriculas.append(matricula)
    print("Cadastro realizado!")
    sleep(0.5)


def exibeAlunos():
    print("Exibindo participantes:")
    for i in range(len(nomes)):
        print("-=-" * 10)
        print(f'Nome: {nomes[i]}')
        print(f'Idade: {idades[i]}')
        print(f'Matricula: {matriculas[i]}')
    x = input("\nPressione qualquer tecla para voltar ao menu")


while True:
    opcao = menu()
    limpar()

    if opcao == 1:
        cadastraAlunos()
    elif opcao == 2:
        exibeAlunos()
    elif opcao == 3:
        break

    
from time import sleep
import os

quant_cl = 0            # Quantidade total de clientes na pousada
quant_for = 0           # Quantidade total de fornecedores

nomes_cl = []           # Lista dos nomes dos clientes
idades_cl = []          # Lista de idades dos clientes
cpf_cl = []             # Lista de CPFs dos clientes
enderecos_cl = []       # Lista de endereços dos clientes
dias_cl = []            # Lista da quantidade de dias que os clientes ficarão

nomes_for = []          # Lista de nomes dos fornecedores
cnpj_for = []           # Lista de CNPJ dos fornecedores
enderecos_for = []      # Lista de entereços dos fornecedores

verm = '\033[31m'
verde = '\033[32m'
branco = '\033[37m'


def limp():
    os.system('cls') or None

def menu(nome):
    print(f"{verde}-=-" * 10)
    print(f'{branco}{nome.upper():^30}')
    print(f"{verde}-=-{branco}" * 10)


while True:
    limp()
    menu("Menu do programa")
    print("1 - Cadastrar Cliente \n2 - Cadastro de fornecedores \n3 - Exibir Clientes")
    opc = int(input("Escolha: "))

    if (opc == 1):      # Cadastrar clientes
        limp()
        menu("Cadastro de Clientes")
        nome = str(input("Nome do Cliente: ")).upper().strip()

        while True:
            idade = str(input("Idade: "))
            if idade.isnumeric():
                idade = int(idade)
                break
            else:
                print(f"{verm}ERRO! digite a idade novamente{branco}")

        ende = str(input("Onde Você mora? ")).upper().strip()
        cpf = str(input("CPF: ")).strip()
        dias = int(input("Quantidade de dias: "))

        nomes_cl.append(nome)
        idades_cl.append(idade)
        enderecos_cl.append(ende)
        cpf_cl.append(cpf)
        dias_cl.append(dias)
        quant_cl += 1
        print("CADASTRADO!")
        sleep(1)


    elif (opc == 2):    # Cadastrar fornecedores
        limp()
        menu("Cadastro de Fornecedores")
        nome = str(input("Nome do Fornecedor: ")).upper().strip()
        cnpj = str(input("CNPJ: ")).strip()
        ende = str(input("Endereço: ")).upper().strip()

        nomes_for.append(nome)
        cnpj_for.append(cnpj)
        enderecos_cl.append(ende)
        print("CADASTRADO!")
        sleep(1)

    elif (opc == 3):    # Mostrar Cadastrados
        limp()
        menu("mostrando cadastros")
        for i in range(quant_cl):
            
            print(f"Nome: {nomes_cl[i]}")
            print(f'Idade: {idades_cl[i]}')
            print(f'CPF: {cpf_cl[i]}')
            print(f'Endereço: {enderecos_cl[i]}')
            print(f'Quantidade de dias: {dias_cl[i]}')
            print("-" * 30)
            print("\n")

        x = input("Pressione uma tecla para voltar ao MENU...")

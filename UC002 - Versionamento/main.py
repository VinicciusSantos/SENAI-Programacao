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

# -=- Códigos de cores -=-
verm = '\033[31m'
verde = '\033[32m'
branco = '\033[37m'


def limp():
    os.system('cls') or None


def menu(nome):
    print(f"{verde}-=-" * 10)
    print(f'{branco}{nome.upper():^30}')
    print(f"{verde}-=-{branco}" * 10)


def cadastraCliente():
    limp()
    menu("Cadastro de Clientes")
    nome = str(input("Nome do Cliente: ")).upper().strip()

    while True:     # Recebendo e validando as dadas
        idade = str(input("Idade: "))
        if idade.isnumeric():
            idade = int(idade)
            break
        else:
            print(f"{verm}ERRO! digite a idade novamente{branco}")

    ende = str(input("Onde Você mora? ")).upper().strip()

    while True:
        cpf = str(input("Numeros do CPF: ")).strip()
        if len(cpf) != 11:
            print(f"{verm}ERRO! Tamanho inválido{branco}")
        else:
            break

    dias = int(input("Quantidade de dias: "))

    # Confirmando cadastros:
    while True:
        limp()
        menu("Confirmando cadastro")
        print(f"1 - Nome: {nome}")
        print(f'2 - Idade: {idade}')
        print(f'3 - CPF: {cpf}')
        print(f'4 - Endereço: {ende}')
        print(f'5 - Quantidade de dias: {dias}')
        print("-" * 30)
        x = input("Aperte <ENTER> para confirmar cadastro ou um numero para editar")

        if x == '1':
            nome = str(input("Nome do Cliente: ")).upper().strip()
        
        elif x == '2':
            while True:     # Editando e validando as dadas
                idade = str(input("Idade: "))
                if idade.isnumeric():
                    idade = int(idade)
                    break
                else:
                    print(f"{verm}ERRO! digite a idade novamente{branco}")

        elif x == '3':        # Editando o CPF
            while True:
                cpf = str(input("Numeros do CPF: ")).strip()
                if len(cpf) != 11:
                    print(f"{verm}ERRO! Tamanho inválido{branco}")
                else:
                    break

        elif x == '4':        # editando Endereço
            ende = str(input("Onde Você mora? ")).upper().strip()

        elif x == '5':        # Editando quantidade de dias
            dias = int(input("Quantidade de dias: "))

        else:
            break

    nomes_cl.append(nome)
    idades_cl.append(idade)
    enderecos_cl.append(ende)
    cpf_cl.append(cpf)
    dias_cl.append(dias)
    print("CADASTRADO!")
    sleep(1)


def cadastraFornecedor():
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


def exibeCadastrados():
    limp()
    menu("mostrando cadastros")

    if quant_cl == 0:
        print(f"{verm}ERRO! Nenhum Cliente cadastrado{branco}")
        input("Pressione uma tecla para voltar ao MENU...")
        return

    for i in range(quant_cl):        
        print(f"Nome: {nomes_cl[i]}")
        print(f'Idade: {idades_cl[i]}')
        print(f'CPF: {cpf_cl[i]}')
        print(f'Endereço: {enderecos_cl[i]}')
        print(f'Quantidade de dias: {dias_cl[i]}')
        print("-" * 30)

    input("Pressione uma tecla para voltar ao MENU...")

while True:     # MENU PRINCIPAL
    limp()
    menu("Programa Code +")
    print("1 - Cadastrar Cliente \n2 - Cadastro de fornecedores \n3 - Exibir Clientes \n4 - Sair")
    opc = int(input(f"{verde}Escolha: {branco}"))

    if opc == 1: 
        cadastraCliente()
        quant_cl += 1

    elif opc == 2: 
        cadastraFornecedor()
        quant_for += 1

    elif opc == 3: 
        exibeCadastrados()
    
    elif opc == 4:
        limp()
        print(f"{verm}Encerrando programa!{branco}")
        sleep(1)
        break

    else:
        print(f"{verm}ERRO! Opção Inválida!{branco}")
        sleep(1)
        
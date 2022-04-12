from asyncio.windows_events import NULL
from tarfile import NUL
from time import sleep
import os
import csv

# -=- Preços dos pacotes individuais -=-
preco_diaria_ind = 200.00
preco_pacote1_ind = 1130.00
preco_pacote2_ind = 2520.00
preco_pacote3_ind = 4500.00

# -=- Preços dos pacotes Duplas -=-
preco_diaria_dupla = 350.00
preco_pacote1_dupla = 1130.00
preco_pacote2_dupla = 4655.00
preco_pacote3_dupla = 9975.00

produtos_nomes_for = []       # Lista temporária de nomes dos produtos dos fornecedores
produtos_preco_for = []       # Lista temporária de preços dos produtos dos fornecedores
produtos_quant_for = []       # Lista temporária de quantidades de cada produto fornecido

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


def box(titulo, *caracteristicas):
    print(f"{verde}-=-" * 10)
    print("|", end='')
    print(f'{branco}{titulo.upper():^28}{verde}', end='')
    print("|")
    print(f"-=-" * 10)

    for c in caracteristicas:
        print("|", end='')
        print(f" {branco}{c:^27}", end='')
        print(f"{verde}|")
    print(f"{verde}-{branco}" * 30)


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

    while True:     # Recebendo e validando o CPF
        cpf = str(input("Numeros do CPF: ")).strip()
        if len(cpf) != 11:
            print(f"{verm}ERRO! Tamanho inválido{branco}")
        else:
            break
    cpf = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

    # Confirmando cadastros:
    while True:
        limp()
        menu("Confirmando cadastro")
        print(f"1 - Nome: {nome}")
        print(f'2 - Idade: {idade}')
        print(f'3 - CPF: {cpf}')
        print(f'4 - Endereço: {ende}')
        print("-" * 30)
        x = input("Aperte <ENTER> para confirmar cadastro ou um numero para editar: ")

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

        else:
            break

    print("CADASTRADO!")
    sleep(0.5)

    while True: # Escolhendo plano individual ou dupla
        limp()
        menu("Escolha um plano")
        print("1 - Individual \n2 - Dupla")
        pessoas_plano = int(input(f"{verde}Opção: {branco}"))
        
        if pessoas_plano == 1 or pessoas_plano == 2:
            break
        else:
            print(f"{verm}ERRO! escolha um plano válido! {branco}")
            sleep(1)

    acompanhante = NULL
    if pessoas_plano == 1:
        box('Diaria', f'R${preco_diaria_ind}')
        box('1º Pacote', 'Uma semana', '10% de desconto', f'Total = R${preco_pacote1_ind}')
        box('2º Pacote', 'Duas semanas', '15% de desconto', f'Total = R${preco_pacote2_ind}')
        box('3º Pacote', '30 dias', '25% de desconto', f'Total = R${preco_pacote3_ind}')

    elif pessoas_plano == 2:
        acompanhante = str(input("Nome do acompanhante: ")).strip().upper() 

        box('Diaria', f'R${preco_diaria_dupla}')
        limp()
        box('1º Pacote', 'Uma semana', '10% de desconto', f'Total = R${preco_pacote1_dupla}')
        box('2º Pacote', 'Duas semanas', '15% de desconto', f'Total = R${preco_pacote2_dupla}')
        box('3º Pacote', '30 dias', '25% de desconto', f'Total = R${preco_pacote3_dupla}')  
        
    quant_dias = int(input('Quantidade de dias: '))
          
    cp_dias = quant_dias    # Cópia da variavel dias

    # -=- Calculando o preço à ser pago pelo cliente -=-
    preco = 0
    quant_p1 = quant_p2 = quant_p3 = quant_diarias = 0
    while True:
        if cp_dias > 30:                                # plano de 1 mês => 30 dias
            if pessoas_plano == 1:
                preco += preco_pacote3_ind
            elif pessoas_plano == 2:
                preco += preco_pacote3_dupla
            cp_dias -= 30
            quant_p3 += 1

        elif cp_dias >= 14 and cp_dias < 30:            # plano de 2 semanas => 14 dias
            if pessoas_plano == 1:
                preco += preco_pacote2_ind
            elif pessoas_plano == 2:
                preco += preco_pacote2_dupla
            cp_dias -= 14
            quant_p2 += 1

        elif cp_dias >= 7 and cp_dias < 14:             # plano de 1 semana => 7 dias
            if pessoas_plano == 1:
                preco += preco_pacote1_ind
            elif pessoas_plano == 2:
                preco += preco_pacote1_dupla
            quant_p1 += 1
            cp_dias -= 7
        
        elif cp_dias != 0:                              # Planos de diárias
            if pessoas_plano == 1:
                preco += cp_dias * preco_diaria_ind
            elif pessoas_plano == 2:
                preco += cp_dias * preco_diaria_dupla
            quant_diarias = cp_dias
            break

    limp()
    box('Resumo da reserva', f'Nome: {nome}', f'CPF: {cpf}', f'Quatidade de dias: {quant_dias}', f'Preço Final: R${preco:.2f}', '-=--=--=--=--=--=--=-',f'Plano 1 aplicado {quant_p1} vezes', f'Plano 2 aplicado {quant_p2} vezes', f'Plano 3 aplicado {quant_p3} vezes', f'Diarias aplicadas {quant_diarias} vezes')
    input()

    # Gravando as informações no CSV:
    with open('clientes.csv', "+a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nome, idade, ende, cpf, quant_dias, preco, acompanhante])


def cadastraFornecedor():
    produtos_nomes_for.clear()
    produtos_preco_for.clear()
    produtos_quant_for.clear()
    limp()
    menu("Cadastro de Fornecedores")
    nome = str(input("Nome do Fornecedor: ")).upper().strip()

    while True:
        cnpj = str(input("CNPJ: ")).strip()
        if len(cnpj) == 14:
            break
        else:
            print(f"{verm}ERRO! CNPJ Inválido! {branco}")

    ende = str(input("Endereço: ")).upper().strip()
    cnpj = f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}'
    
    # Confirmando cadastros:
    while True:
        limp()
        menu("Confirmando cadastro")
        print(f"1 - Nome: {nome}")
        print(f'2 - CNPJ: {cnpj}')
        print(f'3 - Endereço: {ende}')
        print("-" * 30)
        x = input("Aperte <ENTER> para confirmar cadastro ou um numero para editar: ")

        if x == '1':            # Editando o nome
            nome = str(input("Nome do Fornecedor: ")).upper().strip()
        
        elif x == '2':          # Editando o cnpj
            while True:
                cnpj = str(input("CNPJ: ")).strip()
                if len(cnpj) == 14:
                    break
                else:
                    print(f"{verm}ERRO! CNPJ Inválido! {branco}")
            cnpj = f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}'

        elif x == '3':        # Editando o endereço
            ende = str(input("Endereço: ")).upper().strip()

        else:
            break

    while True:
        limp()
        menu('Cadastro de produtos')
        print(f"Fornecedor: {nome}")
        p_nome = str(input("Digite o nome do produto ou '0': ")).upper().strip()

        if p_nome.strip() == '0':
            break

        p_preco = float(input("Digite o preço unitário: "))
        p_quant = int(input("Digite a quantidade total: "))
        preco_final_produtos = p_preco * p_quant

        # Confirmando cadastros:
        while True:
            limp()
            menu("Confirmando cadastro")
            print(f"1 - Nome do produto: {p_nome}")
            print(f'2 - Preço unitário: R${p_preco:.2f}')
            print(f'3 - Quantidade: {p_quant}')
            print(f"{verde}Preço Final: {branco}R${preco_final_produtos:.2f}")
            print("-" * 30)
            x = input("Aperte <ENTER> para confirmar cadastro ou um numero para editar: ")

            if x == '1':            # Editando o nome
                p_nome = str(input("Digite o nome do produto ou 0: ")).upper().strip()
            
            elif x == '2':          # Editando o preco
                p_preco = int(input("Digite o preço unitário: "))

            elif x == '3':        # Editando a quantidade
                p_quant = int(input("Digite a quantidade total: "))

            else:
                break

        produtos_nomes_for.append(p_nome)
        produtos_preco_for.append(p_preco)
        produtos_quant_for.append(p_quant)

    with open('fornecedores.csv', "+a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nome, cnpj, ende, produtos_nomes_for, produtos_preco_for, produtos_quant_for])

    print("CADASTRADO!")
    sleep(1)


def exibeCadastrados():
    limp()
    menu("mostrando cadastros")
    
    with open('clientes.csv', 'r',) as file:
        reader = csv.reader(file)
        for l in reader:
            print(f'Nome: {l[0]} \nIdade: {l[1]} \nEndereço: {l[2]} \nCPF: {l[3]} \nDias: {l[4]}')
            print("-" * 30)

    input("Pressione uma tecla para voltar ao MENU...")


def exibeFornecedores():
    limp()
    menu("mostrando fornecedores")

    with open('fornecedores.csv', 'r',) as file:
        reader = csv.reader(file)
        for l in reader:
            print(f'Nome: {l[0]} \nCNPJ: {l[1]} \nEndereço: {l[2]} \nProdutos: {l[3]}')
            print("-" * 30)

    input("Pressione uma tecla para voltar ao MENU...")

while True:     # MENU PRINCIPAL
    limp()
    menu("Programa Code +")
    print("1 - Cadastrar Cliente \n2 - Cadastro de fornecedores \n3 - Exibir Clientes \n4 - Exibir Fornecedores \n5 - Sair")
    opc = int(input(f"{verde}Escolha: {branco}"))

    if opc == 1: 
        cadastraCliente()

    elif opc == 2: 
        cadastraFornecedor()

    elif opc == 3: 
        exibeCadastrados()

    elif opc == 4:
        exibeFornecedores()
    
    elif opc == 5:
        limp()
        print(f"{verm}Encerrando programa!{branco}")
        sleep(1)
        break

    else:
        print(f"{verm}ERRO! Opção Inválida!{branco}")
        sleep(1)
       
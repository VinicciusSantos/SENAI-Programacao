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

def quant_linhas(link):
    cont = 0
    with open(link, 'r',) as file:
        reader = csv.reader(file)
        for l in reader:
            cont += 1
    return cont


def limp():
    # Caso use linux: ('clear')
    # Caso use Windows: ('cls')
    os.system('clear') or None


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
    andar1 = quant_linhas("clientes_andar1.csv")        # Quantidade de quartos ocupados no 1º andar
    andar2 = quant_linhas("clientes_andar2.csv")        # Quantidade de quartos ocupados no 2º andar
    disponiveis_andar1 = 10 - andar1
    disponiveis_andar2 = 10 - andar2

    menu("Cadastro de Clientes")
    if (andar1 == 10 and andar2 == 10):
        print(f'{verm}Não há quartos disponíveis!{branco}')
        input("Aperte ENTER para continuar!")
        return
    
    else:
        print(f"< {verde}{disponiveis_andar1}{branco} > Quartos individuais disponiveis")
        print(f"< {verde}{disponiveis_andar2}{branco} > Quartos de casal disponiveis")

        while True:
            print('1 - Continuar \n2 - Voltar')
            x = input(f"{verde}Opcão: {branco}")
            if x == '1':          # Se quiser continuar
                break
            elif x == '2':        # Se quiser voltar ao menu
                return

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

    acompanhante = 0
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
        
    while True:    
        quant_dias = str(input('Quantidade de dias: '))
        if quant_dias.isnumeric():
            quant_dias = int(quant_dias)
            break
        else:
            print(f"{verm}ERRO! Digite um número válido!{branco}")
          
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

        elif cp_dias == 0:
            break


    limp()
    menu('Escolha um quarto')
    ocupados = []
    if pessoas_plano == 1:
        with open('clientes_andar1.csv', "r", newline='') as file:
            reader = csv.reader(file)
            for c in reader:
                ocupados.append(int(c[6]))

            for i in range(10):
                print(verde, end='')
                if i+1 in ocupados:
                    print(verm, end='')

                if i == 5:
                    print('\n')

                if i < 9:
                    print(f'A-0{i+1}{branco}',end='  ')
                else:
                    print(f'A-{i+1}{branco}',end='  ')
    
    elif pessoas_plano == 2:
        with open('clientes_andar1.csv', "r", newline='') as file:
            reader = csv.reader(file)
            for c in reader:
                ocupados.append(int(c[6]))

            for i in range(10):
                print(verde, end='')
                if i+1 in ocupados:
                    print(verm, end='')
                    
                if i == 5:
                    print('\n')

                if i < 9:
                    print(f'A-0{i+1}{branco}',end='  ')
                else:
                    print(f'A-{i+1}{branco}',end='  ')
    
    quarto = input("\nOpção: ").strip().upper()
    limp()
    box('Resumo da reserva', f'Nome: {nome}', f'CPF: {cpf}', f'Quatidade de dias: {quant_dias}', f'Preço Final: R${preco:.2f}', f'Quarto: {quarto}', '-=--=--=--=--=--=--=-',f'Plano 1 aplicado {quant_p1} vezes', f'Plano 2 aplicado {quant_p2} vezes', f'Plano 3 aplicado {quant_p3} vezes', f'Diarias aplicadas {quant_diarias} vezes')
    input()

    # Gravando as informações no CSV:
    if (pessoas_plano == 1):
        with open('clientes_andar1.csv', "+a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([nome, idade, ende, cpf, quant_dias, preco, quarto[-2:-1]])
    
    elif (pessoas_plano == 2):
        with open('clientes_andar2.csv', "+a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([nome, acompanhante, idade, ende, cpf, quant_dias, preco, quarto[-2:-1]])


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
    andar1 = quant_linhas("clientes_andar1.csv")
    andar2 = quant_linhas("clientes_andar2.csv")        # Quartos das duplas
    print(f"Quartos ocupados no 1ª andar: {andar1}")
    print(f"Quartos ocupados no 2ª andar: {andar2}")
    print("-=-"*10)
    
    with open('clientes_andar1.csv', 'r',) as file:
        reader = csv.reader(file)
        for l in reader:
            print(f'Nome: {l[0]} \nIdade: {l[1]} \nEndereço: {l[2]} \nCPF: {l[3]} \nDias: {l[4]} \nPreço: {l[5]} \nQuarto: {l[6]}')
            print("-" * 30)

    with open('clientes_andar2.csv', 'r',) as file:
        reader = csv.reader(file)
        for l in reader:
            print(f'Nome: {l[0]} \nIdade: {l[1]}\nAcompanhante: {l[2]} \nEndereço: {l[3]} \nCPF: {l[4]} \nDias: {l[5]} \nPreço: {l[6]} \nQuarto: {l[7]}')
            print("-" * 30)   
        

    input("Pressione uma tecla para voltar ao MENU...")


def exibeFornecedores():
    limp()
    menu("mostrando fornecedores")

    with open('fornecedores.csv', 'r',) as file:
        reader = csv.reader(file)
        for l in reader:
            print(f'Nome: {l[0]} \nCNPJ: {l[1]} \nEndereço: {l[2]} \nProdutos: {l[3]} \nPreços Unitarios: R${l[4]} \nQuantidades de pedidos: {l[5]}')
            print("-" * 30)

    input("Pressione uma tecla para voltar ao MENU...")


def fazerCheckout():
    limp()
    andar1 = quant_linhas("clientes_andar1.csv")        # Quantidade de QUARTOS ocupados no 1º andar
    andar2 = quant_linhas("clientes_andar2.csv")        # Quantidade de QUARTOS ocupados no 2º andar
    menu("Chekout")

    while True:             # Recebendo o quarto e validando
        andar = quarto = errado = 0
        input_quarto = str(input("Qual o quarto? ")).strip().upper()
        # quarto[0] == andar que a pessoa está
        # quarto[1] == separador: "-" 
        # quarto[2:3] == quarto que a pessoa está

        # Verificando o andar (A - Individual | B - Casal)
        if len(input_quarto) != 4:
            print(f"{verm}ERRO! Quarto Inválido! {branco}")

        else:
            if input_quarto[0] == 'A':
                andar = 1
            elif input_quarto[0] == 'B':
                andar = 2 

            quarto = f'{str(input_quarto[2])}{str(input_quarto[3])}'   # número do quarto sempre é formado por 2 algarismos
            if quarto.isnumeric():
                quarto = int(quarto)
            else:
                errado = 1

            if andar == 0 or input_quarto[1] != '-' or errado == 1:
                print(f"{verm}ERRO! Quarto Inválido! {branco}")

            else:   # Validar pra ver se tem alguem no quarto indicado
                if (andar == 1 and andar1 < quarto) or (andar == 2 and andar2 < quarto): 
                    print(f"{verm}ERRO! Esse quarto já estava vazio! {branco}")
                else:
                    break
    
    # Imprimindo os dados do cliente para a confirmação do checkout:
    limp()
    if andar == 1:      # quartos individuais
        with open('clientes_andar1.csv', 'r',) as file:
            reader = csv.reader(file)
            for i, l in enumerate(reader):
                if i+1 == quarto:
                    box(f'Nome: {l[0]}', f'Idade: {l[1]}', f'Endereço: {l[2]}', f'CPF: {l[3]}', f'Dias: {l[4]}', f'Preço: {l[5]}', f'Quarto: {l[6]}')
                    break

    elif andar == 2:    # quartos de casal
        with open('clientes_andar2.csv', 'r',) as file:
            reader = csv.reader(file)
            for i, l in enumerate(reader):
                if i+1 == quarto:
                    box(f'Nome: {l[0]}', f'Acompanhante: {l[1]}', f'Idade: {l[2]}', f'Endereço: {l[3]}', f'CPF: {l[4]}', f'Dias: {l[5]}', f'Preço: {l[6]}', f'Quarto: {l[7]}')
                    break
    
    while True:
        confirma = (str(input("Confirma o cadastro? [S-N] "))).strip().upper()
        if confirma == 'N' or confirma == 'S':
            break
    
    if confirma == 'N':
        print(f"{verm}Chekcout cancelado!{branco}")
        print("Voltando ao MENU...")
        sleep(2)
        return

    # Se o o checkout for confirmado:
    print("Beleza meu chapa")
    x = input()
            

while True:     # MENU PRINCIPAL
    limp()
    #box('Programa Code +', '1 - Cadastrar Cliente', '2 - Cadastrar fornecedores', '3 - Exibir Clientes', '4 - Exibir Fornecedores', '5 - Fazer Checkout', '6 - Sair')
    menu("Programa Code +")
    print("1 - Cadastrar Cliente \n2 - Cadastrar fornecedores \n3 - Exibir Clientes \n4 - Exibir Fornecedores \n5 - Fazer Checkout \n6 - Sair")
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
        fazerCheckout()
    
    elif opc == 6:
        limp()
        print(f"{verm}Encerrando programa!{branco}")
        sleep(1)
        break

    else:
        print(f"{verm}ERRO! Opção Inválida!{branco}")
        sleep(1)
       
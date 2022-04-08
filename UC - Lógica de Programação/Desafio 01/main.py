import csv
import os
from datetime import datetime
from json.encoder import ESCAPE_ASCII
import pandas as pd


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def linha(qtd=10):
    print("-=-" * qtd)


def continuar():
    input("PRESSIONE ENTER PARA VOLTAR AO MENU...")
    clear()


escolha = 0
#df = pd.read_csv("dados.csv")
list = ['Palestrante', 'Estudante']
while escolha != 4:
    qtd_pessoas = 0
    #total_rows=len(df.axes[0])

    while True:
        linha()
        print("             MENU")
        linha()

        print("1 - Cadastrar Evento \n2 - Cadastrar Participantes \n3 - Ver participantes \n4 - Sair\n")
        escolha = int(input("Escolha uma opção: "))
        
        if escolha == 1:
            clear()
            linha()
            print("     CADASTRO DE EVENTO")
            linha()


            #if total_rows+1 > 100:
            #    print("Maximo de pessoas atingidas!")
            #    continuar()
            #    break

            data_dia = int(input("Qual o dia do evento? dd "))
            data_mes = int(input("Qual o mes do evento? mm "))
            data_ano = int(input("Qual o ano do evento? yyyy "))

            hoje_dia = int(datetime.today().strftime('%d'))
            hoje_mes = int(datetime.today().strftime('%m'))
            hoje_ano = int(datetime.today().strftime('%Y'))

            if (data_dia < hoje_dia and data_mes <= hoje_mes and data_ano <= hoje_ano) or data_ano < hoje_ano:
                print("\nData Inválida!\n")
                continuar()
                break
            
            print("\nMarcado!")
            continuar()
            break

        elif escolha == 2:
            clear()
            linha()
            print("   CADASTRO DE PARTICIPANTE")
            linha()

            print("1 - Palestrante \n2 - Estudante")
            opc = int(input("Opção: "))
            idade = int(input("\nQual a sua idade? "))

            if idade < 18:
                print("O cadastro não permitido pela idade!")
                continuar()
                break

            nome = str(input('Qual o seu nome? '))
            with open('dados.csv', "+a", newline='') as file:
                writer = csv.writer(file)
                writer.writerow([list[opc], nome, idade])

            print("Idade Permitida, Cadastro feito!")
            qtd_pessoas += 1
            continuar()
            break

        elif escolha == 3:
            clear()
            linha()
            print("    LISTA DE PARTICIPANTES")
            linha()

            with open('dados.csv', 'r',) as file:
                reader = csv.reader(file)
                for l in reader:
                    print(f'{l[0]}: \nNome: {l[1]} \nIdade: {l[2]}\n')

                continuar()
                break
        
        elif escolha == 4:
            print("Tchau!\n")
            break

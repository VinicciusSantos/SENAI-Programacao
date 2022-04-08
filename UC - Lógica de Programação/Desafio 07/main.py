quant_litros = int(input("Quantidade de litros: "))
print("Tipo de combustivel: \n[1] - Álcool \n[2] - Gasolina")
tipo = int(input("Opção: "))

preco = tot = desc = 0
if (tipo == 1):
    preco = quant_litros * 3.3

    if (quant_litros <= 20):
        desc = 3.3 * 97 / 100
    else:
        desc = 3.3 * 95 / 100

elif (tipo == 2):
    preco = quant_litros * 2.9

    if (quant_litros <= 20):
        desc = 2.9 * 96 / 100
    else:
        desc = 2.9 * 94 / 100

preco2 = quant_litros * desc

print(f"Preço total: R${preco}")
print(f"Desconto por litro: R${desc}")
print(f"Preço final: R${preco2}")
from random import randint

num = 5
txt = 'oi'
valor = False

print(type(num))
print(type(txt))
print(type(valor))

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
print()

lista = []
lista.append(num)
lista.append(txt)
lista.append(valor)
print(lista)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
print()

if randint(1,2) == 1:
    print("foi")
else:
    print("N foi")

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
print()

for i in range(5):
    print('#' * i)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
print()

print("CALCULADORA")
n1 = int(input("Digite o 1 num: "))
n2 = int(input("Digite o 2 num: "))
print(f"Soma: {n1+n2}")

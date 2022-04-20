import csv, os

lista = []
lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)
lista.append(5)
lista.append(6)

for c in lista:
    if c == 5:
        lista.remove(c)

print(lista)
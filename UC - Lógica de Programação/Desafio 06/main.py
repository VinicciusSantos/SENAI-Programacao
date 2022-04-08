from time import sleep
import os

os.system('cls') or None

h1 = int(input('Digite a idade de um Homem: '))
h2 = int(input("Digite a idade de outro homem: "))
m1 = int(input('Digite a idade de uma mulher: '))
m2 = int(input("Digite a idade de outra mulher: "))

if (h1 > h2):
    maior_h = h1
    menor_h = h2
else:
    maior_h = h2
    menor_h = h1

if (m1 > m2):
    maior_m = m1
    menor_m = m2

else:
    maior_m = m2
    menor_m = m1

print(f"\nsoma das idades do homem mais velho com a mulher mais nova: {maior_h + menor_m}")
print(f"produto das idades do homem mais novo com a mulher mais velha: {menor_h * maior_m}")
print("-=-" * 8)
num, gran = input("Digite uma medida e sua grandeza: ")
print("-=-" * 8)


if gran == 'pol':
    numerador, denominador = num.split('/')
    div = float(numerador)/float(denominador)
    print(f'Polegadas Milesimais: {div:.3f} pol')
    print(f'Milimetros: {(div*25.4):.2f} mm')
    print(f'Centimetros: {(div * 2.54):.2f} cm')

elif gran == 'mm':
    num = float(num)
    pol_num = int((num / 25.4) * 128)
    pol_den = 128

    while pol_num % 2 == 0 and pol_den % 2 == 0:
        pol_num /= 2
        pol_den /= 2

    print(f'Polegadas Fracionarias: {int(pol_num)/int(pol_den):.3f} pol')
    print(f'Polegadas Milesimais: {(num / 25.4):.3f} mm')
    print(f'Centimetros: {(num / 10):.2f} cm')
    
def box(titulo, *caracteristicas):
    print("-" * 40)
    print(f'{titulo:^38}', end=None)
    print("-" * 40)

    for c in caracteristicas:
        print("|  ", end=None)
        print(f"{c:<38}")
        print("|")
    print("-" * 40)


box('1º Pacote', 'Uma semana', '10% de desconto', 'Total = R$1449')
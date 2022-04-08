horas_mes = int(input("Horas trabalhadas no mês: "))
horas_semana = horas_mes / 4

salario_por_hora = float(input("Salário por hora: "))

bonus = 0
if (horas_semana > 40):
    bonus = (horas_semana - 40) * (salario_por_hora / 2) * 4

salario_total = (salario_por_hora * horas_mes) + bonus
print(f"Salario Total: {salario_total}")

# Calcular a faixa de IRPF que você está inserido
# Calcular quanto de IR uma pessoa paga!

salario = float(input("Digite o seu salario ..."))
irpf = 0.0
imposto = 0.0

if salario <= 1903.99:
  irpf = 0.0
  imposto = 0.0
  print("Você ganha pouco mas é feliz ... não paga IRPF!")
elif salario > 1903.99 and salario <= 2826.75:
  irpf = 7.5/100
  imposto = irpf*(salario - 1903.99)
elif salario > 2826.75 and salario <= 3751.05:
  irpf = 15/100
  imposto = irpf*(salario - 1903.99) + (2826.75 - 1903.99)*7.5/100
elif salario > 3751.05 and salario <= 4664.68:
  irpf = 22.5/100
  imposto = irpf*(salario - 3751.05) + (3751.05 - 2826.75)*15.0/100 + (2826.75 - 1903.99)*7.5/100
elif salario > 4664.68:
  irpf = 27.5/100
  imposto = irpf*(salario - 4664.68) + (4664.68 - 3751.05)*22.5/100 + (3751.05 - 2826.75)*15.0/100 + (2826.75 - 1903.99)*7.5/100


print("Você vai pagar R$ " + str(imposto) + " de IRPF!")
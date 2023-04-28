# Atividade 1
import math

valorTotal = float(f"{float(input('Digite o valor em reais:')):.2f}")
notas100 = math.floor(valorTotal / 100)
valorTotal -= notas100 * 100
notas50 = math.floor(valorTotal / 50)
valorTotal -= notas50 * 50
notas20 =  math.floor(valorTotal / 20)
valorTotal -= notas20 * 20
notas10 = math.floor(valorTotal / 10)
valorTotal -= notas10 * 10
notas5 = math.floor(valorTotal / 5)
valorTotal -= notas5 * 5
notas2 = math.floor(valorTotal / 2)
valorTotal -= notas2 * 2
moedas1 = math.floor(valorTotal / 1)
valorTotal -= moedas1
moedas50 = math.floor(valorTotal / 0.5)
valorTotal -= moedas50 * 0.5
moedas25 = math.floor(valorTotal / 0.25)
valorTotal -= moedas25 * 0.25
moedas10 = math.floor(valorTotal / 0.10)
valorTotal -= moedas10 * 0.10
moedas5 = math.floor(valorTotal / 0.5)
valorTotal -= moedas5 * 0.5
moedas01 = math.floor(valorTotal / 0.1)
valorTotal -= moedas01 * 0.1
print ("NOTAS:\n",
       notas100, "nota(s) de R$ 100.00\n",
       notas50, "nota(s) de R$ 50.00\n",
       notas20, "nota(s) de R$ 20.00\n",
       notas10, "nota(s) de R$ 10.00\n",
       notas5, "nota(s) de R$ 5.00\n",
       notas2, "nota(s) de R$ 2.00\n",
       "moedas:\n",
       moedas1, "moedas(s) de R$ 1.00\n",
       moedas50, "moedas(s) de R$ 0.50\n",
       moedas25, "moedas(s) de R$ 0.25\n",
       moedas10, "moedas(s) de R$ 0.10\n",
       moedas5, "moedas(s) de R$ 0.05\n",
       moedas01, "moedas(s) de R$ 0.01")

# Atividade 2
mes = int(input("Digite um número:"))
match mes:
  case 1:
    print("Janeiro")
  case 2:
    print("Fevereiro")
  case 3:
    print("Março")
  case 4:
    print("Abril")
  case 5:
    print("Maio")
  case 6:
    print("Junho")
  case 7:
    print("Julho")
  case 8:
    print("Agosto")
  case 9:
    print("Setembro")
  case 10:
    print("Outubro")
  case 11:
    print("Novembro")
  case 12:
    print("Dezembro")

# Atividade 3
valorFinanciamento = float(input("Digite o valor a ser financiado:"))
renda = float(input("Digite sua renda:"))
numParcelas = int(input("Digite o número de parcelas:"))
valorParcela = float(valorFinanciamento / numParcelas)
if valorParcela <= renda * 0.3 and numParcelas <= 180:
  print("Financiamento de R$", f"{valorFinanciamento:.2f}", "aprovado com", numParcelas, "parcelas de R$", f"{valorParcela:.2f}")
else:
  print("Financiamento não aprovado")

# Atividade 4
valorFinanciamento = float(input("Digite o valor a ser financiado:"))
renda = float(input("Digite sua renda:"))
numParcelas = int(input("Digite o número de parcelas:"))
valorParcela = float(valorFinanciamento / numParcelas)
if valorParcela <= renda * 0.3 and numParcelas <= 180:
  print("Financiamento de R$", f"{valorFinanciamento:.2f}", "aprovado com", numParcelas, "parcelas de R$", f"{valorParcela:.2f}")
else:
  print("Financiamento não aprovado")

# Atividade 5
salario = float(input("Digite seu salário em reais:"))
imposto = 0
if salario <= 2000:
  print("Isento")
elif salario >= 2000.01 and salario <= 3000:
  imposto = (salario - 2000) * 0.08
elif salario >= 3000.01 and salario <= 4500:
  imposto = (salario - 3000) * 0.18 + 80
elif salario > 4500:
  imposto = (salario - 4500) * 0.28 + 350
print("Valor de R$", f"{imposto:.2f}")

# Atividade 6
n = int(input("Digite o valor:"))
i = n - 1
if n == 0:
  print(1)
else:
  while i > 0:
    n *= i
    i -= 1
  print(f"{n}! =", n)

# Atividade 7
palavra = input("João, qual palavra você descobriu?")
if len(palavra) >= 10:
  print(palavra, "é um palavrão")
else:
  print(palavra, "é uma palavrinha")

# Atividade 8
count = int(input("Digite o número de donuts:"))
if count >= 10:
  print("Número de donuts: many")
else:
  print("Número de donuts:", count)

# Atividade 9
s = input("Digite o texto:")
if len(s) < 2:
  print("")
else:
  s = s.replace(s[2:len(s)-2],"")
  print(s)

# Atividade 10
s = input("Digite o texto:")
string = s[0]
s = string + s[1:].replace(string, "*")
print(s)


# Atividade 1
idade = int(input("Sua idade:"))
if idade >= 18:
  print("Você é maior de idade.")
else:
  print("Você é menor de idade.")

# Atividade 2
animal = input("Digite um nome de um animal:")
match animal:
  case "gato":
    print("O animal é um gato")
  case "cachorro":
    print("O animal é um cachorro")
  case _:
    print("O animal não é um gato nem um cachorro")

# Atividade 3
for i in range(1, 100, 2):
  print(i)

# Atividade 4
numeros = []
total = 0
i = 0
while i != -1:
  i = int(input("Digite um número: (-1 para cancelar)"))
  if i != -1:
    numeros.append(i)
for numero in numeros:
  total += numero
media = total / len(numeros)
print("A média é de:", f"{float(media):.2f}")

# Atividade 5
n = int(input("Digite um valor inteiro:"))
i = 2
s = 1
while i < n:
  s += 1/i
  i += 1
print(float(s))

# Atividade 6
for i in range(1000, 2001):
  if i % 11 == 5:
    print(i)


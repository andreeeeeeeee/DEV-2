# Atividade 1
print("a) 'abc':", bool("abc"))
print("b) range(0):", bool(range(0)))
print("c) 123456.789:", bool(123456.789))
print("d) -5:", bool(-5))
print("e) None:", bool(None))
print("f) not(False):", bool(not(False)))
print("g) False:", bool(False))
print("h) print():", bool(print()))

# Atividade 2
precos = {'camiseta': 20, 'calca': 50, 'sapato': 100}

qtdCamiseta = int(input("Quantidade de camisetas vendidas:"))
qtdCalca = int(input("Quantidade de calças vendidas:"))
qtdSapato = int(input("Quantidade de sapatos vendidos:"))
produtos = {'camiseta': qtdCamiseta, 'calca': qtdCalca, 'sapato': qtdSapato}

totalCamiseta = precos['camiseta'] * produtos['camiseta']
totalCalca = precos['calca'] * produtos['calca']
totalSapato = precos['sapato'] * produtos['sapato']
total = totalCamiseta + totalCalca + totalSapato

print("Valor total de vendas de camisetas: R$", f"{totalCamiseta:.2f}")
print("Valor total de vendas de calcas: R$", f"{totalCalca:.2f}")
print("Valor total de vendas de sapatos: R$", f"{totalSapato:.2f}")
print("Valor total de vendas: R$", f"{total:.2f}")

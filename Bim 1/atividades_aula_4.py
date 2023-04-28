# Atividade 1
nome = input("Qual seu nome?")
salarioFixo = float(input("Qual seu salário fixo, em reais?"))
valorVendas = float(input("Quanto você vendeu nesse mês, em reais?"))
valorComissao = valorVendas * 0.15
valorTotal = valorComissao + salarioFixo
print(f"A remuneração final de {nome} é de R$ {valorTotal:.2f}.")

# Atividade 2
tempo = float(input("Tempo da viagem, em horas:"))
velocidadeMedia = float(input("Velocidade média do carro, em km/h, na viagem:"))
distanciaPercorrida = velocidadeMedia*tempo
consumo = distanciaPercorrida/12
print(f"Consumo total de {consumo:.2f} litros")


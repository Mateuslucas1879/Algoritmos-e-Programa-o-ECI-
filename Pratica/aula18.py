teste = list()
teste.append("Dara")
teste.append(25)
print(teste)


casamento = list()
casamento.append(teste[:])
print(casamento)


teste[0] = "Mateus"
teste[1] = 26
casamento.append(teste)
print(casamento)

casamento.append(teste[:])
print(casamento)
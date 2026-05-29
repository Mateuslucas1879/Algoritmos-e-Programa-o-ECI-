def depositar_procedual(saldo,valor):
    saldo += valor
    return saldo

def sacar_procedual(saldo,valor):
    if saldo >= valor:
        saldo -= valor
    else:
        print("Saldo insuficiente")
    return saldo

conta_saldo = 1000
conta_saldo = depositar_procedual(conta_saldo,200)
print(f"Saldo apos deposito: {conta_saldo}")
conta_saldo = sacar_procedual(conta_saldo,00)
print(f"Saldo apos desacado: {conta_saldo}")

print("\n" + "-"*30 + "\n")

class ContaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def depositar(self, valor):
        self.saldo += valor
        print(f"Deposito de {valor} realizado. Novo saldo: {self.saldo}")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de {valor} realizado. Novo saldo: {self.saldo}")

        else:
            print("Saldo insuficiente")

minha_conta = ContaBancaria(1000)
minha_conta.depositar(200)
minha_conta.sacar(300)
minha_conta.sacar(1500)


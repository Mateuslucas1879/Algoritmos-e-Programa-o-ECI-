class Funcionario:
    def __init__(self,  data_emissao, nome="Estagiario", salario=2000):
        self.nome = nome
        self.data_emissao = data_emissao
        self.salario = salario

    def nome_funcionario(self):
        print(f"Funcionario: {self.nome}")

    def data_funcionario(self):
        print(f"DataEmissao: {self.data_emissao}")

    def salario_funcionario(self):
        print(f"Salario: {self.salario}")

class Gerente(Funcionario):
    def __init__(self, data_emissao, nome="Gerente", salario=20000):
        # super() conecta com a classe pai de forma mais limpa
        super().__init__(data_emissao, nome, salario)

    # NÃO PRECISA REESCREVER OS MÉTODOS AQUI!
    # O Gerente já sabe usar o nome_funcionario(), salario_funcionario(), etc.


# --- Testando o código ---

dados_01 = Funcionario(2026, "Dara", 1700)
dados_02 = Funcionario(2019)

dados_01.nome_funcionario()
dados_01.data_funcionario()
dados_01.salario_funcionario()

print()
dados_02.nome_funcionario()
dados_02.data_funcionario()
dados_02.salario_funcionario()

print()
# Criando o Gerente
dados_03 = Gerente(2026, "Mateus", 35000)

# Reparou que usamos os mesmos métodos do Funcionário?
dados_03.nome_funcionario()
dados_03.data_funcionario()
dados_03.salario_funcionario()



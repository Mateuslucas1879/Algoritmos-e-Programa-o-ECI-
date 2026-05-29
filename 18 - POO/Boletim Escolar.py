class Aluno:
    def __init__(self, matricula,nome, turma, notas,historico):
        self.matricula = matricula
        self.nome = nome
        self.turma = turma
        self.notas = notas
        self.historico = historico

    def adicionar_notas(self):
        pass
    def calcular_notas(self):
        pass
    def adicionar_historico(self):
        pass


class Curso:
    def __init__(self,nome_curso,codigo_curso,vagas_disponiveis,lista_alunos):
        self.nome_curso = nome_curso
        self.codigo_curso = codigo_curso
        self.vagas_disponiveis = vagas_disponiveis
        self.lista_alunos = lista_alunos

    def matricular_aluno(self):
        pass

    def remover_aluno(self):
        pass

    def listar_matriculados(self):
        pass
class Pessoa:
  def __init__(self, nome, email, data_nascimento, endereco, cpf, telefone, ativo=True):
    self.nome = nome
    self.email = email
    self.data_nascimento = data_nascimento
    self.endereco = endereco
    self.cpf = cpf
    self.telefone = telefone
    self.ativo = ativo

  def cadastrar_pessoa(self):
    pass

class Aluno(Pessoa):
  def __init__(self, nome, email, data_nascimento, endereco, cpf, telefone, matricula, curso, turma, ativo=True,):
    super().__init__(nome, email, data_nascimento, endereco, cpf, telefone, ativo)
    self.matricula = matricula
    self.curso = curso
    self.turma = turma

  def fazer_matricula(curso):
    pass

class Professor(Pessoa):
  def __init__(self, nome, email, data_nascimento, endereco, cpf, telefone, contrato, modulos, ativo=True):
    super().__init__(nome, email, data_nascimento, endereco, cpf, telefone, ativo)
    self.contrato = contrato
    self.modulos = []

    def registrar_aula(self):
      pass

    def adicionar_modulo(self):
      pass
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
  def __init__(self, nome, email, data_nascimento, endereco, cpf, telefone, contrato, modulos = None, ativo=True):
    super().__init__(nome, email, data_nascimento, endereco, cpf, telefone, ativo)
    self.contrato = contrato
    self.modulos = modulos if modulos is not None else []

    def registrar_aula(self):
      pass

    def adicionar_modulo(self):
      pass

class Modulo:
  def __init__(self, nome, duracao, cursos=None, professores=None):
    self.nome = nome
    self.duracao = duracao
    self.cursos = cursos if cursos is not None else []
    self.professores = professores if professores is not None else []

  def registrar_notas(self):
    pass

  def registrar_faltas(self):
    pass

class Curso:
  def __init__(self, nome, duracao, modulos=None):
    self.nome = nome
    self.duracao = duracao
    self.modulos = modulos if modulos is not None else []

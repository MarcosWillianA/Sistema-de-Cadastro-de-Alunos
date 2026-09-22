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

  def visualizar_perfil(self):
    pass

  def configurar_perfil(self):
    pass

  def remover_perfil(self):
    pass


class Aluno(Pessoa):
  def __init__(self, nome, email, data_nascimento, endereco, cpf, telefone, matricula, curso, turma, ativo=True,):
    super().__init__(nome, email, data_nascimento, endereco, cpf, telefone, ativo)
    self.matricula = matricula
    self.curso = curso
    self.turma = turma

  def fazer_matricula(self, curso):
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

  def 

class Sistema: 
  def __init__(self, alunos=None, professores=None, turmas=None, cursos=None, modulos=None):
    self.alunos = alunos if alunos is not None else []
    self.professores = professores if professores is not None else []
    self.turmas = turmas if turmas is not None else []
    self.cursos = cursos if cursos is not None else []
    self.modulos = modulos if modulos is not None else []

  def exibir_menu(self):
    pass

  def cadastrar_aluno(self):
    pass 

  def cadastrar_professor(self):
    pass

  def cadastrar_turmas(self):
    pass

  def cadastrar_cursos(self):
    pass 

  def cadastrar_modulos(self):
    pass

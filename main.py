class Pessoa:
  def __init__(self, nome, email, data_nascimento, endereco, cpf, telefone, ativo):
    self.nome = nome
    self.email = email
    self.data_nascimento = data_nascimento
    self.endereco = endereco
    self.cpf = cpf
    self.telefone = telefone
    self.ativo = ativo

  def cadastrar_pessoa():
    pass

class Aluno(Pessoa):
  pass
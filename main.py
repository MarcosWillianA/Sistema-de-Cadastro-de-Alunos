# Trabalho em Grupo – LÓGICA DE PROGRAMAÇÃO II Professor: Lukas Rocha Rodrigues
# Alunos: Marcos Willian, Maria do Socorro, Tailana Guerreiro
# Grupo MMT - Gordinhas Tech

class Modulo:
    def __init__(self, nome:str, carga_horaria:int=20):        
        self._nome = nome
        self._carga_horaria = carga_horaria #em horas

    def validar_modulo(self):
        if self._carga_horaria < 20 or self._carga_horaria > 120:
            raise ValueError('Um módulo não pode ter menos de 20 horas ou mais de 120 horas.')
            return False
        else:
            return True


    def exibir_modulo(self):
        if self.validar_modulo():
            print(f'\nMódulo: {self._nome} \nCarga Horária: {self._carga_horaria} horas') 
        else:
            print('Este módulo necessita de ajustes')


class Curso:
    def __init__(self, nome:str, tipo:str, carga_horaria:int):
        self._nome = nome
        self._tipo = tipo #técnico ou qualificação profissional
        self._carga_horaria = carga_horaria 
        self._modulos = []

    def adicionar_modulo(self, modulo):
        if modulo.validar_modulo():
            self._modulos.append(modulo)
        else:
            raise ValueError('O módulo que quer criar necessita de ajustes')

    def __str__(self):
        modulos_formatados = ''
        for modulo in self._modulos:
            modulos_formatados += f'\n - - - {modulo._nome}'
        return (
            f'Nome: {self._nome}\n'
            f'Tipo: {self._tipo}\n'
            f'Carga Horária: {self._carga_horaria}\n'
            f'Módulos:{modulos_formatados}\n'            
        )

class Pessoa:
    def __init__(self, nome:str, cpf:str, email:str, telefone:str, endereco:str):
        self._nome = nome
        self._cpf = cpf
        self._email = email
        self._telefone = telefone
        self._endereco = endereco

    def validar_cpf(self):
        if len(self._cpf) == 11:
            return True
        else:
            raise ValueError('O CPF é inválido, digite novamente.')
            return False

    def __str__(self):
        return f'Nome: {self._nome} \nCPF: {self._cpf} \nEmail: {self._email} \nTelefone: {self._telefone}'  

class Aluno(Pessoa):
    def __init__(self, nome:str, cpf:str, email:str, telefone:str, endereco:str):
        super().__init__(nome, cpf, email, telefone, endereco)
        self._matriculas = []

    def validar_cpf(self):
        return super().validar_cpf()

    def modulos_aprovados(self):
        pass

    def esta_formado(self):
        pass

    def __str__(self):
        dados_pessoais = super().__str__()
        return f'{dados_pessoais} \nCursos Matriculados: {len(self._matriculas)}'


class HistoricoModulo:
    def __init__(self, aluno:Aluno, modulo:Modulo, nota:float=None, faltas:int=0):    
        self._aluno = aluno    
        self._modulo = modulo
        self._nota = nota
        self._faltas = faltas

    def esta_aprovado(self):
        if self._nota >= 7 and self._faltas <= 0.20 * self._modulo._carga_horaria:
            return True
        elif self._nota == None:
            return False
        else:
            return False

    def __str__(self):
        return (
            f'Aluno: {self._aluno._nome} \n'
            f'Módulo: {self._modulo._nome} \n'
            f'Nota: {self._nota} \n'
            f'Faltas: {self._faltas}'
        )

class Turma:
    def __init__(self, codigo:str, turno:str, ano:int, curso:Curso, ativa=True):
        self._codigo = codigo
        self._turno = turno
        self._ano = ano
        self._curso = curso
        self._matriculas = []
        self._ativa = ativa

    def matricular_aluno(self, aluno):
        novo_aluno = Matricula(Aluno.nome)

    def encerrar_turma(self):
        for matricula in self._matriculas:
            if not matricula.concluir_curso():
                self._ativa = True
            else:
                self._ativa = False

    def __str__(self):
        return f'Código: {self._codigo} \nTurno: {self._turno} \nAno: {self._ano} \nCurso: {self._curso} \nAtivo: {"Sim" if self._ativa else "Não"}'

class Matricula:
    def __init__(self, aluno:Aluno, turma:Turma, status:str='cursando'):        
        self._aluno = aluno
        self._turma = turma
        self._status = status
        self._historicos = []

    def lancar_nota(self, modulo:str, nota:float):
        if nota < 0 or nota > 10:
            raise ValueError('Nota não pode ser menor que zero ou maior que dez.')
        else:
            for historico in self._historicos:
                if modulo == historico._modulo:
                    historico._nota = nota

    def lancar_faltas(self, modulo:str, faltas:int):
        if faltas > 120:
            raise ValueError('Não é possível ter mais faltas que a carga horária.')
        else:
            for historico in self._historicos:
                if modulo == historico._modulo:
                    historico._faltas = faltas

    def trancar_curso(self):
        if self._status == 'cursando':
            self._status = 'trancado'

    
    def concluir_curso(self):
        for historico in self._historicos:
            if not historico.esta_aprovado():
                return False
            else:
                return True

    def __str__(self):
        modulos_historico = '\n'.join(f'{historico._modulo._nome}' for historico in self._historicos)
        if not modulos_historico:
            modulos_historico = "Nenhum módulo registrado"
        return (
            f'Aluno: {self._aluno._nome} \n'
            f'Turma: {self._turma._curso._nome} - {self._turma._turno} - {self._turma._ano} \n'
            f'Status: {self._status} \n'
            f'Módulos: \n ------- {modulos_historico}'            
        )


# Função pra criar Curso Técnico em Administração
def criar_curso_adm():
    teoria_geral_adm = Modulo('Teoria Geral da Administração', 120)
    planej_estrat = Modulo('Planejamento Estratégico', 120)
    legis_empresarial = Modulo('Legislação Empresarial', 120)
    fund_contab = Modulo('Fundamentos da Contabilidade', 120)
    mat_financ = Modulo('Matemática Financeira', 120)

    curso_tecnico_administracao = Curso('Técnico em Administração', 'técnico', 600)

    modulos_curso_tec = [teoria_geral_adm, planej_estrat, legis_empresarial, fund_contab, mat_financ]
    for modulo in modulos_curso_tec:
        curso_tecnico_administracao.adicionar_modulo(modulo)

    return curso_tecnico_administracao

# Função pra criar Curso Técnico em Informática
def criar_curso_info():
    intro_info = Modulo('Introdução a Informática', 120)
    arqui_comp = Modulo('Arquitetura de Computadores', 120)
    sist_op = Modulo('Sistemas Operacionais', 120)
    log_prog = Modulo('Lógica de Programação', 120)
    dev_web = Modulo('Desenvolvimento Web', 120)
    #-----
    curso_tecnico_informatica = Curso('Técnico em Informática', 'técnico', 600)
    
    modulos_curso_tec = [intro_info, arqui_comp, sist_op, log_prog, dev_web]
    for modulo in modulos_curso_tec:
        curso_tecnico_informatica.adicionar_modulo(modulo) 
    
    return curso_tecnico_informatica

def matricular_aluno():
    cancelou = False
    while True:
        nome_aluno = input('Digite aqui o nome do aluno (ou 0 para cancelar): ').capitalize()
        if nome_aluno == '0':
            cancelou = True
            break
        cpf_aluno = input('Digite aqui o CPF do aluno (ou 0 para cancelar): ').strip()
        if cpf_aluno == '0':
            cancelou = True
            break
        

# Função inicializadora ---------------------------------------------------------------------------------------------
def main():
    rodando = True
    mensagem = '''
    Seja bem vindo ao App de Gerenciamento da Escola Técnica MMT
    Escolha uma das opções do menu:

    1 - Matricular Aluno
    2 - Exibir Alunos
    3 - Exibir Cursos
    4 - Exibir Turmas
    5 - Editar Dados de Aluno
    6 - Sair
    '''

    def exibir_menu():
        print(mensagem)

    while rodando:
        opcao_usuario = input('Qual opção do menu vai escolher? ')
        
        if opcao_usuario == 1:
            cancelou = False

            while True:
                inicio_cadastro == 



main()    

# Trabalho em Grupo – LÓGICA DE PROGRAMAÇÃO II  Professor: Lukas Rocha Rodrigues
# Alunos: Marcos Willian, Maria do Socorro, Tailana Guerreiro
# Grupo MMT - Gordinhas Tech
# Sistema de cadastro de alunos – Escola Técnica MMT

class Modulo:
    def __init__(self, nome: str, carga_horaria: int = 20):
        self._nome = nome
        self._carga_horaria = carga_horaria  # em horas
        self.validar_modulo()

    def validar_modulo(self):
        if self._nome.strip() == '':
            raise ValueError('O módulo precisa ter um nome.')
        if self._carga_horaria < 20 or self._carga_horaria > 100:
            raise ValueError('Um módulo deve ter entre 20 e 100 horas.')
        return True

    def __str__(self):
        return f'{self._nome} ({self._carga_horaria}h)'


class Curso:
    def __init__(self, nome: str, tipo: str, carga_horaria: int):
        self._nome = nome
        self._tipo = tipo  # 'técnico' ou 'qualificação'
        self._carga_horaria = carga_horaria
        self._modulos = []
        self.validar_curso()

    def validar_curso(self):
        if self._tipo not in ('técnico', 'qualificação'):
            raise ValueError("O tipo do curso deve ser 'técnico' ou 'qualificação'.")
        if self._carga_horaria <= 0:
            raise ValueError('A carga horária do curso deve ser maior que zero.')
        if self._tipo == 'técnico' and (self._carga_horaria < 800 or self._carga_horaria > 1200):
            raise ValueError('Um curso técnico deve ter entre 800 e 1200 horas.')
        return True

    def carga_total(self):
        # soma a carga horária de todos os módulos já adicionados
        total = 0
        for modulo in self._modulos:
            total += modulo._carga_horaria
        return total

    def adicionar_modulo(self, modulo):
        if modulo in self._modulos:
            raise ValueError('Este módulo já está no curso.')
        if self.carga_total() + modulo._carga_horaria > self._carga_horaria:
            raise ValueError('Os módulos passariam da carga horária do curso.')
        self._modulos.append(modulo)

    def __str__(self):
        texto = (
            f'Curso: {self._nome} \n'
            f'Tipo: {self._tipo} \n'
            f'Carga Horária: {self._carga_horaria}h \n'
            f'Módulos ({len(self._modulos)}):'
        )
        for modulo in self._modulos:
            texto += f'\n   - {modulo}'
        return texto


class Pessoa:
    def __init__(self, nome: str, cpf: str, email: str, telefone: str, endereco: str):
        self._nome = nome
        self._cpf = cpf
        self._email = email
        self._telefone = telefone
        self._endereco = endereco
        # valida tudo na criação: se algo estiver errado, o objeto nem é criado
        self.validar_nome()
        self.validar_cpf()
        self.validar_email()
        self.validar_telefone()
        self.validar_endereco()

    def validar_nome(self):
        nome = self._nome.strip()
        if len(nome) < 3:
            raise ValueError('Nome inválido: use pelo menos 3 letras.')
        for letra in nome:
            if not (letra.isalpha() or letra == ' '):
                raise ValueError('Nome inválido: use apenas letras e espaços.')
        return True

    def validar_cpf(self):
        if len(self._cpf) != 11 or not self._cpf.isdigit():
            raise ValueError('CPF inválido: digite exatamente 11 números.')
        return True

    def validar_email(self):
        partes = self._email.split('@')
        if len(partes) != 2 or partes[0] == '' or '.' not in partes[1] or ' ' in self._email:
            raise ValueError('E-mail inválido. Exemplo: nome@dominio.com')
        return True

    def validar_telefone(self):
        if len(self._telefone) != 11 or not self._telefone.isdigit():
            raise ValueError('Telefone inválido: DDD + 9 + 8 dígitos (11 números).')
        return True

    def validar_endereco(self):
        if len(self._endereco.strip()) < 10:
            raise ValueError('Endereço muito curto: digite o endereço completo.')
        return True

    def __str__(self):
        c = self._cpf
        t = self._telefone
        cpf_formatado = f'{c[:3]}.{c[3:6]}.{c[6:9]}-{c[9:]}'
        telefone_formatado = f'({t[:2]}) {t[2:7]}-{t[7:]}'
        return (
            f'Nome: {self._nome} \n'
            f'CPF: {cpf_formatado} \n'
            f'E-mail: {self._email} \n'
            f'Telefone: {telefone_formatado} \n'
            f'Endereço: {self._endereco}'
        )


class Aluno(Pessoa):  # Aluno HERDA de Pessoa
    def __init__(self, nome: str, cpf: str, email: str, telefone: str, endereco: str):
        super().__init__(nome, cpf, email, telefone, endereco)
        self._matriculas = []

    def modulos_aprovados(self):
        # olha todas as matrículas do aluno e junta os módulos em que ele passou
        aprovados = []
        for matricula in self._matriculas:
            for historico in matricula._historicos:
                if historico.esta_aprovado() and historico._modulo not in aprovados:
                    aprovados.append(historico._modulo)
        return aprovados

    def modulos_pendentes(self, curso):
        # módulos do curso em que o aluno ainda NÃO foi aprovado
        aprovados = self.modulos_aprovados()
        pendentes = []
        for modulo in curso._modulos:
            if modulo not in aprovados:
                pendentes.append(modulo)
        return pendentes

    def esta_formado(self, curso):
        # formado = aprovado em todos os módulos do curso
        return len(curso._modulos) > 0 and len(self.modulos_pendentes(curso)) == 0

    def __str__(self):
        dados_pessoais = super().__str__()
        return f'{dados_pessoais} \nMatrículas: {len(self._matriculas)}'


class HistoricoModulo:
    # guarda a nota e as faltas de UM aluno em UM módulo
    def __init__(self, aluno: Aluno, modulo: Modulo, nota: float = None, faltas: int = 0):
        self._aluno = aluno
        self._modulo = modulo
        self._nota = nota
        self._faltas = faltas

    def esta_aprovado(self):
        if self._nota is None:  # nota ainda não lançada
            return False
        faltas_ok = self._faltas <= LIMITE_FALTAS * self._modulo._carga_horaria
        return self._nota >= NOTA_MINIMA and faltas_ok

    def situacao(self):
        if self._nota is None:
            return 'sem nota'
        if self.esta_aprovado():
            return 'aprovado'
        return 'reprovado'

    def __str__(self):
        nota = '-' if self._nota is None else self._nota
        return (
            f'{self._modulo._nome}: nota {nota} | '
            f'faltas {self._faltas}h | {self.situacao()}'
        )


class Turma:
    def __init__(self, codigo: str, turno: str, ano: int, curso: Curso, ativa: bool = True):
        if turno not in ('matutino', 'vespertino', 'noturno'):
            raise ValueError("O turno deve ser 'matutino', 'vespertino' ou 'noturno'.")
        self._codigo = codigo
        self._turno = turno
        self._ano = ano
        self._curso = curso
        self._matriculas = []
        self._ativa = ativa

    def matricular_aluno(self, aluno):
        if not self._ativa:
            raise ValueError('Esta turma está encerrada.')
        if len(self._curso._modulos) == 0:
            raise ValueError('Este curso ainda não tem módulos.')
        # não pode cursar o mesmo curso em duas turmas ao mesmo tempo
        for matricula in aluno._matriculas:
            if matricula._status == 'cursando' and matricula._turma._curso is self._curso:
                raise ValueError('O aluno já está cursando este curso em uma turma.')
        # só cursa os módulos em que ainda não foi aprovado (assim ele refaz os que perdeu)
        pendentes = aluno.modulos_pendentes(self._curso)
        if len(pendentes) == 0:
            raise ValueError('O aluno já foi aprovado em todos os módulos deste curso.')
        nova_matricula = Matricula(aluno, self, pendentes)
        self._matriculas.append(nova_matricula)
        aluno._matriculas.append(nova_matricula)
        return nova_matricula

    def encerrar_turma(self):
        for matricula in self._matriculas:
            if matricula._status == 'cursando':
                raise ValueError('Ainda há alunos cursando. Conclua ou tranque as matrículas antes.')
        self._ativa = False

    def __str__(self):
        return (
            f'Código: {self._codigo} \n'
            f'Curso: {self._curso._nome} \n'
            f'Turno: {self._turno} | Ano: {self._ano} \n'
            f'Alunos matriculados: {len(self._matriculas)} \n'
            f'Ativa: {"Sim" if self._ativa else "Não"}'
        )


class Matricula:
    def __init__(self, aluno: Aluno, turma: Turma, modulos: list, status: str = 'cursando'):
        self._aluno = aluno
        self._turma = turma
        self._status = status  # 'cursando', 'trancada' ou 'concluída'
        self._historicos = []
        for modulo in modulos:
            self._historicos.append(HistoricoModulo(aluno, modulo))

    def _buscar_historico(self, modulo):
        for historico in self._historicos:
            if historico._modulo is modulo:
                return historico
        raise ValueError('Este módulo não faz parte desta matrícula.')

    def _verificar_cursando(self):
        if self._status != 'cursando':
            raise ValueError(f'A matrícula está {self._status}: não pode mais ser alterada.')

    def lancar_nota(self, modulo, nota: float):
        self._verificar_cursando()
        if nota < 0 or nota > 10:
            raise ValueError('A nota deve estar entre 0 e 10.')
        self._buscar_historico(modulo)._nota = nota

    def lancar_faltas(self, modulo, faltas: int):
        self._verificar_cursando()
        if faltas < 0 or faltas > modulo._carga_horaria:
            raise ValueError(f'As faltas devem estar entre 0 e {modulo._carga_horaria}h (carga do módulo).')
        self._buscar_historico(modulo)._faltas = faltas

    def trancar_curso(self):
        self._verificar_cursando()
        self._status = 'trancada'

    def concluir_curso(self):
        self._verificar_cursando()
        for historico in self._historicos:
            if historico._nota is None:
                raise ValueError(f'Ainda falta lançar a nota de "{historico._modulo._nome}".')
        self._status = 'concluída'

    def __str__(self):
        texto = (
            f'{self._turma._curso._nome} - {self._turma._turno} {self._turma._ano} '
            f'| Situação: {self._status}'
        )
        for historico in self._historicos:
            texto += f'\n      - {historico}'
        return texto


# =============================================================================
# FUNÇÕES DE APOIO (entrada e saída de dados)
# =============================================================================

def somente_digitos(texto):
    # "123.456.789-01" vira "12345678901"
    digitos = ''
    for letra in texto:
        if letra.isdigit():
            digitos += letra
    return digitos


def ler_numero(pergunta, inteiro=False):
    texto = input(pergunta).strip().replace(',', '.')
    try:
        if inteiro:
            return int(texto)
        return float(texto)
    except ValueError:
        raise ValueError('Digite apenas números válidos.')


def escolher_item(titulo, opcoes):
    # mostra uma lista numerada e devolve a posição escolhida (ou None se voltar)
    while True:
        print(f'\n--- {titulo} ---')
        print('0 - Voltar')
        for numero in range(len(opcoes)):
            print(f'{numero + 1} - {opcoes[numero]}')
        resposta = input('Escolha uma opção: ').strip()
        if resposta == '0':
            return None
        if resposta.isdigit() and 1 <= int(resposta) <= len(opcoes):
            return int(resposta) - 1
        print('❌ Opção inválida!')


def buscar_aluno(alunos, cpf):
    for aluno in alunos:
        if aluno._cpf == cpf:
            return aluno
    return None


def ler_dados_aluno(cpf):
    # pede os dados até o aluno ser criado sem erro (ou até digitar "cancelar")
    while True:
        nome = input('Nome completo (ou "cancelar"): ').strip()
        if nome.lower() == 'cancelar':
            return None
        email = input('E-mail: ').strip().lower()
        telefone = somente_digitos(input('Telefone com DDD (ex.: 69911110000): '))
        endereco = input('Endereço completo: ').strip()
        try:
            return Aluno(nome.title(), cpf, email, telefone, endereco)
        except ValueError as erro:
            print(f'❌ {erro} Digite os dados novamente.')


def escolher_matricula_ativa(alunos):
    # lista todas as matrículas "cursando" e devolve a escolhida
    matriculas = []
    textos = []
    for aluno in alunos:
        for matricula in aluno._matriculas:
            if matricula._status == 'cursando':
                matriculas.append(matricula)
                textos.append(
                    f'{aluno._nome} - {matricula._turma._curso._nome} ({matricula._turma._turno})'
                )
    if len(matriculas) == 0:
        print('Nenhuma matrícula em andamento.')
        return None
    indice = escolher_item('Escolha a matrícula', textos)
    if indice is None:
        return None
    return matriculas[indice]


# =============================================================================
# DADOS INICIAIS DA ESCOLA
# =============================================================================

def criar_curso(nome, tipo, carga_horaria, lista_modulos):
    curso = Curso(nome, tipo, carga_horaria)
    for nome_modulo, horas in lista_modulos:
        curso.adicionar_modulo(Modulo(nome_modulo, horas))
    return curso


def criar_dados():
    modulos_adm = [
        ('Teoria Geral da Administração', 100), ('Planejamento Estratégico', 60),
        ('Legislação Empresarial', 100), ('Fundamentos da Contabilidade', 60),
        ('Matemática Financeira', 100), ('Gestão de Pessoas', 60),
        ('Marketing', 100), ('Logística e Operações', 60),
        ('Administração de Materiais', 100), ('Comunicação Empresarial', 60),
    ]
    modulos_info = [
        ('Introdução à Informática', 60), ('Arquitetura de Computadores', 100),
        ('Sistemas Operacionais', 100), ('Lógica de Programação I', 60),
        ('Lógica de Programação II', 100), ('Redes de Computadores', 60),
        ('Banco de Dados', 100), ('Desenvolvimento Web', 100),
        ('Manutenção de Computadores', 60), ('Segurança da Informação', 60),
    ]
    adm = criar_curso('Técnico em Administração', 'técnico', 800, modulos_adm)
    info = criar_curso('Técnico em Informática', 'técnico', 800, modulos_info)

    turmas = [
        Turma('ADM-2026-N', 'noturno', 2026, adm),
        Turma('INFO-2026-N', 'noturno', 2026, info),
        Turma('INFO-2026-M', 'matutino', 2026, info),
    ]
    return [adm, info], turmas


# =============================================================================
# AÇÕES DO MENU
# =============================================================================

def acao_matricular(turmas, alunos):
    textos = []
    for turma in turmas:
        aviso = '' if turma._ativa else ' [ENCERRADA]'
        textos.append(f'{turma._curso._nome} - {turma._turno} - {turma._ano}{aviso}')
    indice = escolher_item('Turmas disponíveis', textos)
    if indice is None:
        return
    turma = turmas[indice]

    cpf = somente_digitos(input('CPF do aluno (só números): '))
    if len(cpf) != 11:
        raise ValueError('CPF inválido: digite exatamente 11 números.')

    aluno = buscar_aluno(alunos, cpf)
    if aluno is None:
        print('Aluno ainda não cadastrado. Informe os dados:')
        aluno = ler_dados_aluno(cpf)
        if aluno is None:
            print('Cadastro cancelado.')
            return
        alunos.append(aluno)
    else:
        print(f'Aluno já cadastrado: {aluno._nome}')

    matricula = turma.matricular_aluno(aluno)
    print('\n✅ Matrícula realizada!')
    print(matricula)


def acao_exibir_alunos(alunos):
    if len(alunos) == 0:
        print('Nenhum aluno cadastrado ainda.')
        return
    for aluno in alunos:
        print('\n' + '=' * 50)
        print(aluno)
        for matricula in aluno._matriculas:
            print(f'   >> {matricula}')


def acao_exibir_cursos(cursos):
    for curso in cursos:
        print('\n' + '=' * 50)
        print(curso)


def acao_exibir_turmas(turmas):
    for turma in turmas:
        print('\n' + '=' * 50)
        print(turma)


def acao_lancar(alunos):
    matricula = escolher_matricula_ativa(alunos)
    if matricula is None:
        return
    textos = []
    for historico in matricula._historicos:
        textos.append(str(historico))
    indice = escolher_item('Escolha o módulo', textos)
    if indice is None:
        return
    historico = matricula._historicos[indice]
    nota = ler_numero('Nota (0 a 10): ')
    faltas = ler_numero('Faltas em horas: ', inteiro=True)
    matricula.lancar_nota(historico._modulo, nota)
    matricula.lancar_faltas(historico._modulo, faltas)
    print(f'\n✅ Lançado! {historico}')


def acao_concluir_trancar(alunos):
    matricula = escolher_matricula_ativa(alunos)
    if matricula is None:
        return
    indice = escolher_item('O que deseja fazer?', ['Concluir matrícula', 'Trancar matrícula'])
    if indice == 0:
        matricula.concluir_curso()
        print('\n✅ Matrícula concluída!')
    elif indice == 1:
        matricula.trancar_curso()
        print('\n✅ Matrícula trancada.')


def acao_formatura(alunos, cursos):
    if len(alunos) == 0:
        print('Nenhum aluno cadastrado ainda.')
        return
    nomes_alunos = []
    for aluno in alunos:
        nomes_alunos.append(aluno._nome)
    i = escolher_item('Escolha o aluno', nomes_alunos)
    if i is None:
        return
    nomes_cursos = []
    for curso in cursos:
        nomes_cursos.append(curso._nome)
    j = escolher_item('Escolha o curso', nomes_cursos)
    if j is None:
        return
    aluno = alunos[i]
    curso = cursos[j]
    if aluno.esta_formado(curso):
        print(f'\n🎓 {aluno._nome} está FORMADO em {curso._nome}!')
    else:
        print(f'\n{aluno._nome} ainda não está formado em {curso._nome}.')
        print('Módulos pendentes:')
        for modulo in aluno.modulos_pendentes(curso):
            print(f'   - {modulo}')


def acao_encerrar_turma(turmas):
    ativas = []
    textos = []
    for turma in turmas:
        if turma._ativa:
            ativas.append(turma)
            textos.append(f'{turma._curso._nome} - {turma._turno} - {turma._ano}')
    if len(ativas) == 0:
        print('Não há turmas ativas.')
        return
    indice = escolher_item('Qual turma encerrar?', textos)
    if indice is None:
        return
    ativas[indice].encerrar_turma()
    print('\n✅ Turma encerrada.')


# =============================================================================
# PROGRAMA PRINCIPAL
# =============================================================================

def main():
    cursos, turmas = criar_dados()
    alunos = []

    menu = '''
    Seja bem vindo ao App de Gerenciamento da Escola Técnica MMT
    Escolha uma das opções do menu:

    1 - Matricular Aluno
    2 - Exibir Alunos
    3 - Exibir Cursos
    4 - Exibir Turmas
    5 - Lançar Nota e Faltas
    6 - Concluir ou Trancar Matrícula
    7 - Verificar Formatura do Aluno
    8 - Encerrar Turma
    9 - Sair
    '''

    while True:
        print(menu)
        opcao = input('Qual opção do menu vai escolher? ').strip()
        try:
            if opcao == '1':
                acao_matricular(turmas, alunos)
            elif opcao == '2':
                acao_exibir_alunos(alunos)
            elif opcao == '3':
                acao_exibir_cursos(cursos)
            elif opcao == '4':
                acao_exibir_turmas(turmas)
            elif opcao == '5':
                acao_lancar(alunos)
            elif opcao == '6':
                acao_concluir_trancar(alunos)
            elif opcao == '7':
                acao_formatura(alunos, cursos)
            elif opcao == '8':
                acao_encerrar_turma(turmas)
            elif opcao == '9':
                print('Saindo do programa, até logo.')
                break
            else:
                print('❌ Opção inválida.')
        except ValueError as erro:  # captura qualquer erro de regra e continua o programa
            print(f'\n❌ {erro}')


if __name__ == '__main__':
    main()
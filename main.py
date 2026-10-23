# Trabalho em Grupo – LÓGICA DE PROGRAMAÇÃO II 
# Professor: Lukas Rocha Rodrigues
# Alunos: Marcos Willian
# Grupo MMT 
# Sistema de cadastro de alunos – Escola Técnica MMT

class Pessoa:
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf
        self.validar_cpf()

    def validar_cpf(self):
        # Exigência de nota máxima: Uso de exceção
        if len(self.cpf) != 11 or not self.cpf.isdigit():
            raise ValueError("Erro: O CPF deve conter exatamente 11 números.")

    def __str__(self):
        return f"Nome: {self.nome} | CPF: {self.cpf}"


# Exigência de nota máxima: Herança
class Aluno(Pessoa):
    def __init__(self, nome: str, cpf: str):
        super().__init__(nome, cpf)
        self.matriculas = []

    def adicionar_matricula(self, matricula):
        self.matriculas.append(matricula)

    def __str__(self):
        base = super().__str__()
        return f"{base} | Matrículas Ativas: {len(self.matriculas)}"


class Curso:
    def __init__(self, nome: str, tipo: str):
        self.nome = nome
        self.tipo = tipo

    def __str__(self):
        return f"Curso: {self.nome} ({self.tipo})"


# Exigência de nota máxima: Relacionamento
class Turma:
    def __init__(self, codigo: str, curso: Curso):
        self.codigo = codigo
        self.curso = curso  # Relacionamento com a classe Curso
        self.alunos_matriculados = []

    def matricular(self, aluno: Aluno):
        matricula = Matricula(aluno, self)
        self.alunos_matriculados.append(matricula)
        aluno.adicionar_matricula(matricula)
        return matricula

    def __str__(self):
        return f"Turma: {self.codigo} | {self.curso.nome} | Alunos: {len(self.alunos_matriculados)}"


class Matricula:
    def __init__(self, aluno: Aluno, turma: Turma):
        self.aluno = aluno  # Relacionamento com Aluno
        self.turma = turma  # Relacionamento com Turma

    def __str__(self):
        return f"Matrícula -> {self.aluno.nome} na {self.turma.codigo}"


# =============================================================================
# PROGRAMA PRINCIPAL
# =============================================================================

def main():
    # Exigência de nota máxima: Criar no mínimo 3 objetos 
    curso1 = Curso("Técnico em Administração", "Técnico")
    curso2 = Curso("Técnico em Informática", "Técnico")
    
    turma1 = Turma("ADM-2026-N", curso1)
    turma2 = Turma("INFO-2026-N", curso2)
    
    cursos = [curso1, curso2]
    turmas = [turma1, turma2]
    alunos = []

    menu = '''
    --- Menu Escola Técnica MMT ---
    1 - Matricular Aluno
    2 - Exibir Alunos
    3 - Exibir Cursos
    4 - Exibir Turmas
    0 - Sair
    -------------------------------
    Escolha uma opção: '''

    while True:
        opcao = input(menu).strip()
        
        try:
            if opcao == '1':
                print("\n--- Turmas disponíveis ---")
                for i, t in enumerate(turmas):
                    print(f"{i + 1} - {t.codigo} ({t.curso.nome})")
                
                escolha = int(input("Escolha o número da turma: ")) - 1
                
                if 0 <= escolha < len(turmas):
                    turma_escolhida = turmas[escolha]
                    nome = input("Nome do Aluno: ").title()
                    cpf = input("CPF (11 dígitos numéricos): ")
                    
                    # Cria o objeto Aluno e valida (pode disparar a exceção do CPF)
                    novo_aluno = Aluno(nome, cpf)
                    alunos.append(novo_aluno)
                    
                    turma_escolhida.matricular(novo_aluno)
                    print("\n✅ Aluno matriculado com sucesso!")
                else:
                    print("\n❌ Turma inválida.")
                    
            elif opcao == '2':
                print("\n--- Lista de Alunos ---")
                if not alunos:
                    print("Nenhum aluno cadastrado.")
                for a in alunos:
                    print("-" * 30)
                    print(a)
                    for mat in a.matriculas:
                        print(f"  -> {mat.turma.codigo}")
                        
            elif opcao == '3':
                print("\n--- Lista de Cursos ---")
                for c in cursos:
                    print("-" * 30)
                    print(c)
                    
            elif opcao == '4':
                print("\n--- Lista de Turmas ---")
                for t in turmas:
                    print("-" * 30)
                    print(t)
                    
            elif opcao == '0':
                print("\nSaindo do programa... Até logo!")
                break
            else:
                print("\n❌ Opção inválida.")
                
        except ValueError as erro:
            # Captura erros de conversão de texto pra int ou erros das classes
            if "invalid literal" in str(erro):
                print("\n❌ Erro: Digite apenas números inteiros ao selecionar a turma.")
            else:
                print(f"\n❌ {erro}")
        except Exception as erro:
            print(f"\n❌ Erro inesperado: {erro}")


if __name__ == '__main__':
    main()

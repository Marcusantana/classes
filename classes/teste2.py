
class Funcionarios:
    def __init__(self, matricula, nome , telefone, email, cpf , rg , crm , coren):
        self.matricula = matricula
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.cpf = cpf
        self.rg = rg
        self.crm = crm
        self.coren = coren

class Enfermeiro (Funcionarios):
    def __init__(self, matricula, nome , telefone, email, cpf , rg , coren):
        super().__init__(self, matricula, nome , telefone, email, cpf , rg , coren )
        self.coren = coren

class Medico (Funcionarios):
    def __init__(self, matricula, nome , telefone, email, cpf , rg , crm, especialidade , horarios):
        super().__init__(self, matricula, nome , telefone, email, cpf , rg, crm )
        self.crm = crm
        self.especialidade = especialidade
        self.horarios = horarios

    def medico (self, especialidade, horarios):
        print(f"Especialidade: {especialidade} \nHorario: {horarios}")

menu = """

================ DIGITE SEU CARGO =================

[A] Médico
[B] Enfermeiro

====================================================

"""

print(menu)

opcao = input("Digite seu cargo:")
menu = opcao

if opcao == "A":

    matricula = input("\nNDigite sua matricula:")
    nome = input("Digite seu nome:")
    telefone = input("Digite seu telefone:")
    email = input("Digite seu email:")
    cpf = input("Digite seu cpf:")
    rg = input("Digite seu rg:")
    crm = input("Digite seu CRM:")
    especialidade = input("Digite sua especialidade")
    horarios = input("Digite seus horarios")

    dados = Medico(matricula , nome , telefone , email , cpf , rg , crm , especialidade , horarios)
    
    print(f"\nMatricula: {dados.matricula}")
    print(f"Nome: {dados.nome}")
    print(f"Telefone: {dados.telefone}")
    print(f"Email: {dados.email}")
    print(f"CPF: {dados.cpf}")
    print(f"RG: {dados.rg}")
    print(f"CRM {dados.crm}")
    print(f"Especialidade {dados.especialidade}")
    print(f"Horarios: {dados.horarios}")


    
elif opcao == "B":

    matricula = input("Digite sua matricula:")
    nome = input("Digite seu nome:")
    telefone = input("Digite seu telefone:")
    email = input("Digite seu email:")
    cpf = input("Digite seu cpf:")
    rg = input("Digite seu rg:")
    coren = input("Digite seu coren:")

    dados = Enfermeiro(matricula , nome , telefone , email , cpf , rg , coren)
    
    print(f"\nMatricula: {dados.matricula}")
    print(f"Nome: {dados.nome}")
    print(f"Telefone: {dados.telefone}")
    print(f"Email: {dados.email}")
    print(f"CPF: {dados.cpf}")
    print(f"RG: {dados.rg}")
    print(f"Coren: {dados.coren}")

especialidade.medico(dados.especialidade)
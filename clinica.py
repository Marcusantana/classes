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
        especialidade ="""

==============ESPECIALIDADE================

        [1] Cardiologista 
        [2] Urologista 
        [3] Pediatra 
        [4] Pneumologista 
        [5] Ginecologista 
        [6] Oftamologista 
        [7] Radiologista 
        [8] Ortopedista

===========================================
"""

        print(especialidade)
        
        valor = int(input("Digite uma especialidade"))
        especialidade = valor
        
        if valor == 1:
            print (especialidade[0])
            horarios = ["Segunda: 08:00 - 17:00", "Quarta: 08:00 - 17:00" , "Sexta: 08:00 - 17:00"]
            print(horarios)
        
        elif valor == 2:
            print (especialidade[1])
            horarios = ["Segunda: 08:00 - 17:00", "Quarta: 08:00 - 17:00" , "Sexta: 08:00 - 17:00"]
            print(horarios)
        
        elif valor == 3:
            print (especialidade[2])
            horarios = ["Segunda: 08:00 - 17:00", "Quarta: 08:00 - 17:00" , "Sexta: 08:00 - 17:00"]
            print(horarios)

        elif valor == 4:
            print (especialidade[3])
            horarios = ["Segunda: 08:00 - 17:00", "Quarta: 08:00 - 17:00" , "Sexta: 08:00 - 17:00"]
            print(horarios)

        elif valor == 5:
            print (especialidade[4])
            horarios = ["Terça: 07:00 - 16:00", "Quinta: 07:00 - 16:00" , "Sabado: 07:00 - 16:00"]
            print(horarios)

            
        elif especialidade == 6:
            print (especialidade[5])
            horarios = ["Terça: 07:00 - 16:00", "Quinta: 07:00 - 16:00" , "Sabado: 07:00 - 16:00"]
            print(horarios)

            
        elif valor == 7:
            print (especialidade[6])
            horarios = ["Terça: 07:00 - 16:00", "Quinta: 07:00 - 16:00" , "Sabado: 07:00 - 16:00"]
            print(horarios)

            
        elif valor == 8:
            print (especialidade[7])
            horarios = ["Terça: 07:00 - 16:00", "Quinta: 07:00 - 16:00" , "Sabado: 07:00 - 16:00"]
            print(horarios)

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
    especialidade = ""
    horarios = ""

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

    dados.medico(especialidade)
    
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


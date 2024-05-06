from funcionarios import Funcionarios

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

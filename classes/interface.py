from funcionarios import Funcionarios
from enfermeiros_medicos import Enfermeiro , Medico

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
    medico1 = Medico("03940923" , "Ricardo" , "(21)982940294" , "ricardo@hotmail.com" , "080.845.231-20" , "12.432.454-8" , "78929402-9/BR" , "Cardiologista" , "\nSegunda: 08:00 - 17:00 \nQuarta: 08:00 - 17:00 \nSexta: 08:00 - 17:00")
    medico2 = Medico("08596859" , "João" , "(21)974326879" , "joao@hotmail.com" , "070.775.232-76" , "81.443.007-1" , "32325678-4/BR" , "Urologista" , "\nSegunda: 08:00 - 17:00 \nQuarta: 08:00 - 17:00 \nSexta: 08:00 - 17:00")
    medico3 = Medico("06895596" , "Vanessa" , "(21)996536780" , "vanessa@hotmail.com" , "011.212.774-10" , "66.800.890-2" , "90786543-6/BR" , "Pediatra" , "\nSegunda: 08:00 - 17:00 \nQuarta: 08:00 - 17:00 \nSexta: 08:00 - 17:00")
    medico4 = Medico("05469893" , "Bianca" , "(21)965684422" , "bianca@hotmail.com" , "121.431.777-74" , "18.004.988-9" , "12987050-4/BR" , "Pneumologista" , "\nSegunda: 08:00 - 17:00 \nQuarta: 08:00 - 17:00 \nSexta: 08:00 - 17:00")
    medico5 = Medico("09452343" , "Fabricio" , "(21)984564325" , "fabricio@hotmail.com" , "576.576.666-04" , "90.787.099-3" , "90863513-0/BR" , "Ginecologista" , "Terça: 07:00 - 16:00 \nQuinta: 07:00 - 16:00 Sabado: 07:00 - 16:00")
    medico6 = Medico("05676787" , "Carlos" , "(21)982345863" , "carlos@hotmail.com" , "042.643.756-88" , "98.675.030-2" , "90875341-8/BR" , "Oftamologista" , "\nTerça: 07:00 - 16:00 \nQuinta: 07:00 - 16:00 \nSabado: 07:00 - 16:00")
    medico7 = Medico("00239923" , "Sergio" , "(21)980890403" , "sergio@hotmail.com" , "999.843.124-54" , "32.656.788-6" , "98760213-7/BR" , "Radiologista" , "\nTerça: 07:00 - 16:00 \nQuinta: 07:00 - 16:00 \nSabado: 07:00 - 16:00")
    medico8 = Medico("01342344" , "Paola" , "(21)994665556" , "paola@hotmail.com" , "898.456.123-21" , "16.444.567-4" , "09876351-1/BR" , "Ortopedista" , "\nTerça: 07:00 - 16:00 \nQuinta: 07:00 - 16:00 \nSabado: 07:00 - 16:00")

    print("Matricula:", medico1.matricula , "\nNome:" , medico1.nome , "\nTelefone:" , medico1.telefone , "\nEmail:" , medico1.email , "\nCPF:" , medico1.cpf , "\nRG:" , medico1.rg , "\nCRM:" , medico1.crm , "\nEspecialidade:" , medico1.especialidade , "\nHorarios:" , medico1.horarios)
    print("\n\nMatricula:", medico2.matricula , "\nNome:" , medico2.nome , "\nTelefone:" , medico2.telefone , "\nEmail:" , medico2.email , "\nCPF:" , medico2.cpf , "\nRG:" , medico2.rg , "\nCRM:" , medico2.crm , "\nEspecialidade:" , medico2.especialidade , "\nHorarios:" , medico2.horarios)
    print("\n\nMatricula:", medico3.matricula , "\nNome:" , medico3.nome , "\nTelefone:" , medico3.telefone , "\nEmail:" , medico3.email , "\nCPF:" , medico3.cpf , "\nRG:" , medico3.rg , "\nCRM:" , medico3.crm , "\nEspecialidade:" , medico3.especialidade , "\nHorarios:" , medico3.horarios)
    print("\n\nMatricula:", medico4.matricula , "\nNome:" , medico4.nome , "\nTelefone:" , medico4.telefone , "\nEmail:" , medico4.email , "\nCPF:" , medico4.cpf , "\nRG:" , medico4.rg , "\nCRM:" , medico4.crm , "\nEspecialidade:" , medico4.especialidade , "\nHorarios:" , medico4.horarios)
    print("\n\nMatricula:", medico5.matricula , "\nNome:" , medico5.nome , "\nTelefone:" , medico5.telefone , "\nEmail:" , medico5.email , "\nCPF:" , medico5.cpf , "\nRG:" , medico5.rg , "\nCRM:" , medico5.crm , "\nEspecialidade:" , medico5.especialidade , "\nHorarios:" , medico5.horarios)
    print("\n\nMatricula:", medico6.matricula , "\nNome:" , medico6.nome , "\nTelefone:" , medico6.telefone , "\nEmail:" , medico6.email , "\nCPF:" , medico6.cpf , "\nRG:" , medico6.rg , "\nCRM:" , medico6.crm , "\nEspecialidade:" , medico6.especialidade , "\nHorarios:" , medico6.horarios)
    print("\n\nMatricula:", medico7.matricula , "\nNome:" , medico7.nome , "\nTelefone:" , medico7.telefone , "\nEmail:" , medico7.email , "\nCPF:" , medico7.cpf , "\nRG:" , medico7.rg , "\nCRM:" , medico7.crm , "\nEspecialidade:" , medico7.especialidade , "\nHorarios:" , medico7.horarios)
    print("\n\nMatricula:", medico8.matricula , "\nNome:" , medico8.nome , "\nTelefone:" , medico8.telefone , "\nEmail:" , medico8.email , "\nCPF:" , medico8.cpf , "\nRG:" , medico8.rg , "\nCRM:" , medico8.crm , "\nEspecialidade:" , medico8.especialidade , "\nHorarios:" , medico8.horarios)

    interface = """

    =============DESEJA PROSSEGUIR COM A CONSULTA?===============

        [1]SIM
        [2]NAO

    ==============================================================
    """
    print(interface)

    interface1 = input("Escolha uma opção:")
    interface = interface1

    if interface1 == "1":
        
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
        
        especialidade1 = input("Digite a especialidade desejada:")
        especialidade = especialidade1


        if especialidade1 == "1":
            medico1.medico(medico1.especialidade , medico1.horarios)

        if especialidade1 == "2":
            medico1.medico(medico2.especialidade , medico2.horarios)
        
        if especialidade1 == "3":
            medico1.medico(medico3.especialidade , medico3.horarios)

        if especialidade1 == "4":
                medico1.medico(medico4.especialidade , medico4.horarios)
            
        if especialidade1 == "5":
            medico1.medico(medico5.especialidade , medico5.horarios)
            
        if especialidade1 == "6":
            medico1.medico(medico6.especialidade , medico6.horarios)
            
        if especialidade1 == "7":
            medico1.medico(medico7.especialidade , medico7.horarios)
            
        if especialidade1 == "8":
            medico1.medico(medico8.especialidade , medico8.horarios)


elif opcao == "B":
    enfermeiro1 = Enfermeiro("03940923" , "Ricardo" , "(21)982940294" , "ricardo@hotmail.com" , "080.845.231-20" , "12.432.454-8" , "983710" )
    enfermeiro2 = Enfermeiro("08596859" , "João" , "(21)974326879" , "joao@hotmail.com" , "070.775.232-76" , "81.443.007-1" , "903753")
    enfermeiro3 = Enfermeiro("06895596" , "Vanessa" , "(21)996536780" , "vanessa@hotmail.com" , "011.212.774-10" , "66.800.890-2" , "659313")
    enfermeiro4 = Enfermeiro("05469893" , "Bianca" , "(21)965684422" , "bianca@hotmail.com" , "121.431.777-74" , "18.004.988-9" , "156094")

    print("Matricula:", enfermeiro1.matricula , "\nNome:" , enfermeiro1.nome , "\nTelefone:" , enfermeiro1.telefone , "\nEmail:" , enfermeiro1.email , "\nCPF:" , enfermeiro1.cpf , "\nRG:" , enfermeiro1.rg , "\nCOREN:" , enfermeiro1.coren)
    print("\n\nMatricula:", enfermeiro2.matricula , "\nNome:" , enfermeiro2.nome , "\nTelefone:" , enfermeiro2.telefone , "\nEmail:" , enfermeiro2.email , "\nCPF:" , enfermeiro2.cpf , "\nRG:" , enfermeiro2.rg , "\nCOREN:" , enfermeiro2.coren)
    print("\n\nMatricula:", enfermeiro3.matricula , "\nNome:" , enfermeiro3.nome , "\nTelefone:" , enfermeiro3.telefone , "\nEmail:" , enfermeiro3.email , "\nCPF:" , enfermeiro3.cpf , "\nRG:" , enfermeiro3.rg , "\nCOREN:" , enfermeiro3.coren)
    print("\n\nMatricula:", enfermeiro4.matricula , "\nNome:" , enfermeiro4.nome , "\nTelefone:" , enfermeiro4.telefone , "\nEmail:" , enfermeiro4.email , "\nCPF:" , enfermeiro4.cpf , "\nRG:" , enfermeiro4.rg , "\nCOREN:" , enfermeiro4.coren)
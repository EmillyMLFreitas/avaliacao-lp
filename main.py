def imprimir_pacinete(id_paciente, array_pacientes):
    if len(array_pacientes) < (id_paciente - 1):
        print("Paciente não encontrado")
    else:
        paciente = array_pacientes[id_paciente - 1]    
        print(paciente)


pacientes = []
executar_programa = True

while executar_programa:

    print("1. Inserir dados do Paciente")
    print("2. Imprimir dados do Paciente")
    print("3. Verificar situação do Paciente")
    print("4. Sair do programa")
    
    opcao = int(input("Digite a opção: "))
    if opcao == 1:
        
        nome = str(input("Nome: "))
        data_nasc = str(input("Data de Nasc: "))
        peso = float(input("Peso: "))
        massa_corporal = int(input("Massa Corporal (%): "))
        
        paciente = [nome, data_nasc, peso, massa_corporal]
        pacientes.append(paciente)
        
        
        
       
        

          
    
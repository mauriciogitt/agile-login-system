print("Bem-vindo ao sistema")

# Sistema de login

print("Sistema iniciado")

usuario_correto = "admin"
senha_correta = "123"

# Lista de tarefas
tarefas = []

usuario = input("Usuário: ")
senha = input("Senha: ")

if usuario == usuario_correto and senha == senha_correta:

    while True:

        print("\n1 - Adicionar tarefa")
        print("2 - Averiguar tarefas")
        print("3 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":

            tarefa = input("Digite a tarefa: ")
            tarefas.append(tarefa)

        elif opcao == "2":

            print(tarefas)

        elif opcao == "3":

            break

else:
    print("Login inválido")

    print("Sistema encerrado")
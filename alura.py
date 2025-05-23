while True:
    nome_usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if len(nome_usuario) >= 5 and len(senha) >= 8:
        print("Cadastro realizado com sucesso!")
        break
    else:
        print("Erro no cadastro:")
        if len(nome_usuario) < 5:
            print("- O nome de usuário deve ter pelo menos 5 caracteres.")
        if len(senha) < 8:
            print("- A senha deve ter pelo menos 8 caracteres.")
        print("Tente novamente.\n")

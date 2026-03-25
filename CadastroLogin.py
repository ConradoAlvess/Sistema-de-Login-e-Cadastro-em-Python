import json

ARQUIVO = "usuarios.json"


def carregar_usuarios():
    try:
        with open(ARQUIVO, "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []


def salvar_usuarios(usuarios):
    with open(ARQUIVO, "w") as arquivo:
        json.dump(usuarios, arquivo, indent=4)


def cadastrar_usuario(usuarios):
    print("\n=== CADASTRO ===")
    nome = input("Nome: ")
    senha = input("Senha: ")

    for u in usuarios:
        if u["nome"] == nome:
            print("Usuário já existe!\n")
            return

    usuario = {
        "nome": nome,
        "senha": senha
    }

    usuarios.append(usuario)
    salvar_usuarios(usuarios)
    print("Usuário cadastrado com sucesso!\n")


def fazer_login(usuarios):
    print("\n=== LOGIN ===")
    nome = input("Nome: ")
    senha = input("Senha: ")

    for u in usuarios:
        if u["nome"] == nome and u["senha"] == senha:
            print("Login realizado com sucesso!\n")
            return True

    print("Usuário ou senha incorretos.\n")
    return False


def menu():
    usuarios = carregar_usuarios()

    while True:
        print("=== SISTEMA ===")
        print("1 - Cadastrar")
        print("2 - Login")
        print("3 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_usuario(usuarios)

        elif opcao == "2":
            if fazer_login(usuarios):
                print("Bem-vindo ao sistema!")

        elif opcao == "3":
            print("Encerrando...")
            break

        else:
            print("Opção inválida.\n")


menu()
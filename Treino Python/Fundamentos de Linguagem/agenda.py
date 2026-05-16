def exibir_menu():
    print("\n--- Agenda Simples ---")
    print("1. Cadastrar Contato")
    print("2. Listar Contatos")
    print("3. Buscar Contato")
    print("4. Deletar Contato")
    print("5. Sair")
    return input("Escolha uma opção: ")

def CadastrarContatos(agenda):
    nome = input("Nome: ")
    telefone = input("Telefone: (+55) ")
    agenda[nome] = telefone
    print(f"Contato {nome} adicionado!")

def ListarContatos(agenda):
    if not agenda:
        print("Agenda vazia.")
    else:
        print("--- Lista de Contatos ---")
        for nome in agenda.keys():
            print(f"Nome: {nome} | Telefone: {agenda[nome]}")

def BuscarContatos(nome, agenda):
    telefone = agenda.get(nome)
    if telefone:
        print(f"Encontrado - Nome: {nome} | Telefone: {telefone}")
    else:
        print(f"Telefone não encontrado.")

def DeletarContatos(nome, agenda):
    telefone = agenda.get(nome)
    if telefone:
        del agenda[nome]
    else:
        print("Esse número não existe ou já foi deletado.")

def main():
    agenda = {}

    while True:
        try:
            opcao = exibir_menu()
            

            match(opcao):
                case "1":
                    CadastrarContatos(agenda)
                case "2":
                    ListarContatos(agenda)
                case "3":
                    nome = input("Qual contato buscar?: ")
                    BuscarContatos(nome, agenda)
                case "4":
                    nome = input("Qual contato deletar?: ")
                    DeletarContatos(nome, agenda)
                case "5":
                    break
        except ValueError:
            print("Opção Inválida")

main()
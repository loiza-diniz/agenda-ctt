def adicionar_contato(contatos):
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    favorito = input("O contato é favorito? (s/n): ").strip().lower() == 's'
    
    contatos[nome] = {'telefone': telefone, 'favorito': favorito}
    print(f"Contato {nome} adicionado com sucesso!")

def listar_contatos(contatos):
    if not contatos:
        print("Não há contatos cadastrados.")
    else:
        for nome in sorted(contatos):
            telefone = contatos[nome]['telefone']
            favorito = "Favorito" if contatos[nome]['favorito'] else "Não Favorito"
            print(f"{nome} - {telefone} - {favorito}")


def buscar_contato(contatos):
    nome = input("Digite o nome do contato a ser buscado: ")
    if nome in contatos:
        telefone = contatos[nome]['telefone']
        favorito = "Favorito" if contatos[nome]['favorito'] else "Não Favorito"
        print(f"{nome} - {telefone} - {favorito}")
    else:
        print("Contato não encontrado.")

def atualizar_contato(contatos):
    nome = input("informe o nome do contato a ser atualizado: ")
    if nome in contatos:
        telefone = input(f"digite uo novo telefone para {nome}: ")
        favorito = input("o contato será favoritado (s/n): ").strip().lower() == 's'
        contatos[nome] = {'telefone': telefone, 'favorito': favorito}
        print(f"contato {nome} atualizado com sucesso!")
    else:
        print("contato não encontrado")

def remover_contato(contatos):
    nome = input("Digite o nome do contato a ser removido: ") 
    if nome in contatos:
        del contatos[nome]
        print(f"contato {nome} removido com sucesso")
    else:
        print("contato não encontrado")

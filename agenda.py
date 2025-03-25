def adicionar_contato(contatos):
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    favorito = input("O contato é favorito? (s/n): ").strip().lower() == 's'
    
    contatos[nome] = {'telefone': telefone, 'favorito': favorito}
    print(f"Contato {nome} adicionado com sucesso!")

def listar_contatos(contatos):
    if not contatos:
        print("Não há contatos registrados")
    else:
        for nome in sorted(contatos):
            telefone = contatos[nome]['telefone']
            favorito = "Favorito" if contatos[nome]['favorito'] else "Não Favorito"
            print(f"{nome} - {telefone} - {favorito}")

def buscar_contato(contatos):
    nome = input("informe o nome do contato: ")
    if nome in contatos:
        telefone = contatos[nome]['telefone']
        favorito = "favorito" if contatos [nome]['favorito'] else "não favorito"
        print(f"{nome} - {telefone} - {favorito}")
    else:
        print("contato não encontrado")


import json
import os

AGENDA_FILE = 'agenda.json'

def carregar_contatos():
    if os.path.exists(AGENDA_FILE):
        try:
            with open(AGENDA_FILE, 'r') as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Erro ao carregar os dados da agenda: {e}")
            return {}
    return {}

def salvar_contatos(contatos):
    try:
        with open(AGENDA_FILE, 'w') as file:
            json.dump(contatos, file, indent=4)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Erro ao salvar os dados da agenda: {e}")

def adicionar_contato(contatos):
    try:
        nome = input("informe o nome do contato: ").strip()
        telefone = input("informe o telefone do contato: ").strip()
        
        if not nome or not telefone:
            raise ValueError("Nome e telefone não podem ser vazios.")
        
        favorito = input("O contato é favorito? (s/n): ").strip().lower() == 's'
        
        contatos[nome] = {'telefone': telefone, 'favorito': favorito}
        print(f"Contato {nome} adicionado com sucesso!")
    except ValueError as ve:
        print(f"Erro de validação: {ve}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao adicionar o contato: {e}")

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

def favoritar_desfavoritar(contatos):
    nome = input("Digite o nome do contato a ser favoritado/desfavoritado: ")
    if nome in contatos:
        contatos[nome]['favorito'] = not contatos[nome]['favorito']
        status = "favoritado" if contatos[nome]['favorito'] else "desfavoritado"
        print(f"Contato {nome} {status} com sucesso!")
    else:
        print("contato não encontrado")

def listar_favoritos(contatos):
    favoritos = {nome: contatos[nome] for nome in contatos if contatos[nome]['favorito']}
    if not favoritos:
        print("Não há contatos favoritos.")
    else:
        for nome in sorted(favoritos):
            telefone = favoritos['nome']['telefone']
            print(f"{nome} - {telefone} - Favorito")


def menu():
    contatos = carregar_contatos()
    while True:
        print("\nAGENDA DE CONTATOS")
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Buscar contato")
        print("4. Atualizar contato")
        print("5. Remover contato")
        print("6. Favoritar/Desfavoritar contato")
        print("7. Listar contatos favoritos")
        print("8. Sair")

        opcao = input("escolha uma opção: ").strip()

        if opcao == '1':
            adicionar_contato(contatos)
            salvar_contatos(contatos)
        elif opcao == '2':
            listar_contatos(contatos)
        elif opcao == '3':
            buscar_contato(contatos)
        elif opcao == '4':
            atualizar_contato(contatos)
            salvar_contatos(contatos)
        elif opcao == '5':
            remover_contato(contatos)
            salvar_contatos(contatos)
        elif opcao == '6':
            favoritar_desfavoritar(contatos)
            salvar_contatos(contatos)
        elif opcao == '7':
            listar_favoritos(contatos)
        elif opcao == '8':
            print("saindo...")
            break
        else:
            print("Opção inválida! Tente novamente")

if __name__ == "__main__":
    menu()
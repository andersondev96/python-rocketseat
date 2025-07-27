# App Agenda

def criar_contato(contatos, nome_contato, telefone_contato, email_contato):
  contato = {"nome": nome_contato, "telefone": telefone_contato, "email": email_contato, "favorito": False}
  contatos.append(contato)
  print(f"\nContato {nome_contato} foi adicionado a agenda")
  return

def ver_contatos(contatos):
  print("\nLista de contatos:")
  print("==========================================")
  for indice, contato in enumerate(contatos, start=1):
    favorito = "❤️ " if contato["favorito"] else ""
    print(f"Contato {indice}: ")
    print(f"{favorito}Nome do contato: {contato["nome"]}")
    print(f"Telefone: {contato["telefone"]}")
    print(f"E-mail: {contato["email"]}")
    print("==========================================")
  return

def atualizar_contato(contatos, indice, nome_contato, telefone_contato, email_contato):
  indice_contato_ajustado = int(indice) - 1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
    contatos[indice_contato_ajustado]["nome"] = nome_contato
    contatos[indice_contato_ajustado]["telefone"] = telefone_contato
    contatos[indice_contato_ajustado]["email"] = email_contato
    print(f"Contato de indice {indice} atualizado.")
  else:
    print("Indice do contato inválido")
  return

def excluir_contato(contatos, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
    contatos.pop(indice_contato_ajustado)
    print("O contato foi removido da sua agenda")
  else:
    print("Indice do contato inválido")
  return

def marcar_ou_desmarcar_contato_favorito(contatos, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
    status_contato = contatos[indice_contato_ajustado]["favorito"] 
    contatos[indice_contato_ajustado]["favorito"] = not status_contato
    contato_favorito = contatos[indice_contato_ajustado]["nome"]
    if not status_contato:
      print(f"O contato {contato_favorito} foi adicionado na sua lista de contatos favoritos.")
    else:
      print(f"O contato {contato_favorito} foi removida da sua lista de contatos favoritos.")  
  else:
    print("Indice do contato inválido")
  return

def ver_contatos_favoritos(contatos):
  print("\nLista de contatos favoritos")
  print("==========================================") 
  for indice, contato in enumerate(contatos, start=1):
    if contato["favorito"]:
      print(f"{indice}. {contato["nome"]}")
  return 

contatos = []
while True:
  print("\n==========MENU==========")
  print("\n[1] Adicionar novo contato")
  print("[2] Ver contatos")
  print("[3] Editar contato")
  print("[4] Excluir contato")
  print("[5] Marcar contato como favorito")
  print("[6] Ver contatos favoritos")
  print("[7] Sair")

  escolha = input('\nDigite a opção desejada: ')

  if escolha == "1":
    nome_contato = input("Digite o nome do contato: ")
    telefone_contato = input("Digite o telefone do contato: ")
    email_contato = input("Digite o e-mail do contato: ")
    criar_contato(contatos, nome_contato, telefone_contato, email_contato)

  if escolha == "2":
    ver_contatos(contatos)

  if escolha == "3":
    ver_contatos(contatos)
    indice_contato = input("\nInforme o número do contato que deseja atualizar: ")
    novo_nome_contato = input("Digite o novo nome do contato: ")
    novo_telefone_contato = input("Digite o novo telefone do contato: ")
    novo_email_contato = input("Digite o novo e-mail do contato: ")
    atualizar_contato(contatos, indice_contato, novo_nome_contato, novo_telefone_contato, novo_email_contato)

  if escolha == "4":
    ver_contatos(contatos)
    indice_contato = input("\nInforme o número do contato que será removido: ")
    excluir_contato(contatos, indice_contato)

  if escolha == "5":
    ver_contatos(contatos)
    indice_contato = input("\nInforme o contato que deseja adicionar aos favoritos: ")
    marcar_ou_desmarcar_contato_favorito(contatos, indice_contato)
  
  if escolha == "6":
    ver_contatos_favoritos(contatos)

  if escolha == "7":
    break


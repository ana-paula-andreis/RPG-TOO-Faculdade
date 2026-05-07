from personagem import Personagem
from item import Item, TipoItem


p1 = None


while True:

    print("\n===== RPG MENU =====")
    print("1 - Criar personagem")
    print("2 - Adicionar item")
    print("3 - Equipar item")
    print("4 - Ganhar XP")
    print("5 - Mostrar personagem")
    print("0 - Sair")

    op = input("Escolha: ")

    # ------------------------
    # CRIAR PERSONAGEM
    # ------------------------
    if op == "1":

        nome = input("Nome do personagem: ")
        p1 = Personagem(nome)

        ataque = int(input("Ataque base: "))
        p1.ataqueBase = ataque

        print("Personagem criado!")

    # ------------------------
    # ADICIONAR ITEM
    # ------------------------
    elif op == "2":

        if not p1:
            print("Crie um personagem primeiro!")
            continue

        nome = input("Nome do item: ")
        desc = input("Descrição: ")

        print("Tipo: 1-Arma | 2-Vestimenta | 3-Utilitário")
        tipo_op = input("Escolha tipo: ")

        if tipo_op == "1":
            tipo = TipoItem.ARMA
            efeito = int(input("Dano: "))

        elif tipo_op == "2":
            tipo = TipoItem.VESTIMENTA
            efeito = int(input("Bônus vida (%): "))

        elif tipo_op == "3":
            tipo = TipoItem.UTILITARIO
            efeito = int(input("Bônus vida (%): "))

        else:
            print("Tipo inválido")
            continue

        item = Item(nome, desc, tipo, efeito)
        p1.adicionar_item_inventario(item)

        print("Item adicionado!")

    # ------------------------
    # EQUIPAR ITEM
    # ------------------------
    elif op == "3":

        if not p1:
            print("Crie um personagem primeiro!")
            continue

        if len(p1.inventario) == 0:
            print("Sem itens no inventário!")
            continue

        print("\nInventário:")
        for i, item in enumerate(p1.inventario):
            print(f"{i} - {item}")

        idx = int(input("Escolha o item: "))

        if idx >= 0 and idx < len(p1.inventario):
            p1.equipar_item(p1.inventario[idx])
            print("Item equipado!")
        else:
            print("Índice inválido")

    # ------------------------
    # GANHAR XP
    # ------------------------
    elif op == "4":

        if not p1:
            print("Crie um personagem primeiro!")
            continue

        xp = int(input("Quanto XP ganhou? "))
        p1.concluir_missao(xp)

        print("XP atualizado!")

    # ------------------------
    # MOSTRAR STATUS
    # ------------------------
    elif op == "5":

        if not p1:
            print("Crie um personagem primeiro!")
            continue

        p1.mostrar()

    # ------------------------
    # SAIR
    # ------------------------
    elif op == "0":

        print("Saindo...")
        break

    else:

        print("Opção inválida")
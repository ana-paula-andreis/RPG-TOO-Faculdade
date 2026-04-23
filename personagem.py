class Personagem:
    def __init__(self, nome):
        self.__nome = nome
        self.__nivel = 1
        self.__xp = 0
        self.__missoes = []

    def add_missao(self, missao):
        if missao not in self.__missoes:
            self.__missoes.append(missao)
            missao.iniciar_missao()
            print(f"Missão '{missao.nome}' adicionada ao herói {self.__nome}.")
        else:
            print("Missão já existe no diário.")

    def concluir_missao(self, missao, valor):
        if missao in self.__missoes:
            sucesso = missao.concluir_missao(valor)
            if sucesso:
                self.__xp += missao.recompensa
                print(f"Ganhou {missao.recompensa} de XP!")
            else:
                print(f"Progresso insuficiente para {missao.nome}.")
        else:
            print("O personagem não possui essa missão.")

    def exibir_dados(self):
        return (f"\n--- Status de {self.__nome} ---\n"
                f"Nível: {self.__nivel} | XP: {self.__xp}\n"
                f"Missões no diário: {len(self.__missoes)}")
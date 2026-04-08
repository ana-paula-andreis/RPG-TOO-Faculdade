class Personagem:
    def __init__(self, nome):
        self.__nome = nome
        self.__nivel = 1
        self.__vida = 100
        self.__xp = 0

    def exibir_dados(self):
        print(f"mome: {self.__nome}")
        print(f"nivel: {self.__nivel}")
        print(f"vida: {self.__vida}")
        print(f"xp: {self.__xp}")
from Missao import Missao
from Status import *

class Personagem:
    def __init__(self, nome):
        self.__nome = None
        self.__nivel = 1
        self.__vida = 100
        self.__xp = 0
        self.__missoes: list[Missao] = []

        self.nome = nome


    @property
    def missoes(self):
        return self.__missoes

    def add_missao(self, missao):
        if missao not in self.missoes:
            missao.iniciar_missao()
            self.__missoes.append(missao)
        else:
            raise Exception(f"Missão já adicionada ao personagem {self.nome}")

    def concluir_missao(self, missao: Missao, valor):
        for m in self.__missoes:
            if m == missao:
                resultado = m.concluir_missao(valor)
                if m.status == Status.CONCLUIDA:
                    self.__xp += m.recompensa

                    if self.__xp >= 20:
                        ganho_vida = self.__xp // 20
                        self.__nivel += ganho_vida
                        self.__xp = self.__xp % 20

                return resultado

        raise Exception("Missão não encontrada")
    
    def listar_missoes(self):
        if len(self.missoes) > 0:
            aux = f"Missões de {self.nome}"
            for m in self.missoes:
                aux += "-" + str(m) + "\n"
            return aux
        else:
            return (f"Não há missões cadastradas para o personsagem {self.nome}")
        
    @property
    def nome(self):
        return self.__nome

    @property
    def nivel(self):
        return self.__nivel

    @property
    def vida(self):
        return self.__vida

    @property
    def xp(self):
        return self.__xp

    @nome.setter
    def nome(self, valor):
        if valor and valor.strip():
            self.__nome = valor.strip().title()
        else:
            raise ValueError("Nome inválido")

    def __eq__(self, other):
        return isinstance(other, Personagem) and self.nome == other.nome

    def __str__(self):
        return f"personagem: {self.nome} | nivel: {self.nivel}"

    def exibir_dados(self):
        msg = (f"nome: {self.nome}\n")
        msg += (f"nivel: {self.nivel}\n")
        msg += (f"vida: {self.vida}\n")
        msg += (f"XP: {self.xp}\n")
        msg += self.listar_missoes()
        return msg
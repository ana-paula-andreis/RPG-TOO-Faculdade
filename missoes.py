from status import Status

class Missao:
    def __init__(self, nome, descricao, recompensa):
        self.__nome = nome
        self.__descricao = descricao
        self.__recompensa = recompensa
        self.__status = Status.PENDENTE

    @property
    def nome(self): return self.__nome
    @property
    def recompensa(self): return self.__recompensa
    @property
    def status(self): return self.__status
    @status.setter
    def status(self, novo): self.__status = novo

    def iniciar_missao(self):
        if self.__status == Status.PENDENTE:
            self.__status = Status.EM_ANDAMENTO
            print(f"Missão '{self.__nome}' iniciada!")

    def finalizar(self):
        self.__status = Status.CONCLUIDA
        print(f"Missão '{self.__nome}' concluída!")
        return True

class MissaoCombate(Missao):
    def __init__(self, nome, descricao, recompensa, inimigo, qtd):
        super().__init__(nome, descricao, recompensa)
        self.__qtd_alvo = qtd

    def concluir_missao(self, valor):
        if valor >= self.__qtd_alvo:
            return self.finalizar()
        return False

class MissaoColeta(Missao):
    def __init__(self, nome, descricao, recompensa, item, qtd):
        super().__init__(nome, descricao, recompensa)
        self.__qtd_alvo = qtd

    def concluir_missao(self, valor):
        if valor >= self.__qtd_alvo:
            return self.finalizar()
        return False

class MissaoExploracao(Missao):
    def __init__(self, nome, descricao, recompensa, regiao, distancia):
        super().__init__(nome, descricao, recompensa)
        self.__distancia_alvo = float(distancia)

    def concluir_missao(self, valor):
        if valor >= self.__distancia_alvo:
            return self.finalizar()
        return False
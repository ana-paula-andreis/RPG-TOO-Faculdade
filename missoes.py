from status import Status

class Missao:
    def __init__(self, nome, descricao, recompensa):
        self.__nome = nome
        self.__descricao = descricao
        self.__recompensa = recompensa
        self.__status = Status.PENDENTE

    @property
    def nome(self):
        return self.__nome

    @property
    def descricao(self):
        return self.__descricao

    @property
    def recompensa(self):
        return self.__recompensa

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, novo_status):
        if isinstance(novo_status, Status):
            self.__status = novo_status
        else:
            raise ValueError("Status inválido")

    def iniciar_missao(self):
        if self.status == Status.PENDENTE:
            self.status = Status.EM_ANDAMENTO
            print(f"A missao '{self.nome}' comecou objetivo missão: {self.descricao}")
        elif self.status == Status.EM_ANDAMENTO:
            print("A missao já está em andamento.")
        else:
            print("a missao nao pode ser iniciada.")

    def concluir_missao(self):
        if self.status == Status.EM_ANDAMENTO:
            self.status = Status.CONCLUIDA
            print(f"missão concluida com sucesso o prêmio de {self.recompensa} xp")
        else:
            print(f"Erro: nao e possivel concluir a missão {self.status.value}")

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Descrição: {self.descricao}")
        print(f"Recompensa: {self.recompensa}")
        print(f"Status: {self.status.value}")


class MissaoCombate(Missao):
    def __init__(self, nome, descricao, recompensa, inimigo, inimigos_a_derrotar):
        super().__init__(nome, descricao, recompensa)
        self.__inimigo = inimigo
        self.__inimigos_a_derrotar = inimigos_a_derrotar

    @property
    def inimigo(self):
        return self.__inimigo

    @property
    def inimigos_a_derrotar(self):
        return self.__inimigos_a_derrotar

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Inimigo: {self.inimigo}")
        print(f"Quantidade a derrotar: {self.inimigos_a_derrotar}")

class MissaoColeta(Missao):
    def __init__(self, nome, descricao, recompensa, item_necessario, quantidade_item):
        super().__init__(nome, descricao, recompensa)
        self.__item_necessario = item_necessario
        self.__quantidade_item = quantidade_item

    @property
    def item_necessario(self):
        return self.__item_necessario

    @property
    def quantidade_item(self):
        return self.__quantidade_item

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Item necessário: {self.item_necessario}")
        print(f"Quantidade: {self.quantidade_item}")

class MissaoExploracao(Missao):
    def __init__(self, nome, descricao, recompensa, regiao_destino, distancia_em_km):
        super().__init__(nome, descricao, recompensa)
        self.__regiao_destino = regiao_destino
        self.__distancia_em_km = float(distancia_em_km)

    @property
    def regiao_destino(self):
        return self.__regiao_destino

    @property
    def distancia_em_km(self):
        return self.__distancia_em_km

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Região: {self.regiao_destino}")
        print(f"Distância: {self.distancia_em_km} km")
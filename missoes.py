from Status import Status
from abc import ABC, abstractmethod

class Missao(ABC):
    def __init__(self, nome, descricao:str, recompensa, status:Status=Status.PENDENTE):
        self.__nome = None
        self.__descricao = None
        self.__recompensa = None
        self.status = status

        self.nome = nome
        self.descricao = descricao
        self.recompensa = recompensa

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if valor and valor.strip():
            self.__descricao = valor.strip() if valor else ""
        else:
            raise ValueError("nome invalido")

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, valor):
        self.__descricao = valor.strip()

    @property
    def recompensa(self):
        return self.__recompensa

    @recompensa.setter
    def recompensa(self, valor):
        if 1 <= valor <= 50:
            self.__recompensa = valor
        else:
            raise ValueError("entre 1 e 50")

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, novo_status:Status):
        
        if isinstance(novo_status, Status):
            self.__status = novo_status
        else:
            raise ValueError("Status não existe")

    def __eq__(self, other):
        return isinstance(other, Missao) and self.nome == other.nome

    def __str__(self):
        return f"missao [{self.__class__.__name__}]: {self.nome} | status: {self.status}"

    def exibir_dados(self):
        msg = f"[{self.__class__.__name__}]"
        msg += (f"\nnome: {self.nome}\n")
        msg += (f"descricao: {self.descricao}\n")
        msg += (f"recompensa: {self.recompensa}\n")
        msg += (f"status: {self.status.value}")
        return msg
    
    def iniciar_missao(self):
        if(self.status == Status.PENDENTE):
            self.status = Status.EM_ANDAMENTO
            return f"A missão {self.nome} começou! Objetivo central da missão: {self.descricao})."
        else:
            return f"A missão {self.nome} já foi iniciada!!!"
        
    @abstractmethod
    def concluir_missao(self, valor):
        pass
        '''
        if(self.status == Status.EM_ANDAMENTO):
            self.status = Status.CONCLUIDA
            return f"Missão concluída como sucesso. A contabilidade do prêmio de {self.recompensa} XP agora está pronta para retirada financeira."
        else:
            return f"A missão {self.nome} não está em andamento."
        '''
        
    
class MissaoColeta(Missao):

    def __init__(self, nome, descricao, recompensa, item_necessario, quantidade_item):
        super().__init__(nome, descricao, recompensa)
        self.item_necessario = item_necessario
        self.quantidade_item = quantidade_item
        
    @property
    def item_necessario(self):
        return self.__item_necessario
    
    @item_necessario.setter
    def item_necessario(self, item:str):
        if item:
            self.__item_necessario = item.strip().lower()
        else:
            raise ValueError("Item inválido")
        
    @property
    def quantidade_item(self):
        return self.__quantidade_item
    
    @quantidade_item.setter
    def quantidade_item(self, qnt:int):
        if isinstance(qnt, int):
            if qnt > 0:
                self.__quantidade_item = qnt
            else:
                raise Exception(f"Quantidade do item deve ser maior que Zero")
        else:
            raise Exception(f"Quantidade do item deve ser um valor numérico")



    def exibir_dados(self):
        msg = super().exibir_dados()
        msg += f"\nItem necessário: {self.item_necessario}"
        msg += f"\nQuantidade de Item a coletar: {self.quantidade_item}"
        return msg
    
    def concluir_missao(self, valor):
        if isinstance(valor, int):
            if valor >= self.quantidade_item:
                if(self.status == Status.EM_ANDAMENTO):
                    self.status = Status.CONCLUIDA
                    return f"Missão concluída como sucesso. A contabilidade do prêmio de {self.recompensa} XP agora está pronta para retirada financeira."
                else:
                    return f"A missão {self.nome} não está em andamento."
            else:
                self.status = Status.FRACASSADA
                return f"Missão fracassada"

class MissaoCombate(Missao):

    def __init__(self, nome, descricao, recompensa, tipo_inimigo:str, qnt_inimigos:int):
        super().__init__(nome, descricao, recompensa)
        self.tipo_inimigo = tipo_inimigo
        self.inimigos_a_derrotar = qnt_inimigos
        
    @property
    def tipo_inimigo(self):
        return self.__tipo_inimigo
    
    @tipo_inimigo.setter
    def tipo_inimigo(self, tipo:str):
        self.__tipo_inimigo = tipo.strip().lower()
        
    @property
    def inimigos_a_derrotar(self):
        return self.__inimigos_a_derrotar
    
    @inimigos_a_derrotar.setter
    def inimigos_a_derrotar(self, qnt:int):
        if isinstance(qnt, int):
            if qnt > 0:
                self.__inimigos_a_derrotar = qnt
            else:
                raise Exception(f"Quantidade de inimigos deve ser maior que Zero")
        else:
            raise Exception(f"Quantidade de inimigos deve ser um valor numérico")


    def exibir_dados(self):
            str = super().exibir_dados()
            str += f"\nInimigo a Derrotar: {self.tipo_inimigo}"
            str += f"\nQuantidade de Inimigos a derrotar: {self.inimigos_a_derrotar}"
            return str
    
    def concluir_missao(self, valor):
        if isinstance(valor, int):
            if valor >= self.inimigos_a_derrotar:
                if(self.status == Status.EM_ANDAMENTO):
                    self.status = Status.CONCLUIDA
                    return f"Missão concluída como sucesso. A contabilidade do prêmio de {self.recompensa} XP agora está pronta para retirada financeira."
                else:
                    return f"A missão {self.nome} não está em andamento."
            else:
                self.status = Status.FRACASSADA
                return f"Missão fracassada"
    
class MissaoExploracao(Missao):

    def __init__(self, nome, descricao, recompensa, regiao_destino:str, distancia_em_km:float):
        super().__init__(nome, descricao, recompensa)
        self.regiao_destino = regiao_destino
        self.distancia_em_km = distancia_em_km
        
    @property
    def regiao_destino(self):
        return self.__regiao_destino
    
    @regiao_destino.setter
    def regiao_destino(self, regiao:str):
        self.__regiao_destino = regiao.strip().lower()
        
    @property
    def distancia_em_km(self):
        return self.__distancia_em_km
    
    @distancia_em_km.setter
    def distancia_em_km(self, qnt:float):
        if isinstance(qnt, (float,int)):
            if qnt > 0:
                self.__distancia_em_km = qnt
            else:
                raise Exception(f"Distância deve ser maior que Zero")
        else:
            raise Exception(f"Distância deve ser um valor numérico")

    def exibir_dados(self):
            str = super().exibir_dados()
            str += f"\nTerritório a Conquistar: {self.regiao_destino}"
            str += f"\nDistância a conquistar: {self.distancia_em_km}"
            return str
        
    def concluir_missao(self, valor):
        if isinstance(valor, (float,int)):
            if valor >= self.distancia_em_km:
                if(self.status == Status.EM_ANDAMENTO):
                    self.status = Status.CONCLUIDA
                    return f"Missão concluída como sucesso. A contabilidade do prêmio de {self.recompensa} XP agora está pronta para retirada financeira."
                else:
                    return f"A missão {self.nome} não está em andamento."
            else:
                self.status = Status.FRACASSADA
                return f"Missão fracassada"
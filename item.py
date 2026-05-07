from enum import Enum

class TipoItem(Enum):
    ARMA = 1
    VESTIMENTA = 2
    UTILITARIO = 3

class Item():
    def __init__(self, nome, descricao:str, tipo, valorEfeito):
        self.__nome = None
        self.__descricao = None
        self.__tipo = None
        self.__valorEfeito = None

        self.nome = nome
        self.descricao = descricao
        self.tipo = tipo
        self.valorEfeito = valorEfeito

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter 
    def nome(self, valor):
        if valor and valor.strip():
            self.__nome = valor.strip().title()
        else: 
            raise ValueError("Nome inválido")
        
    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, valor):
        if valor and valor.strip():
            self.__descricao = valor.strip()
        else:
            raise ValueError("Descrição inválida")
    
    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, valor):
        if isinstance(valor, TipoItem):
            self.__tipo = valor
        else: 
            raise ValueError("Tipo inválido")
        
    @property
    def valorEfeito(self):
        return self.__valorEfeito

    @valorEfeito.setter
    def valorEfeito(self, valor):
        if valor >= 0:
            self.__valorEfeito = valor
        else:
            raise ValueError("Valor do efeito inválido")

    def __str__(self):
        return (
            f"Item: {self.nome} | "
            f"Tipo: {self.tipo.name} | "
            f"Efeito: {self.valorEfeito}"
        )
from missoes import Missao
from status import *
from item import Item, TipoItem

class Personagem:
    def __init__(self, nome):
        self.__nome = None
        self.__nivel = 1
        self.__vida = 100
        self.__xp = 0

        self.__ataqueBase = 0 
        
        self.__inventario: list[Item] = []
        self.__arma_equipada = None
        self.__vestimenta_equipada = None
        self.__utilitario_equipado = None
        

        self.__missoes: list[Missao] = []

        self.nome = nome


    @property
    def vida(self):
        return self.__vida
    
    @property
    def ataqueBase(self):
        return self.__ataqueBase
    
    @ataqueBase.setter
    def ataqueBase(self, valor):
        if isinstance(valor, (int, float)) and valor >= 0:
            self.__ataqueBase = valor
        else:
            raise ValueError("Ataque base deve ser um número não-negativo")

    @property
    def inventario(self):
        return self.__inventario
    
    @property
    def arma_equipada(self):
        return self.__arma_equipada
    
    @property
    def vestimenta_equipada(self):
        return self.__vestimenta_equipada
    
    @property
    def utilitario_equipado(self):
        return self.__utilitario_equipado

    def __reduzir_vida(self,valor):
        if self.vida > 0:
            if (valor <= self.vida):
                self.__vida -= valor
                return
            elif valor <= 0:
                return ("Valor inválido!! Informe valor positivo")
            
            else:
                self.__vida = 0
                raise Exception("Game Over")
            

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
                        ganho_nivel = self.__xp // 20
                        self.__nivel += ganho_nivel
                        self.__xp = self.__xp % 20
                        
                elif m.status == Status.FRACASSADA:
                    self.__reduzir_vida(10)
                    
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
        
    def adicionar_item_inventario(self, item: Item):
        """Adiciona um item ao inventário do personagem"""
        if not isinstance(item, Item):
            raise ValueError("Apenas objetos da classe Item podem ser adicionados")
        self.__inventario.append(item)
    
    def remover_item_inventario(self, item: Item):
        """Remove um item do inventário do personagem"""
        if item in self.__inventario:

            if self.__arma_equipada == item:
                self.__arma_equipada = None
            elif self.__vestimenta_equipada == item:
                self.__vestimenta_equipada = None
            elif self.__utilitario_equipado == item:
                self.__utilitario_equipado = None
            
            self.__inventario.remove(item)
        else:
            raise ValueError("Item não encontrado no inventário")
    
    def equipar_item(self, item: Item):
        """Equipa um item do inventário baseado no seu tipo"""
        if item not in self.__inventario:
            raise ValueError("Item não está no inventário")
        
        if item.tipo == TipoItem.ARMA:
            self.__arma_equipada = item
        elif item.tipo == TipoItem.VESTIMENTA:
            self.__vestimenta_equipada = item
        elif item.tipo == TipoItem.UTILITARIO:
            self.__utilitario_equipado = item
        else:
            raise ValueError("Tipo de item inválido")
    
    def desequipar_item(self, tipo_item: TipoItem):
        """Desequipa um item do tipo especificado"""
        if tipo_item == TipoItem.ARMA:
            self.__arma_equipada = None
        elif tipo_item == TipoItem.VESTIMENTA:
            self.__vestimenta_equipada = None
        elif tipo_item == TipoItem.UTILITARIO:
            self.__utilitario_equipado = None
        else:
            raise ValueError("Tipo de item inválido")
    
    def desequipar_item_por_objeto(self, item: Item):
        """Desequipa um item específico se ele estiver equipado"""
        if item == self.__arma_equipada:
            self.__arma_equipada = None
            return f"{item.nome} (Arma) foi desequipado"
        elif item == self.__vestimenta_equipada:
            self.__vestimenta_equipada = None
            return f"{item.nome} (Vestimenta) foi desequipado"
        elif item == self.__utilitario_equipado:
            self.__utilitario_equipado = None
            return f"{item.nome} (Utilitário) foi desequipado"
        else:
            raise ValueError("Este item não está equipado")
    
    def listar_inventario(self):
        """Lista todos os itens do inventário"""
        if len(self.__inventario) == 0:
            return f"{self.nome} não possui itens no inventário"
        
        msg = f"Inventário de {self.nome}:\n"
        for idx, item in enumerate(self.__inventario, 1):
            equipado = " (EQUIPADO)" if self._is_item_equipado(item) else ""
            msg += f"{idx}. {item}{equipado}\n"
        return msg
    
    def _is_item_equipado(self, item: Item) -> bool:
        """Verifica se um item está equipado"""
        return (item == self.__arma_equipada or 
                item == self.__vestimenta_equipada or 
                item == self.__utilitario_equipado)
    
    def calcular_ataque_total(self) -> float:
        """
        Calcula o ataque total do personagem.
        Ataque Total = ataqueBase + valorEfeito da Arma equipada (se houver)
        """
        ataque_total = self.__ataqueBase
        
        if self.__arma_equipada is not None:
            ataque_total += self.__arma_equipada.valorEfeito
        
        return ataque_total
    
    def calcular_vida_total(self) -> int:
        """
        Calcula a vida total do personagem com os bônus percentuais dos itens.
        Vida Total = vidaBase * (1 + (bônus% da Vestimenta + bônus% do Utilitário) / 100)
        Máximo de vida: 100
        """
        vida_base = 100  
        bonus_percentual = 0
        
        if self.__vestimenta_equipada is not None:
            bonus_percentual += self.__vestimenta_equipada.valorEfeito
        
        if self.__utilitario_equipado is not None:
            bonus_percentual += self.__utilitario_equipado.valorEfeito
        
        vida_total = vida_base + (vida_base * bonus_percentual / 100)
        
        vida_total = min(vida_total, 100)
        
        return int(vida_total)
        
    @property
    def nome(self):
        return self.__nome

    @property
    def nivel(self):
        return self.__nivel

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
        msg += (f"vida total com bônus: {self.calcular_vida_total()}\n")
        msg += (f"ataque base: {self.ataqueBase}\n")
        msg += (f"ataque total com equipamento: {self.calcular_ataque_total()}\n")
        msg += (f"XP: {self.xp}\n")
        msg += "--- Itens Equipados ---\n"
        msg += (f"Arma: {self.arma_equipada if self.arma_equipada else 'Nenhuma'}\n")
        msg += (f"Vestimenta: {self.vestimenta_equipada if self.vestimenta_equipada else 'Nenhuma'}\n")
        msg += (f"Utilitário: {self.utilitario_equipado if self.utilitario_equipado else 'Nenhum'}\n")
        msg += "\n" + self.listar_missoes()
        return msg
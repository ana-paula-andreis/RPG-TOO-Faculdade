from enum import Enum

class Status(Enum):
    PENDENTE = "pndente"
    EM_ANDAMENTO = "em andamento"
    CONCLUIDA = "concluida"
    FRACASSADA = "fracassada"
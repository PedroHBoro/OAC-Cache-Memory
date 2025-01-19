from random import randint
from dataclasses import dataclass

@dataclass
class Bloco:
    ordem: int # Ordem de inserção
    valores: list # Lista de valores inteiros
    id: int # Identificador de bloco
    hits: int = 0 # Quantidade de Cache-Hits do bloco


def ramGenerator(tamanho: int) -> list[list]:
    lista = []
    for _ in range(tamanho):
        valor = randint(0, 10000)

        repetido = valor in lista
        while repetido:
            valor = randint(0, 10000)
            repetido = valor in lista
        lista.append(valor)
    return lista
 
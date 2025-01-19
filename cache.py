from ram import Bloco

class Cache:
    def __init__(self, ram: list[int], algoritmo: str, tamanho: int = 4):

        if algoritmo != 'FIFO' and algoritmo != 'LFU' and algoritmo != 'LRU':
            raise ValueError('Algoritmo iválido!')

        self.ram: list[int] = ram # Dados da memória RAM
        self.cache: list[Bloco] = [Bloco(i, [], -1) for i in range(tamanho)] # Dados da memória Cache
        self.algoritmo: str = algoritmo # Algorítmo de substituição, pode ser: 'LRU', 'LFU' e 'FIFO'
        self.ordem: int = tamanho # Ordem de insersão (Ordem de Acesso no alg LRU). Identificador atribuído ao próximo bloco acessado
    
    def imprimirRam(self):
        print('\n___ RAM ___')
        print('posição | valor')
        for i in range(len(self.ram)):
            if i % 4 == 0: print(f'\n___ {i//4} ___')
            print(f'{i}  |  [{self.ram[i]}]')

    def imprimirCache(self):
        print('\n___ CACHE ___')
        print('\nposição da ram | valores | hits')
        for i in self.cache:
            print(f'{i.id if i.id > -1 else '/'} - {i.valores} - [{i.hits}]')

    def proxRemover(self):
        remover = 0
        for i in range(len(self.cache)):
            if self.cache[i].ordem < self.cache[remover].ordem:
                remover = i
        
        if self.algoritmo == 'LFU':
            for i in range(len(self.cache)):
                if self.cache[i].hits == self.cache[remover].hits and self.cache[i].ordem < self.cache[remover].ordem:
                    remover = i
                elif self.cache[i].hits < self.cache[remover].hits:
                    remover = i
        return remover

    def insere(self, bloco: list[int], posicao: int):
        remover = self.proxRemover()
        for i in range(len(self.ram)):
            if i // 4 == self.cache[remover].id:
                self.ram[i] = self.cache[remover].valores[i%4]
        self.cache[remover] = Bloco(self.ordem, bloco, posicao // 4)
        self.ordem += 1

    def acessar(self, posicao: int, substituir: int|None = None):
        if posicao >= len(self.ram) or posicao < 0:
            raise ValueError('Posição invalida')

        for i in self.cache:
            if i.id == posicao // 4:
                if self.algoritmo == 'LRU':
                    i.ordem = self.ordem
                    self.ordem += 1
                i.hits += 1
                if substituir != None:
                    i.valores[posicao%4] = substituir
                return
        
        aux = []
        for i in range(len(self.ram)):
            if i // 4 == posicao // 4:
                if substituir != None and i == posicao:
                    aux.append(substituir)
                else: aux.append(self.ram[i])
        self.insere(aux, posicao)
from cache import Cache
from ram import ramGenerator

def main():
    ram = ramGenerator(500)
    rodando = True
    cacheMenu = ['\nEscolha o algoritmo de substituição', 
                    '   [1] -- FIFO', 
                    '   [2] -- LFU', 
                    '   [3] -- LRU',
                    '   [4] -- Sair\n']
    while rodando:
        for i in cacheMenu:
            print(i)

        cache = None
        algoritmo = input('-->  ')
        match algoritmo:
            case '1': cache = Cache(ram, 'FIFO')
            case '2': cache = Cache(ram, 'LFU')
            case '3': cache =Cache(ram, 'LRU')
            case '4': rodando = False
            case _: print('Algoritmo inválido!')
        
        if cache != None:
            principal = True
            while principal:
                try:
                    menuPrincipal = ['\nEscolha uma opção',
                                    '   [1] -- Imprimir RAM',
                                    '   [2] -- Imprimir Cache',
                                    '   [3] -- Acessar posição da RAM',
                                    '   [4] -- Acessar e substituir dado da RAM',
                                    '   [5] -- Sair\n']
                    for i in menuPrincipal:
                        print(i)

                    opcao = input('-->  ')

                    match opcao:
                        case '1': cache.imprimirRam()
                        case '2': cache.imprimirCache()
                        case '3': cache.imprimirRam(); cache.acessar(int(input('\nPosição --> '))); cache.imprimirCache()
                        case '4': cache.imprimirRam(); cache.acessar(int(input('\nPosição --> ')), int(input('\nSubstituir por --> '))); cache.imprimirCache()
                        case _: principal = False
                except:
                    print('\nErro ao acessar memória')

if __name__ == '__main__':
    main()
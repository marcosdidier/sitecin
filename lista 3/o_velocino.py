informacoes_deuses = [
    ['Zeus', 'Poseidon', 'Atenas', 'Ares', 'Afrodite'],
    [100, 90, 80, 70, 60],
    ['Raio', 'Tridente', 'Égide', 'Lança', 'Cinto Mágico']
]

icompleto = ''
sequencia = input()

for i in sequencia:
    iint = int(i)
    icompleto += i
    if icompleto == sequencia:
        if iint == 2 or iint == 4:
            print(f'Deusa:{informacoes_deuses [0] [iint]}')
            print(f'Poder:{informacoes_deuses [1] [iint]}')
            print(f'Artefato:{informacoes_deuses [2] [iint]}')
        else:
            print(f'Deus:{informacoes_deuses [0] [iint]}')
            print(f'Poder:{informacoes_deuses [1] [iint]}')
            print(f'Artefato:{informacoes_deuses [2] [iint]}')
    else:
        if iint == 2 or iint == 4:
            print(f'Deusa:{informacoes_deuses [0] [iint]}')
            print(f'Poder:{informacoes_deuses [1] [iint]}')
            print(f'Artefato:{informacoes_deuses [2] [iint]}')
            print('')
        else:
            print(f'Deus:{informacoes_deuses [0] [iint]}')
            print(f'Poder:{informacoes_deuses [1] [iint]}')
            print(f'Artefato:{informacoes_deuses [2] [iint]}')
            print('')
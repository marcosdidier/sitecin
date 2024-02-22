nome_filme1 = str(input())
pontuacao_global_filme1 = int(input())
critica_filme1 = str(input())
nome_filme2 = str(input())
pontuacao_global_filme2 = int(input())
critica_filme2 = str(input())
nome_filme3 = str(input())
pontuacao_global_filme3 = int(input())
critica_filme3 = str(input())
pontfinal1 = 0
pontfinal2 = 0
pontfinal3 = 0
p1 = 'a'
p2 = 'a'
p3 = 'a'

if critica_filme1 == 'boa':
    pontfinal1 = pontuacao_global_filme1 * 1.25

elif critica_filme1 == 'media':
    pontfinal1 = pontuacao_global_filme1 * 1

elif critica_filme1 == 'ruim':
    pontfinal1 = pontuacao_global_filme1 * 0.75

elif critica_filme1 == 'pessima':
    pontfinal1 = 0

if critica_filme2 == 'boa':
    pontfinal2 = pontuacao_global_filme2 * 1.25

elif critica_filme2 == 'media':
    pontfinal2 = pontuacao_global_filme2 * 1

elif critica_filme2 == 'ruim':
    pontfinal2 = pontuacao_global_filme2 * 0.75

elif critica_filme2 == 'pessima':
    pontuacao_global_filme2 = 0

if critica_filme3 == 'boa':
    pontfinal3 = pontuacao_global_filme3 * 1.25

elif critica_filme3 == 'media':
    pontfinal3 = pontuacao_global_filme3 * 1

elif critica_filme3 == 'ruim':
    pontfinal3 = pontuacao_global_filme3 * 0.75

elif critica_filme3 == 'pessima':
    pontfinal3 = 0

print('****TOP 3 FILMES****')

if pontfinal1 == pontfinal2 or pontfinal1 == pontfinal3 or pontfinal2 == pontfinal3:
    end = ''

elif pontfinal1 > pontfinal2 and pontfinal1 > pontfinal3 and pontfinal2 > pontfinal3:
    p1 = nome_filme1
    p2 = nome_filme2
    p3 = nome_filme3
    print(f'{p1} está em 1° lugar')
    print(f'{p2} está em 2° lugar')
    print(f'{p3} está em 3° lugar')

elif pontfinal1 > pontfinal2 and pontfinal1 > pontfinal3 and pontfinal3 > pontfinal2:
    p1 = nome_filme1
    p2 = nome_filme3
    p3 = nome_filme2
    print(f'{p1} está em 1° lugar')
    print(f'{p2} está em 2° lugar')
    print(f'{p3} está em 3° lugar')

elif pontfinal2 > pontfinal1 and pontfinal2 > pontfinal3 and pontfinal1 > pontfinal3:
    p1 = nome_filme2
    p2 = nome_filme1
    p3 = nome_filme3
    print(f'{p1} está em 1° lugar')
    print(f'{p2} está em 2° lugar')
    print(f'{p3} está em 3° lugar')

elif pontfinal2 > pontfinal1 and pontfinal2 > pontfinal3 and pontfinal3 > pontfinal1:
    p1 = nome_filme2
    p2 = nome_filme3
    p3 = nome_filme1
    print(f'{p1} está em 1° lugar')
    print(f'{p2} está em 2° lugar')
    print(f'{p3} está em 3° lugar')

elif pontfinal3 > pontfinal1 and pontfinal3 > pontfinal2 and pontfinal1 > pontfinal2:
    p1 = nome_filme3
    p2 = nome_filme1
    p3 = nome_filme2
    print(f'{p1} está em 1° lugar')
    print(f'{p2} está em 2° lugar')
    print(f'{p3} está em 3° lugar')

elif pontfinal3 > pontfinal1 and pontfinal3 > pontfinal2 and pontfinal2 > pontfinal1:
    p1 = nome_filme3
    p2 = nome_filme2
    p3 = nome_filme1
    print(f'{p1} está em 1° lugar')
    print(f'{p2} está em 2° lugar')
    print(f'{p3} está em 3° lugar')

if pontfinal1 == 0:
    print(f'{nome_filme1} teve uma crítica péssima')

if pontfinal2 == 0:
    print(f'{nome_filme2} teve uma crítica péssima')

if pontfinal3 == 0:
    print(f'{nome_filme3} teve uma crítica péssima')








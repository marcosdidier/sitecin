nome_animal = input('Digite o nome do animal: ')
distancia = int(input('Digite a distância que será percorrida pelo animal (em cm): '))
t_passo = int(input('Digite o tamanho do passo do animal (em cm): '))
n_passos = 0


for i in range (0, distancia, t_passo):
    n_passos += 1

print(f'Cada {nome_animal} percorrerá uma distância de {distancia} centímetros e dará {n_passos} passos.')
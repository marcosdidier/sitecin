from random import randint
num = randint (0, 100)
tentativa = int(input('Digite o número que você acha que foi escolhido pelo programa: '))
while tentativa != num:
    if tentativa > num:
        print('Quase! Porém o número escolhido é menor')
    elif tentativa < num:
        print('Quase! Porém o número escolhido é maior')
    tentativa = int(input())
    
else:
    print('Você ganhou!')
    
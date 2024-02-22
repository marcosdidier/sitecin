from random import randint

def comando():
    num = randint(0, 10)
    cond = False
    tentativa = int(input('Digite um número aleatório entre 0 e 10: '))
    while not cond:
        if tentativa == num:
            print('Parabéns, você acertou!')
            cond = True
        elif tentativa < num:
            tentativa = int(input('Tente um número maior: '))
        else:
            tentativa = int(input('Tente um número menor: '))
    else:
        print('Fim de jogo!')

comando()
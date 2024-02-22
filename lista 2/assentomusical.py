qnt_musicas = int(input())
numero_assento = 1

for x in range(qnt_musicas):
    musica = input()
    analise = musica.lower()
    pontuacao = 0
    for i in analise:
        if i in 'aeiou':
            pontuacao += 1
        elif i in 'bcdfghjklmnpqrstvwxyz':
            pontuacao += 2

    numero_assento *= pontuacao

print(f'Parabéns por adquirir o ingresso! Seu assento é o {numero_assento}, estamos ansiosos para vê-lo, vai ser incrível!')
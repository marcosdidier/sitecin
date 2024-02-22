opiniao = 'a'
minutos_escutados = 0
musicas_album = 0
comentario = 'a'
vezes_escutadas = 0

while musicas_album != 21 and opiniao != 'parei':
    opiniao = input()
    if opiniao == 'amei':
        minutos_escutados += 4
        musicas_album += 1
    elif opiniao == 'essa não deu':
        musicas_album += 1
    elif opiniao == 'escutei só metade':
        minutos_escutados += 2
        musicas_album += 1
    elif opiniao == 'não parei de ouvir':
        comentario = input()
        while comentario != 'pulei':
            comentario = input()
            minutos_escutados += 4
        musicas_album += 1
        
else:
    print(f'Você ouviu {minutos_escutados} minutos hoje!!!')
    
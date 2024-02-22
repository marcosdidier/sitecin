sequencia = ''
labirintol = []
labirintoc = []
posicaoc = []
linha = 0
coluna = 0
reliquias = 0
cond = False
while not cond:
    sequencia = input()
    if sequencia == 'Fim do labirinto':
        cond = True
    else:
        sequencialista = sequencia.split()
        for objeto in range(len(sequencialista)):
            if sequencialista[objeto] == '0':
                reliquias += 0
            elif sequencialista[objeto] == '1':
                reliquias += 1
                labirintol.append(linha)
                labirintoc.append(objeto)
        
    linha += 1

tamanho_lab = int(len(labirintol))

if reliquias == 0:
    print('Nenhuma relíquia encontrada no labirinto.')

else:
    print('Relíquias encontradas nos seguintes locais:')
    for i in range(tamanho_lab): 
        print(f'linha: {labirintol[i]}, coluna: {labirintoc [i]}')
        

    


nome_missao = input()
herois = []
cond = False

while not cond:
    novo_heroi = input()
    if novo_heroi == 'Grupo formado':
        cond = True
    else:
        herois.append(novo_heroi)
    tamanho = int(len(herois))

print(f'O grupo formado por {tamanho} heróis para a missão {nome_missao} foi:')
for heroi in herois:
    print(f'- {heroi}')
    



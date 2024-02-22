nome_pretendente = input()

while nome_pretendente != 'vou dormir':
    palavra_pretendente = input()
    palavra_taylor = input()
    cond = True

    for x in palavra_taylor:
        if x in palavra_pretendente:
            palavra_pretendente = palavra_pretendente.replace(x, '', 1)
        else:
            cond = False
            
    if cond:
        print(f'você acertou, estreou na lista! {nome_pretendente}')
    else:
        print('perdeu covarde!')
    
    nome_pretendente = input()


produtos_loja = ['ombro', 'joelho', 'tornozelo', 'pé']
produtos_estoque = ['tornozelo', 'ombro','joelho', 'pé', 'joelho', 'ombro', 'pé', 'tornozelo', 'ombro','tornozelo', 'ombro', 'joelho']

for produtos in produtos_loja:
    qtd = 0
    for estoque in produtos_estoque:
        if produtos == estoque:
            qtd +=1    
    print(f'Existem {qtd} {produtos} em estoque.')
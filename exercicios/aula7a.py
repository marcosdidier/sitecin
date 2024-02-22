produtos_vendidos = ['martelo', 'alicate', 'chave de fenda', 'chave estrel', 'tesoura']
produtos_estoque = ['martelo', 'alicate', 'martelo', 'martelo', 'chave de fenda', 'alicate', 'chave estrela']
qtd_produto = 0 
vende_produto = False


consulta = input()
for vendidos in produtos_vendidos:
    if vendidos == consulta:
        vende_produto = True
        
if vende_produto:
    for estoque in produtos_estoque:
        if estoque == consulta:
            qtd_produto += 1
        
if not vende_produto:
    print('Não vendemos esse produto!')

elif qtd_produto > 0:
    print(f'Existem {qtd_produto} {consulta}(s) em estqoue na nossa loja!')

else:
    print(f'O estqoque de {consulta} está zerado!')
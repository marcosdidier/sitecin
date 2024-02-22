itens_necessarios = input()
lista_necessarios = itens_necessarios.split(', ')
tamanho_necessarios = int(len(lista_necessarios))
itens_achados = input()
lista_achados = itens_achados.split(', ')
tamanho_achados = int(len(lista_achados))
i = 1
quantidade_n_encontrados = tamanho_necessarios
quantidade_encontrados = 0


for item in lista_necessarios:
    if item in lista_achados:
        quantidade_n_encontrados -= 1
        quantidade_encontrados += 1
if quantidade_encontrados > 0:
    print('Estes são os itens que já tenho no Acampamento Meio-Sangue:')
    for item in lista_necessarios:
        if item in lista_achados:
           print (f'{i}º item: {item}')
           i += 1
if quantidade_encontrados == tamanho_necessarios:
    print(f'Perfeito, encontrei todos os {tamanho_necessarios} itens aqui no Acampamento Meio-Sangue!')
elif quantidade_encontrados > 0:
    print(f'Vou precisar adquirir {quantidade_n_encontrados} itens antes da batalha!')
elif quantidade_encontrados == 0:
    print(f'Hmm, preciso visitar um vendedor ambulante! Não encontrei nenhum dos {tamanho_necessarios} itens aqui no Acampamento Meio-Sangue.')
print('Estou pronto para a batalha! Que comece a guerra contra os Titãs!')

    
    
    
    
    
    

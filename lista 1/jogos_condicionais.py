nome_vitima = str(input())
nome_antagonista = str(input())
tipo_armadilha = str(input())
tempo = int(input())

if nome_antagonista == 'John Kramer' and tipo_armadilha == 'Armadilha de urso reversa' and tempo >= 300:
    print(f'Com tempo de sobra, {nome_vitima} consegue retirar a armadilha de sua cabeça, sobrevivendo com sucesso ao jogo de Jigsaw.')

elif nome_antagonista == 'John Kramer' and tipo_armadilha == 'Armadilha de urso reversa' and tempo >= 150: 
    print(f'À beira de perder a cabeça, e desafiando as expectativas de seu algoz, {nome_vitima} remove a armadilha de urso e por pouco escapa de um destino cruel.')

elif nome_antagonista == 'John Kramer' and tipo_armadilha == 'Tanque de agua' and tempo >= 240:
    print(f'{nome_vitima} usa suas práticas de respiração na natação a seu favor, vencendo o jogo de Jigsaw sem perder muito fôlego.')

elif nome_antagonista == 'John Kramer' and tipo_armadilha == 'Tanque de agua' and tempo >= 120:
    print(f'{nome_vitima} passa por maus bocados, mas vira o jogo e consegue evitar, no limite, seu afogamento dentro da armadilha.')

elif nome_antagonista == 'Amanda Young' and tipo_armadilha == 'Caixa de laminas' and tempo >= 600:
    print(f'Apenas com ferimentos leves, {nome_vitima} se liberta rapidamente das perigosas lâminas da armadilha montada pela discípula de Jigsaw.')

elif nome_antagonista == 'Amanda Young' and tipo_armadilha == 'Caixa de laminas' and tempo >= 360:
    print(f'Por um triz, {nome_vitima} sobrevive ao jogo de Amanda, mas com lesões profundas em suas mãos e braços.')

elif nome_antagonista == 'Amanda Young' and tipo_armadilha == 'Asas de anjo' and tempo >= 180:
    print(f'Com surpreendente facilidade, {nome_vitima} alcança a chave da armadilha e vence o desafio da aprendiz de Jigsaw.')

elif nome_antagonista == 'Amanda Young' and tipo_armadilha == 'Asas de anjo' and tempo >= 90:
    print(f'{nome_vitima} desafia as possibilidades e o cruel anseio de sua algoz, escapando da armadilha com poucas queimaduras e arranhões.')

else:
    print('Game Over...')

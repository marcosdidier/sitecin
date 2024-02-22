frase = str(input())
carac = str(input())

if frase == 'Parou filhotada, assim vocês vão deixar todo mundo maluco.':
    if carac == 'Uivar' or carac == 'Pelos' or carac == 'Caninos':
        print('Bem-vindos ao Hotel Transilvânia!')
        print('Wayne, seu cachorrão.')
    
    else:
        print('UM HUMANO! Quem é você, e como você achou esse lugar?')

elif frase == 'Veio de novo pelo correio, deixa de ser pão duro.':
    if carac == 'Desmontável' or carac == 'Parafusos' or carac == 'Morto-vivo':
        print('Bem-vindos ao Hotel Transilvânia!')
        print('Frank, assim vai acabar perdendo a cabeça.')

    else:
        print('UM HUMANO! Quem é você, e como você achou esse lugar?')

elif frase == 'Quem me beliscou?':
    if carac == 'Transparente':
       print('Bem-vindos ao Hotel Transilvânia!')
       print('Griffin, prazer em vê-lo.')

    else:
        print('UM HUMANO! Quem é você, e como você achou esse lugar?')


elif frase == 'Tô na área galera!':
    if carac == 'Enfaixado' or carac == 'Morto-vivo':
       print('Bem-vindos ao Hotel Transilvânia!')
       print('Murray, sempre soltando areia.')

    else:
        print('UM HUMANO! Quem é você, e como você achou esse lugar?')

else:
    print('UM HUMANO! Quem é você, e como você achou esse lugar?')
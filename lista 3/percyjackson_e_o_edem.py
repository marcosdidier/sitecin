lista1 = ['Zeus', 'deus', 'trovão']
lista2 = ['Afrodite', 'amor', 'deusa']
lista3 = ['Poseidon', 'deus', 'oceanos']
lista4 = ['Hércules', 'força', 'semideus']
lista5 = ['Aquiles', 'resistência', 'semideus']
lista6 = ['Orfeu', 'música', 'semideus']
acertos = 0
porcentagem = 0
qtd_questoes = int(input())
if qtd_questoes == 0:
    print('Infelizmente, Percy Jackson, chegou atrasado para a exame...')
else:
    for i in range(1, qtd_questoes + 1):
        resposta = input()
        resposta_nova = resposta.replace(',', '')
        resposta_qs_final = resposta_nova.split()
        final = sorted(resposta_qs_final)
        if final == lista1 or final == lista2 or final == lista3 or final == lista4 or final == lista5 or final == lista6:
            print(f'A resposta da {i}ª questão está... CORRETA!')
            acertos += 1
        else:
            print(f'A resposta da {i}ª questão está... ERRADA!')
    porcentagem = int((acertos / qtd_questoes) * 100)
    print(f'Percy Jackson, sua taxa de acerto no EDEM é de aproximadamente... {porcentagem}%')
    if porcentagem >= 100:
        print('UAU, você gabaritou! Você é praticamente um deus do Olimpo!')
    elif porcentagem > 60:
        print('Muito bem, você quase pode começar a desfilar entre os semideuses!')
    elif porcentagem > 20:
        print('Você pode melhorar um pouco mais!')
    else:
        print('Bem... te vejo ano que vem')








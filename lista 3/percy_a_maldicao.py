saga = ['O Ladrão de Raios', 'O Mar de Monstros', 'A Maldição do Titã', 'A Batalha do Labirinto', 'O Último Olimpiano']
tamanho_saga = int(len(saga))
colecao = input()
lista_colecao = colecao.split(', ')
qtd_total_edicoes = int(input())
livros_faltando = []
bagunca = []
numerolivros = 0


for livro in lista_colecao:
       if livro in saga:
           numerolivros += 1
       else:
           bagunca.append(livro)

for i in saga:
    if i not in lista_colecao:
        livros_faltando.append(i)

strbagunca = ', '.join(bagunca)
strfalta = ', '.join(livros_faltando)


if numerolivros == tamanho_saga:
    print('Sua coleção está completa! Você pode ler à vontade.')
elif numerolivros > 0:
    print(f'Infelizmente, sua coleção está incompleta. Falta(m) esse(s) livro(s): {strfalta}.')
elif numerolivros == 0:
    print('Caramba, você não tem nenhum livro. Compre todos imediatamente.')
if strbagunca != '':
    print(f'Cuidado, Sérgio! Você está organizando seus livros de uma forma errada, o(s) livro(s): {strbagunca}, não faz(em) parte da saga "Percy Jackson e os Olimpianos".')



    





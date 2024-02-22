computadores_disponiveis = int(input())
dinheiro_disponivel = float(input())
tempo_espera = int(input())
tempo_minutos = 60 * tempo_espera
quantidade_amigos = 0
nome_amigos = ''
cond1 = False
valor_ingresso = 0
local_show = ''
cond2 = False
contagem_computador = 0
posicao_fila = 0
opcoes_ingressos = 0
computador_vencedor = 0
fila_espera = float("inf")

#Parte do código que analisa a quantidade de amigos
while not cond1:
    nome_amigos = input()
    if nome_amigos == 'end':
        if quantidade_amigos == 0:
            print('Ah não! João não conseguiu nenhum amigo que o ajudasse. Agora ele vai ter que contar com a sorte para pegar um bom lugar na fila, usando apenas seu computador.')
            end = ''
        else:
             print(f'Bom começo! Consegui {quantidade_amigos} amigos que podem me ajudar a comprar o ingresso')
        cond1 = True
    elif nome_amigos == 'laura' or nome_amigos == 'carlos' or nome_amigos == 'roberto':
        quantidade_amigos += 0
    else:
        quantidade_amigos += 1
        if quantidade_amigos == computadores_disponiveis:
            print(f'Bom começo! Consegui {quantidade_amigos} amigos que podem me ajudar a comprar o ingresso')
            cond1 = True 
        
#Parte do código que analisa as condições dos ingressos
while not cond2 and quantidade_amigos > 0:
    valor_ingresso = float(input())
    local_show = input()
    

    if local_show == 'end':
        contagem_computador += 1
    
    elif local_show == 'rio de janeiro' or local_show == 'são paulo' or local_show == 'buenos aires':
        print('Consegui um ingresso em um local que João possa ir! Agora temos que ver o preço')
        contagem_computador += 1
        if valor_ingresso <= dinheiro_disponivel:
            print('Consegui o dinheiro! Agora só falta ver a minha colocação na fila dos ingressos...')
            posicao_fila = int(input())
            #Parte em que se analisa qual computador teve o ingresso com a melhor posição, fila_espera começa com valor infinito e automaticamente é substituida por posicao_fila
            if fila_espera > posicao_fila:
                fila_espera = posicao_fila
                computador_vencedor = contagem_computador
            calculo_tempo_posicao = (10 * posicao_fila) / 16
            

            if calculo_tempo_posicao <= tempo_minutos:
                print('ISSOOO, conseguimos um ingresso!!!')
                opcoes_ingressos += 1
            else:
                
                print(f'Caramba, essa foi quase! Mas infelizmente não consegui um bom lugar na fila dos ingressos no computador de número {contagem_computador}')

    

        else:
            print('Caramba! Só tinha ingresso para a pista vip, que está bem acima do meu orçamento.')
    
    if contagem_computador == quantidade_amigos:
        cond2 = True

if quantidade_amigos > 0:
    if opcoes_ingressos >= 1:
        print(f'Consegui o ingresso! Com {int((opcoes_ingressos/quantidade_amigos)*100)}% de aproveitamento da ajuda dos meus amigos. E a fila escolhida para comprar o ingresso foi do computador número {computador_vencedor}. Rumo ao show da Taylor!!!')

    elif opcoes_ingressos == 0 and quantidade_amigos / computadores_disponiveis > 0.5:
        print('Não acredito que tive amigos para ocuparem mais da metade dos computadores, e ainda assim não consegui um ingresso...')

    else:
        print('Poxa, não acredito que não consegui o ingresso, acho que eu devia ter chamado mais amigos para ajudar.')










def formatacao(lista):
    quantidades = lista.split(' ')
    quantidades_inteiras = list(map(lambda x : int(x), quantidades))
    return(quantidades_inteiras)

def funcao_calculo(qtd_inicial, final):
    lista_quantidade = []
    resposta = ''
    if final in lista_quantidade:
        resposta = 'SIM'
    else:
        lista_quantidade.append(qtd_inicial / 3 * 2)
        lista_quantidade.append(qtd_inicial / 3)
        qtd_inicial1 = lista_quantidade[-1]
        qtd_inicial2 = lista_quantidade [-2]
        funcao_calculo(qtd_inicial1, qtd_inicial2)
        resposta = 'NÃO'

    return(resposta)
    

num_pedidos = int(input())
for i in range(num_pedidos):
    lista = input()
    qtd_inicial, final = formatacao(lista)[0], formatacao(lista)[1]
    funcao_lista()
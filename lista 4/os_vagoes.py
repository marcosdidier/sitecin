#Criando a função de organização das malas
def organizar_as_malas(pesos_str):
    lista_pesos_str = pesos_str.split(', ')
    #Linha 5 representa a passagem da entrada string para inteiros para que o programa possa organizar os valores
    listinha_int = list(map(lambda x: int(x) , lista_pesos_str))
    #Da linha 7 a 9 temos a ordenação dos valores em ordem crescente e depois são feitas as trocas que a questão pediu
    listinha_int.sort()
    listinha_int[0], listinha_int[-1] = listinha_int[-1], listinha_int[0]
    listinha_int[1], listinha_int[-2] = listinha_int[-2], listinha_int[1]
    #Linha 11 e 12 representam passagem da lista já organizada de inteiros para strings e depois a formação de apenas uma string com a resposta
    listinha_str = list(map(lambda x: str(x) , listinha_int))
    resultado = ', '.join(listinha_str)
    return(resultado)

#Criando a função parâmetros
def parametros(qtd_blocos, peso, n_passageiros):
    #Aqui em vez de usar o elemento return eu decidi retornar um print com tudo que seria necessário para essa função, preferi fazer assim, mas ainda não testei usar um return triplo
    velocidade = int((qtd_blocos + 200) / 2)
    carga = int((peso + 4000) / 1000)
    n_pessoas = n_passageiros + 40
    print(f'A velocidade que o trem partirá é de: {velocidade}Km/H')
    print(f'A carga do Trem em Toneladas é: {carga} Ton.')
    print(f'A quantidade de passageiros é de {n_pessoas}')

#Criando a função turno
def turno(hora_final, n_roteiro, lista_funcionarios):
    if (7 < hora_final < 21):
        if n_roteiro == 'Roteiro 1':
            lista_nova = [lista_funcionarios[0], lista_funcionarios[1]]
            nomes = ', '.join(lista_nova)
            print(f'Os funcionários convocados são: {nomes}')
        elif n_roteiro == 'Roteiro 2':
            lista_nova = [lista_funcionarios[0], lista_funcionarios[-1]]
            nomes = ', '.join(lista_nova)
            print(f'Os funcionários convocados são: {nomes}')
    elif hora_final <= 7 or hora_final >= 21:
        if n_roteiro == 'Roteiro 1':
            print(f'Os funcionários convocados são: {lista_funcionarios[2]}')
        elif n_roteiro == 'Roteiro 2':
            print('Os funcionários convocados são: Nenhum! O turno da Madrugada vai ser tranquilo para todos')

#Fiz essa função para formatar a entrada com a informação do horário e converter ela em um inteiro
def formatacao_hora(hora):
    hora1 = hora[0] + hora[1]
    hora1_int = int(hora1)
    hora2 = hora[3] + hora[4]
    hora2_int = int(hora2)
    hora2_formatada = hora2_int / 60
    hora_final = hora1_int + hora2_formatada
    return(hora_final)

#Função protocolo de início já com todas as entradas necessárias para o problema e já com o uso de cada uma das 3 funções necessárias com os seus respectivos paramêtros
def protocolo_de_inicio():
    pesos_str = input()
    print(f'A nova organização das malas é a seguinte: {organizar_as_malas(pesos_str)}')
    
    recebimento_func_parametros = input().split(', ')
    entrada = list(map(lambda x: int(x), recebimento_func_parametros))
    parametros(entrada[0], entrada[1], entrada [2])

    lista_funcionarios = input().split(', ')
    hora = input()
    hora_final = formatacao_hora(hora)
    n_roteiro = input()

    turno(hora_final, n_roteiro, lista_funcionarios)

#Chamada da função
protocolo_de_inicio()







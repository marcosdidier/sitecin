#Definição das listas e variáveis que necessitaremos para o problema
lista_completa = []
xdistancias = []
ydistancias =[]
distancias = []
x_noel = 0
y_noel = 0
alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


#Função que transforma os numerais dados no input de string para inteiro para que eles tenham valores numéricos
def transf_int(lista_informacoes):
    lista_informacoes[1], lista_informacoes[2], lista_informacoes[4] = float(lista_informacoes[1]), float(lista_informacoes[2]), int(lista_informacoes[4])
    return(lista_informacoes)

#Função que desfaz a criptografia de cada cidade em função da mensagem dada, do número de vezes que as letras variarão e da direção que elas percorrerão
def funcao_cifra_cesar(criptografia, rodagem, direcao):
    caracteres_traducao = []
    #Esses 2 For são para identificar a letra do input e quando achar a mesma no alfabeto se obtem como resultado a posicão da letra, então é possível somar/subtrair a posição de acordo com os inputs de quantidade de variação e direção de variação
    for i in criptografia:
        posicao = -1
        for j in alfabeto:
            posicao += 1
            if i == j:   
                if direcao == 'R':
                    nova_posicao = posicao + rodagem
                    #Condição para caso a nova posição seja maior do que o número do alfabeto, obtenha-se a posição real usando o resto da divisão para o cálculo
                    if nova_posicao <= 25:
                        posicao_real = nova_posicao
                    else:
                        posicao_real = (nova_posicao % 26)
                elif direcao == 'L':
                    #Condição para caso a nova posição seja maior do que o número do alfabeto, obtenha-se a posição real usando o resto da divisão para o cálculo 
                    nova_posicao = posicao - rodagem
                    if nova_posicao >= -26:
                        posicao_real = nova_posicao
                    else:
                        posicao_real = (nova_posicao % -26)
                letra_final = alfabeto[posicao_real]
                caracteres_traducao.append(letra_final)
        traducao = ''.join(caracteres_traducao)
    return(traducao)

#Função que calcula a distância das cidades
def calculo_distancia(x_noel, y_noel, x_cidade, y_cidade):
    distancia = ((x_noel - x_cidade) ** 2 + (y_noel - y_cidade) ** 2) ** (1/2)
    return(distancia)

#Função que checa as distâncias para sempre ter como output a cidade mais próxima do Papai Noel
def recalculo():
#X e Y do Noel globais para que quando assumirem as coordenadas das cidades visitadas as variáveis funcionem no código todo
    global x_noel
    global y_noel
    distancias = []
#Cálculo das distâncias usando a função de cálculo que já tinha sido criada
    for x, y in zip(xdistancias, ydistancias):
        distancia = calculo_distancia(x_noel, y_noel, x, y)
        distancias.append(distancia)

#Definição dessa variável como infinita pois será necessário para o próximo cálculo
    menor_distancia = float("inf")

#For que acha a menor distância
    for dist in distancias:
        if dist < menor_distancia:
            menor_distancia = dist
    cidade = -1
    for distancia_calculada in distancias:
        cidade += 1
        if distancia_calculada == menor_distancia:
           break
#As coordenadas do papai noel passam a ser as coordenadas da cidade de menor distância
    x_noel = (xdistancias[cidade])
    y_noel = (ydistancias[cidade])
#Remove-se as coordenadas que acabaram de ser utilizadas, pois o papai noel já visitou aquela cidade
    xdistancias.remove(x_noel), ydistancias.remove(y_noel)
    print(f'A senha da cidade {lista_completa[cidade][0]} é: {funcao_cifra_cesar(lista_completa[cidade][3], lista_completa[cidade][4], lista_completa[cidade][5] )}')
#Remove-se toda a informação da cidade da lista completa
    lista_completa.pop(cidade)


#Recebimento de número de cidades
quantidade_de_cidades = int(input())

#Recebimento de informações das cidades + tratamento dos numerais para que assumam valor numérico
for i in range(quantidade_de_cidades):
    lista_informacoes = input().split(', ')
    lista_informacoes = transf_int(lista_informacoes)
    lista_completa.append(lista_informacoes)

#Armazenagem de todas as coordenadas
for lista in lista_completa:
    for listinha in range(len(lista)):
        if listinha == 1:
            xdistancias.append(lista[1])
        elif listinha == 2:
            ydistancias.append(lista[2])

#Solução do problema
for qtd in range(quantidade_de_cidades):
    recalculo()
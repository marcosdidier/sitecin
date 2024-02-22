#Definindo as listas que usei no problema
lista_presentes = []
lista_inicial = []
lista_excluidos = []
lista_caracteres = []
lista_recebidos = []
def decodificacao(entrada):
    #Função que transforma a entrada em inteiros para poder fazer a conversão da entrada na tabela ASCII
    lista_entrada = entrada.split(' ')
    lista_int = list(map(lambda x: int(x), lista_entrada))
    lista_caracteres = []
    #For que traduz todas as letras e coloca elas em uma lista para que depois sejam juntas em uma string resultando no nome do brinquedo traduzido
    for i in lista_int:
        traducao = chr(i)
        lista_caracteres.append(traducao)
    presente = ''.join(lista_caracteres)
    return(presente)

def teste_paridade(entrada):
    lista_caracteres = []
    lista_inicial = entrada.split(' ')
    lista_inteira = list(map(lambda x: int(x), lista_inicial))
    soma = 0
    #For que soma os números que representam cada letra para que possamos verificar se o resultado é par ou ímpar
    for j in lista_inteira:
        soma += j
    #For que decodifica as palavras
    for i in lista_inteira:
        traducao = chr(i)
        lista_caracteres.append(traducao)
    presente = ''.join(lista_caracteres)
    #Condição que irá adicionar a palavra a lista de presentes excluídos ou de presentes recebidos
    if soma % 2 == 0 and presente not in lista_recebidos:
        lista_recebidos.append(presente)
    elif soma % 2 == 1 and presente not in lista_excluidos:
        lista_excluidos.append(presente)
    
#Código
numero_presentes = int(input())

for i in range(numero_presentes):
    #Recebimento dos inputs e uso da função de decodificação para retornar o nome do presente
    entrada = input()
    #Condição para identificar se o presente já foi recebido como entrada antes
    if decodificacao(entrada) in lista_presentes:
        print(f'{decodificacao(entrada)} já está na lista de presentes da Anya!!')
    else:
        print(f'{decodificacao(entrada)} foi adicionado a lista ultrassecreta de presentes da Anya!!')
        lista_presentes.append(decodificacao(entrada))
    #Teste com cada entrada usando a função de paridade para ver se ela será um presente recebido ou não
    teste_paridade(entrada)

#Outputs finais
if len(lista_excluidos) == 0 and len(lista_presentes) > 0:
    print(f'Parece que o Dia das Crianças desse ano será especial!!!! Anya ganhará todos os presentes planejados, mesmo que ela não seja tão exemplar como deveria…')

elif len(lista_excluidos) > 0:
    string_excluidos = ', '.join(lista_excluidos)
    print(f'Infelizmente o Twilight é mão de vaca e os seguintes itens precisaram ser excluídos da lista de presentes ultrassecretos da Anya: {string_excluidos}.')

if len(lista_recebidos) == 0:
    print(f'O quê? Nenhum presente? Isso é um absurdo! Vamos corrigir essa injustiça e garantir que Anya tenha um Dia das Crianças inesquecível!')

else:
    string_presentes = ', '.join(lista_recebidos)
    print(f'Lista final dos melhores presentes da Anya: {string_presentes}.')
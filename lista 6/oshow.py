def formatacao(entrada):
    lista = entrada.split(': ')
    nome = lista[0]
    #Checagem que analisa se a escola é do Rio e se é a primeira vez que ela recebe nota 
    if nome in escolas_rio:
        if nome in escolas_e_notas:
            escolas_e_notas.update({lista[0]: float(lista[1])})
            print(f'{lista[0]} teve sua nota atualizada!')
        else:
            escolas_e_notas.update({lista[0]: float(lista[1])})
            print(f'{lista[0]} teve sua nota apurada!')
    else:
        print('Epa, o que essa escola está fazendo aqui?!')
    lista = []

def maior_nota():
    #Função que organiza as notas em ordem decrescente e passa os nomes e notas para um dicionário atualizado
    temporario = float("-inf")
    for notas in escolas_e_notas.values():
        if notas > temporario:
            temporario = notas
    for nomes, nota in escolas_e_notas.items():
        if nota == temporario:
            escolas_e_notas_atualizado.update({nomes : nota})
            del escolas_e_notas [nomes]
            break
            


#Definição dos dicionários e tuplas que iremos utilizar
escolas_rio = ("Porto da Pedra", "Beija-flor", "Salgueiro", "Grande Rio", "Unidos da Tijuca", "Imperatriz", "Mocidade", "Portela", "Vila Isabel", "Mangueira", "Paraíso do Tuiuti", "Viradouro")
escolas_e_notas = {}
escolas_e_notas_atualizado = {}
tupla_numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
cond1 = False
cond2 = False
cond3 = False

while not cond1:
    entrada = input()
    if entrada == 'Fim':
        cond1 = True
    else:
        formatacao(entrada)

while not cond2:
    maior_nota()
    if escolas_e_notas == {}:
        cond2 = True

#Print da ordem de classificação
print('\nCLASSIFICAÇÃO DO CARNAVAL 2024:')
for numeral, nome, nota in zip(tupla_numeros, escolas_e_notas_atualizado, escolas_e_notas_atualizado.values()):
    print(f'{numeral}. {nome}: {nota}')

#Passagem dos nomes e notas para uma lista para que possamos acessar a primeira e a última posição dos nomes e das notas
escolas_ordem = list(escolas_e_notas_atualizado.keys())
notas_ordem = list(escolas_e_notas_atualizado.values())
escola_campea, escola_perdedora, nota_campea, nota_perdedora = escolas_ordem[0], escolas_ordem[-1], notas_ordem[0], notas_ordem[-1]
#Print final
print(f'\nÉ CAMPEÃ! A ESCOLA {escola_campea} É A GRANDE VENCEDORA DO CARNAVAL DE 2024, FAZENDO {nota_campea} PONTOS!!')
print(f'Infelizmente, a escola {escola_perdedora} não alcançou as expectativas, fazendo apenas {nota_perdedora} pontos, e foi rebaixada.')
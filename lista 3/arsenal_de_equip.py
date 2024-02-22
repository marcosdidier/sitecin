itens_disponiveis = ['Foice de Hades', 'Talismã de Ícaro', 'Elmo da Invisibilidade', 'Cinto de Hermes', 'Espada Anaklusmos', 'Escudo Aegis', 'Adaga Katoptris']
entrada = ''
cond = False
herois = []
lista = []
lista_completa = []

#Formando a lista dos heróis e dos seus respectivos equipamentos
while not cond:
    entrada = input()
    if entrada == 'Parar':
        cond = True
    else:
        lista = entrada.split('-')
        herois.append(lista[0])
        lista_comparativa = itens_disponiveis.copy()
        for i in lista:
            if i in itens_disponiveis:
                lista_comparativa.remove(i)
        if len(lista_comparativa) == 0:
            lista_completa.append('')
        else:
            lista_completa.append(lista_comparativa)


#Output da questão
str_unica = ''
for her, equip in zip(herois, lista_completa):
    str_unica = ''
    str1 = ''
    tamanhoequip = int(len(equip))
    if equip == '':
        print(f'{her} irá batalhar na base do murro!')
    elif tamanhoequip == 1:
        str1 = ''.join(equip)
        print(f'{her} irá rumo a batalha com o equipamento: {str1}!')
    elif tamanhoequip == 2:
        print(f'{her} irá rumo a batalha com os seguintes equipamentos: {equip[0]} e {equip[1]}!')
    else:
        str_unica = ', '.join(equip[0: -1])
        print(f'{her} irá rumo a batalha com os seguintes equipamentos: {str_unica} e {equip[-1]}!')





anel_rotatorio = input()
lista_anel = anel_rotatorio.split(' - ')
tamanho = int(len(lista_anel))
lista_armas = []
numero_giradas = 0
indice_inicial = 0

#Descobrindo o índice inicial do anel
if tamanho % 2 == 0:
    indice_inicial = int(tamanho/2)
    
elif tamanho % 2 == 1:
    indice_inicial = int(tamanho - 1) / 2

novo_indice = indice_inicial

n = int(input())

for i in range(n):
    entrada = input()
    #O If e o Elif são basicamente iguais, só mudam que dependendo da direção desejada o programa irá somar ou subtrair o índice
    #If usado para caso a entrada vá andar em direção à direita do círculo
    if '>' in entrada:
        #Formatando a entrada para obter a quantidade de vezes que o índice irá mudar
        numero_giradas = int(entrada.replace('>', ''))
        novo_indice = (novo_indice + numero_giradas) % tamanho
        novo_indiceint = int(novo_indice)
        palavra = lista_anel[novo_indiceint]
        adc_ou_ign = input()
        if adc_ou_ign == 'Adicionar':
            if palavra in lista_armas:
                print(f'{palavra} já está na mochila. Não seja gananciosa, ou acabará como Midas!')
            else:
                lista_armas.append(palavra)
                print(f'{palavra} adicionado a mochila!')
        elif adc_ou_ign == 'Ignorar':
            if palavra in lista_armas:
                print(f'{palavra} já está na mochila. Não seja gananciosa, ou acabará como Midas!')
            else:
                print(f'{palavra} não vai ser tão útil assim!')

    #Elif usado para caso a entrada vá andar em direção à esquerda do círculo
    elif '<' in entrada:

        numero_giradas = int(entrada.replace('<', ''))
        novo_indice = (novo_indice - numero_giradas) % tamanho
        novo_indiceint = int(novo_indice)
        palavra = lista_anel[novo_indiceint]
        adc_ou_ign = input()
        if adc_ou_ign == 'Adicionar':
            if palavra in lista_armas:
                print(f'{palavra} já está na mochila. Não seja gananciosa, ou acabará como Midas!')
            else:
                lista_armas.append(palavra)
                print(f'{palavra} adicionado a mochila!')
        elif adc_ou_ign == 'Ignorar':
            if palavra in lista_armas:
                print(f'{palavra} já está na mochila. Não seja gananciosa, ou acabará como Midas!')
            else:
                print(f'{palavra} não vai ser tão útil assim!')

#Outputs finais
if lista_armas == []:
    print('Não achei nada útil no arsenal. Acho que vamos precisar ser menos violentos dessa vez…')

else:
    str_armas = ', '.join(lista_armas)
    print(f'Com {str_armas}, seremos imbatíveis na caça à bandeira!')

m = int(input())
n = int(input())
listcamp = []
matrizgrande = []

#Parte do código em que se constrói a matriz da questão
for i in range(m):
    listcamp = []
    for j in range(1, n + 1):
        campistas = input()
        campint = int(campistas)
        listcamp.append(campint)
        if j == n:
            matrizgrande.append(listcamp)

#Criando um mecanismo que forme uma lista com a soma de campistas de cada andar   
tamanhom = int(len(matrizgrande))
soma = 0
lista_da_soma = []
numero_campistas = float("-inf")
andar_vencedor = 0
for andares in matrizgrande:
    soma = 0
    for campistas in andares:
        soma += campistas
    lista_da_soma.append(soma)

#Mecanismo que descobre qual andar tem mais campistas e quantos campistas o andar tem
tamanho_soma = int(len(lista_da_soma))
for i in range(tamanho_soma):
    if lista_da_soma[i] > numero_campistas:
        numero_campistas = lista_da_soma[i]
        andar_vencedor = i + 1

#Imprimindo a matriz final
strlinha = ''
strfinal = ''
for linha in matrizgrande:
    strfinal = ''
    for elementos_linha in linha:
        elementos_linha_str = str(elementos_linha)
        strlinha = ' '.join(elementos_linha_str)
        strfinal = strfinal + strlinha + ' '
    print(strfinal.strip())

#Imprimindo a última parte do output do código
print('')
print(f'O chalé {andar_vencedor} foi o que mais recebeu semi-deuses, tendo um acréscimo de {numero_campistas} novos campistas!')

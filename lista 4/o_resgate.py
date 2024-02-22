def desafio1(frase_x):
    #Definição do alfabeto minúsculo que usaremos para comparação e da lista de caracteres retirados da frase
    letras_minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    lista_caracteres_input = []
    #Tratamento da frase para que ela fique toda minúscula e seja mais fácil de analisar
    frase_tratada = frase_x.lower()
    #For que adiciona os caracteres da frase em uma lista, sem repetí-los e sem adicionar espaços
    for caracteres in frase_tratada:
        if (caracteres not in lista_caracteres_input) and caracteres != ' ':
            lista_caracteres_input.append(caracteres)
    #Caso a frase seja um panagrama, o tamanho da lista de caracteres será igual ao len(alfabeto), permitindo compararmos o tamanho
    if len(lista_caracteres_input) == len(letras_minusculas):
        numero_letras = float("-inf")
        #For para achar a letra que mais se repete
        for letras in letras_minusculas:
            numero_letras_temporario = frase_tratada.count(letras)
            if numero_letras_temporario > numero_letras:
                numero_letras = numero_letras_temporario
    #Caso a frase não seja um panagrama, seguimos com a seguinte condição para achar a letra que menos se repete
    else:
        numero_letras = float("inf")
        for letras in letras_minusculas:
            numero_letras_temporario = frase_tratada.count(letras)
            if (numero_letras_temporario < numero_letras) and numero_letras_temporario != 0:
                numero_letras = numero_letras_temporario
    coordenada_x = numero_letras
    #Fim da função com return da coordenada X, fiz essa passagem na linha 26 só para seguir um padrão igual ao das demais funções
    return(coordenada_x)

def desafio2(palavra_y):
    palavra_tratada = palavra_y.lower()
    tamanho = int(len(palavra_tratada))
    #Parte do código que obtém uma sequência de Fibonacci de acordo com o tamanho da palavra
    sequencia_fibonacci = [0, 1]
    numero_fibonacci = 0
    for i in range(tamanho - 1):
        sequencia_fibonacci.append(sequencia_fibonacci[-1] + sequencia_fibonacci[-2])
    numero_fibonacci = sequencia_fibonacci[-1]
    #Caso haja vogais na palavra, multiplicamos o último número da sequência por 4, senão, multiplicamos por 2
    for letras in palavra_tratada:
        if letras in 'aeiou':
            coordenada_y = numero_fibonacci * 4
            break
        else:
            coordenada_y = numero_fibonacci * 2
    return(coordenada_y)

def desafio3(palavra_z, frase_z):
    letras_minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letras_maiusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    minusculas_palavra = 0
    maiusculas_palavra = 0
    #For que calcula a quantidade de letras minúsculas e maiúsculas da palavra
    for i in palavra_z:
        if i in letras_minusculas:
            minusculas_palavra += 1
        elif i in letras_maiusculas:
            maiusculas_palavra += 1
    
    diferenca_palavras = minusculas_palavra - maiusculas_palavra

    minusculas_frase = 0
    maiusculas_frase = 0
    #For que calcula a quantidade de letras minúsculas e maiúsculas da frase
    for j in frase_z:
        if j in letras_minusculas:
            minusculas_frase += 1
        elif j in letras_maiusculas:
            maiusculas_frase += 1
    
    diferenca_frases = minusculas_frase - maiusculas_frase

    coordenada_z = int(diferenca_frases ** diferenca_palavras)
    return(coordenada_z)

#Decidi fazer uma função que calculasse a distância para na hora de calculá-la, ficar com um código mais organizado
def calculo_distancia(x_noel, y_noel, z_noel, x_jack, y_jack, z_jack):
    distancia = float(((x_noel - x_jack)** 2 + (y_noel - y_jack)** 2 + (z_noel - z_jack)** 2) ** (1/2))
    return(distancia)

#Recebimento de entradas
#Fiz as ações nas linhas 83, 87 e 92 para quando formos calcular a distância não ficar com os parâmetros muito grandes
frase_x = input()
x_noel = desafio1(frase_x)
print(f'A 1ª coordenada do Papai Noel é: {x_noel}')

palavra_y = input()
y_noel = desafio2(palavra_y)
print(f'A 2ª coordenada do Papai Noel é: {y_noel}')

palavra_z = input()
frase_z = input()
z_noel = desafio3(palavra_z, frase_z)
print(f'A 3ª coordenada do Papai Noel é: {z_noel}')

x_jack = int(input())
y_jack = int(input())
z_jack = int(input())

#Parte final do código
print(f'A distância entre Jack Esqueleto e Papai Noel é: {calculo_distancia(x_noel, y_noel, z_noel, x_jack, y_jack, z_jack):.2f}')
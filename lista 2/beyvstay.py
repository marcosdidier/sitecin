numero_de_apresentacoes = int(input())
nota_coreografia_taylor = 0
nota_figurino_taylor = 0
nota_coreografia_beyonce = 0
nota_figurino_beyonce = 0
nota_rodada_taylor = 0
nota_rodada_beyonce = 0
agregado_taylor = 0
agregado_beyonce = 0
cond = False
i = 0
print('Vai começar! Vamos ver quem é a verdadeira diva!')

#Parte do código que irá captar os inputs para gerar as pontuações de cada rodada
while not cond:
    i += 1 
    print(f'Vai começar a {i}º rodada!')
    nota_coreografia_taylor = int(input())
    nota_figurino_taylor = int(input())
    nota_coreografia_beyonce = int(input())
    nota_figurino_beyonce = int(input())
    nota_rodada_taylor = 4 * nota_coreografia_taylor + 3 * nota_figurino_taylor
    nota_rodada_beyonce = 4 * nota_coreografia_beyonce + 3 * nota_figurino_beyonce

    #Parte que analisa quem venceu cada rodada
    if nota_rodada_taylor > nota_rodada_beyonce:
        print(f'Fim da apresentação! O placar da rodada {i} foi {nota_rodada_taylor}x{nota_rodada_beyonce} para os representantes da Tay.')
        agregado_taylor += 1
        

    else:
        print(f'Fim da apresentação! O placar da rodada {i} foi {nota_rodada_beyonce}x{nota_rodada_taylor} para os representantes da Bey.')
        agregado_beyonce += 1
        
    
    #Parte que analisa a diferença de pontos
    if nota_rodada_taylor - nota_rodada_beyonce > 20 or nota_rodada_beyonce - nota_rodada_taylor > 20:
        print(f'A diferença na pontuação foi de {abs(nota_rodada_taylor - nota_rodada_beyonce)} pontos.')

    else:
        print(f'A diferença de pontos foi de apenas {abs(nota_rodada_taylor - nota_rodada_beyonce)}.')

    #Parte que indica a vencedora final
    if i == numero_de_apresentacoes and agregado_taylor > agregado_beyonce or agregado_taylor == 3:
        print(f'Uuuh! Por um placar de {agregado_taylor} a {agregado_beyonce}, a equipe da Taylor Swift venceu a competição e mostrou que ela é a verdadeira diva do pop!')
        cond = True
    elif i == numero_de_apresentacoes and agregado_beyonce > agregado_taylor or agregado_beyonce == 3:
        print(f'Minha nossa! A equipe da Beyoncé chocou o mundo e venceu a equipe da Taylor Swift por um placar de {agregado_beyonce} a {agregado_taylor}. A Bey é a verdadeira rainha do pop!')
        cond = True

    

        




    

def transf_lista(palavra):
    lista_caracteres = []
    for numero in palavra:
        lista_caracteres.append(numero)
    return(lista_caracteres)

def funcao_preenchimento(lista_caracteres):
    resposta = ''
    if len(lista_caracteres) == 32:
        resposta = lista_caracteres
    else:
        lista_caracteres.insert(0, '0')
        funcao_preenchimento(lista_caracteres)
        resposta = lista_caracteres
    return(resposta)

def funcao_juncao():
    palavrao = ''.join(listona)
    return(palavrao)


palavra = input()
lista_caracteres = transf_lista(palavra)
listona = funcao_preenchimento(lista_caracteres)
palavrote = funcao_juncao()
acertou = ''
tentativas = int(input())
for i in range(tentativas):
    tentativa = input()
    if tentativa in palavrote:
        print('Muito bem! Estamos dentro! Vamos queimar essa cidade!!')
        acertou = 'acertou'
        break
    elif tentativa not in palavrote:
        print('Não é essa a senha, estamos ficando sem tempo.')

if acertou != 'acertou':
    print('Corre Keanu! Eles nos descobriram!!')








        
        
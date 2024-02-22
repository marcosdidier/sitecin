def funcao_calculo(codigo):
    resposta = 0
    #Caso base
    if codigo == 1:
        resposta = 1
    #Passo indutivo
    else:
        if codigo % 2 == 0:
            codigo -= 1
            resposta = codigo * funcao_calculo(codigo - 2)
        else:
            resposta = codigo * funcao_calculo(codigo - 2)
    return(resposta)

codigo = int(input())
senha_de_acesso = funcao_calculo(codigo)
print(senha_de_acesso)
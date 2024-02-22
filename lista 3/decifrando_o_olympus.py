entrada = input()
tamanho = int(len(entrada))
lista = []
mensagem = ''
numerais = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in entrada:
    if i == ' ':
        lista.append(i)
    else:
        iord = ord(i)
        iord_somado = iord + tamanho
        caractere = chr(iord_somado)
        if caractere in numerais:
            caracterestr = str(caractere)
        lista.append(caractere)

if lista == [' ']:
    print('Ué não tem nada para me decifrar aqui')

else:
    mensagem = ''.join(lista)
    if (''.join(mensagem.split())).isalpha():
        print(f'Descobri o que a mensagem significa: {mensagem}')
    else:
        print('Algo de errado não está certo. Será que estou ficando doido?')

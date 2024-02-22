pontuacao = 0
frase = 'a'
quantidade_de_musicas_tocadas = 0


while pontuacao >= 0 and frase != 'long live':
    frase = input()
    if frase == 'os fãs estão formando uma ciranda':
        pontuacao -= 3
    elif frase == 'os fãs estão ligando os flashes e atrapalhando a visão':
        pontuacao -= 2
    elif frase == 'os fãs estão dançando na frente da tela':
        pontuacao -= 2
    elif frase == 'os fãs estão gritando o nome da Taylor e atrapalhando a música':
        pontuacao -= 2
    elif frase == 'os fãs estão cantando as músicas em coro':
        pontuacao += 2
    elif frase == 'houve um pedido de casamento na sessão':
        pontuacao += 2
    else:
        pontuacao += 1
        quantidade_de_musicas_tocadas += 1

if pontuacao < 0:
    print(f'A Taylor só conseguiu cantar {quantidade_de_musicas_tocadas} músicas e a sessão foi interrompida.')

if frase == 'long live':
    print(f'A Taylor conseguiu concluir o show sem muitas interrupções e cantou {quantidade_de_musicas_tocadas} músicas.')


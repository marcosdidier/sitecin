pontuacao = 0
porta1 = 0
porta2 = 0
porta3 = 0
porta4 = 0
porta5 = 0
r1 = 'a'
r2 = 'a'
r3 = 'a'
r4 = 'a'
r5 = 'a'
direcaop1 = str(input())
numerop1 = int(input())

if numerop1 % 2 == 1 and direcaop1 == 'direita':
    porta1 = 150
    if porta1 > 0:
        r1 = 'CERTA'
    else:
        r1 = 'ERRADA'
elif numerop1 % 2 == 0 and direcaop1 == 'esquerda':
    porta1 = 150
    if porta1 > 0:
        r1 = 'CERTA'
    else:
        r1 = 'ERRADA'

else:
    porta1 = -150
    if porta1 > 0:
        r1 = 'CERTA'
    else:
        r1 = 'ERRADA'

direcaop2 = str(input())
corp2 = str(input())
plantap2 = str(input())
macanetap2 = str(input())

if direcaop2 == 'direita' and (corp2 == 'dourada' or corp2 == 'prateada') or ((plantap2 == 'avenca' or plantap2 == 'espadinha') and macanetap2 == 'redonda'):
    porta2 = 200
    if porta2 > 0:
        r2 = 'CERTA'
    else:
        r2 = 'ERRADA'

elif direcaop2 == 'esquerda' and not((corp2 == 'dourada' or corp2 == 'prateada') or ((plantap2 == 'avenca' or plantap2 == 'espadinha') and macanetap2 == 'redonda')):
    porta2 = 200
    if porta2 > 0:
        r2 = 'CERTA'
    else:
        r2 = 'ERRADA'

else:
    porta2 = -200
    if porta2 > 0:
        r2 = 'CERTA'
    else:
        r2 = 'ERRADA'

direcaop3 = str(input())
corp3 = str(input())
numerop3 = int(input())
plantap3 = str(input())
macanetap3 = str(input())

if direcaop3 == 'esquerda' and (numerop3 % 5 == 0 and plantap3 == 'espadinha' and macanetap3 == 'quadrada') or (corp3 == 'perolada'):
    porta3 = 250
    if porta3 > 0:
        r3 = 'CERTA'
    else:
        r3 = 'ERRADA'

elif direcaop3 == 'direita' and not((numerop3 % 5 == 0 and plantap3 == 'espadinha' and macanetap3 == 'quadrada') or (corp3 == 'perolada')):
    porta3 = 250
    if porta3 > 0:
        r3 = 'CERTA'
    else:
        r3 = 'ERRADA'

else:
    porta3 = -250
    if porta3 > 0:
        r3 = 'CERTA'
    else:
        r3 = 'ERRADA'

direcaop4 = str(input())
numerop4 = int(input())

if direcaop4 == 'direita' and numerop4 % 3 == 0 and numerop4 % 2 != 0 and numerop4 % 5 != 0:
    porta4 = 300
    if porta4 > 0:
        r4 = 'CERTA'
    else:
        r4 = 'ERRADA'

elif direcaop4 == 'esquerda' and not(numerop4 % 3 == 0 and numerop4 % 2 != 0 and numerop4 % 5 != 0):
    porta4 = 300
    if porta4 > 0:
        r4 = 'CERTA'
    else:
        r4 = 'ERRADA'

else: 
    porta4 = -300
    if porta4 > 0:
        r4 = 'CERTA'
    else:
        r4 = 'ERRADA'

corp5 = str(input())
numerop5 = int(input())
plantap5 = str(input())
florp5 = str(input())
macanetap5 = str(input())

if corp5 == 'acobreada' and(numerop5 % 2 == 1 or macanetap5 == 'triangular' or macanetap5 == 'quadrada') and plantap5 == 'jiboia':
    porta5 = 500
    if porta5 > 0:
        r5 = 'CERTA'
    else:
        r5 = 'ERRADA'

elif corp5 == 'prateada' and(florp5 != 'margarida' and florp5 != 'papoula' and florp5 != 'cosmos') and (macanetap5 == 'hexagonal' or macanetap5 == 'redonda'):
    porta5 = 450
    if porta5 > 0:
        r5 = 'CERTA'
    else:
        r5 = 'ERRADA'

elif corp5 == 'dourada' and (florp5 == 'lirio' or florp5 == 'ixora') and macanetap5 == 'hexagonal':
    porta5 = 400
    if porta5 > 0:
        r5 = 'CERTA'
    else:
        r5 = 'ERRADA'

else:
    porta5 = -500
    if porta5 > 0:
        r5 = 'CERTA'
    else:
        r5 = 'ERRADA'

pontuacao = porta1 + porta2 + porta3 + porta4 + porta5
print('ARISU, VOCÊ FEZ SUAS ESCOLHAS E AGORA VEREMOS SE ESCOLHEU AS PORTAS CERTAS:')
print(r1, r2, r3, r4, r5)

if pontuacao > 0:
    if 0 < pontuacao < 1300:
        print(f'Você passou com {pontuacao} pontos, mas faça melhores escolhas da próxima vez.')
    elif pontuacao >= 1300:
        print(f'Parece que a sorte está ao seu favor, Arisu... Você conseguiu passar com {pontuacao} pontos!')

elif pontuacao < 0:
    if pontuacao > -1400:
        print(f'Por mais que você tenha feito escolhas corretas, não foi suficiente para sobreviver. Você finalizou o jogo com {pontuacao} pontos')    

    elif pontuacao == -1400:
        print(f'Todas suas escolhas foram erradas, Arisu, esperávamos mais de você... Você será executado pois obteve {pontuacao} pontos.')   




   






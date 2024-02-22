lugarshow = input()
codigo = input()
contagem_vip = 0
conserto = 'a'
cond = False


while not cond:
    if codigo == '0000':
        cond = True
    elif codigo == '1000':
        contagem_vip += 1
        print('Mais um VIP! Não podemos esquecer de contabilizá-lo.')
        codigo = input()
    elif codigo == '1001':
        print('Ingresso Normal. Não iremos contabilizá-lo.')
        codigo = input()
    elif codigo == '1002':
        print('Ele ficará na frente do show, porém não é VIP! Não será contabilizado também.')
        codigo = input()
    elif codigo == '1003':
        print('Espera, quem é esse? Ele não pagou! Não devemos sequer analisar sua entrada.')
        codigo = input()
    elif codigo == '1004':
        print('Esse código não existe! O sistema quebrou...')
        print('Vamos aguardar até que o suporte nos ajude.')
        conserto = input()
        while conserto != 'Ajudou':
            print('Ainda não...')
            conserto = input()
        cond = True

print(f'O show da Taylor Swift será em {lugarshow} e contará com {contagem_vip} VIPs!')



    
    


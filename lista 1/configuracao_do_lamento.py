n1 = int(input())
n2 = 0
n3 = 0
n4 = 0
nfinal = 0
palavra = 'a'
palavra
if n1 > 0:
    n2 = int(input())
    if n1 % 2 == 0:
      n1 *= 2
    else:
        n1 *= 0.5
    if n2 > 0:
        n3 = int(input())
        if n2 % 2 == 0:
           n2 *= 2
        else:
           n2 *= 0.5
    else: 
         print(f'{n2:.2f} não está gravado(a) na caixa, não adianta nem continuar que ela não vai abrir.')
    if n3 > 0:
        palavra = str(input())
        if n3 % 2 == 0:
           n3 *= 2
        else:
           n3 *= 0.5
    else:
        print(f'{n3:.2f} não está gravado(a) na caixa, não adianta nem continuar que ela não vai abrir.')
    if palavra.islower():
        n4 = int(input())
        nfinal = (n1 * n2 * n3 * n4 ) ** (1/2)
        if nfinal >= 10:
            print(f'O número {nfinal:.2f} e a palavra {palavra} eram as respostas. A caixa foi aberta.')
        else:
            print(f'A combinação era muito pequena, a caixa só vai poder ser aberta daqui a {10-nfinal:.2f} anos.')
    else:
        print(f'{palavra} não está gravado(a) na caixa, não adianta nem continuar que ela não vai abrir.')

else:
    print(f'{n1:.2f} não está gravado(a) na caixa, não adianta nem continuar que ela não vai abrir.')
    















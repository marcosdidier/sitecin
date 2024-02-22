l1 = float(input('Digite o primeiro lado: '))
l2 = float(input('Digite o segundo lado: '))
l3 = float(input('Digite o terceiro lado: '))

if l1 == l2 == l3 :
    print('O triângulo é equilátero.')

elif l1 == l2 or l1 == l3 or l2 == l3:
    print('O triângulo é isósceles.')

else:
    print('O triângulo é escaleno')